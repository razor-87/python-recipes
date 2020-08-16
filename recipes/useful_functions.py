# -*- coding: utf-8 -*-
from typing import (Any, Callable, Deque, Generator, Iterable, List, Optional,
                    Sequence, TextIO, Tuple)


def array_shift(data: Iterable, shift: int) -> Deque:
    """
    left(-) or right(+) shift of array

    >>> arr = range(10)
    >>> array_shift(arr, -3)
    deque([3, 4, 5, 6, 7, 8, 9, 0, 1, 2])
    >>> array_shift(arr, 3)
    deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6])
    """
    from collections import deque
    deq = deque(data)
    deq.rotate(shift)
    return deq


def find_idx(required_el: Any, lst: List[Any]) -> Optional[int]:
    # list.index() without raise an exception
    if required_el in {*lst}:
        return lst.index(required_el)
    return None


def bytes2human(bts: int) -> str:
    """
    http://code.activestate.com/recipes/578019

    >>> bytes2human(10000)
    '9.8K'
    >>> bytes2human(100001221)
    '95.4M'
    """
    symbols = "YZEPTGMK"
    nums = (1 << i for i in range(80, 9, -10))
    return next((f"{bts / n:.1f}{s}"
                 for s, n in zip(symbols, nums) if bts >= n), f"{bts}B")


def int_to_bytes(integer: int,
                 *,
                 byteorder: str = 'big') -> Tuple[bytes, bool]:
    if integer < 0:
        return (integer.to_bytes((((integer + 1).bit_length() + 8) // 8),
                                 byteorder=byteorder,
                                 signed=True), True)
    return (integer.to_bytes(((integer.bit_length() + 7) // 8),
                             byteorder=byteorder), False)


def int_from_bytes(bytes_sign: Tuple[bytes, bool],
                   *,
                   byteorder: str = 'big',
                   signed: bool = False) -> int:
    bytes_, signed = bytes_sign
    return int.from_bytes(bytes_, byteorder='big', signed=signed)


def datetime_now(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    from datetime import datetime
    return datetime.now().strftime(fmt)


def elapsed_time() -> Generator:
    from time import monotonic
    start = monotonic()
    while True:
        yield monotonic() - start


def ifile(name: str) -> Generator:
    with open(name, encoding='utf-8') as f:
        yield from f


def file_processing(file_name, processing):
    with open(f"{file_name}") as f:
        for line in iter(f.readline, ''):
            processing(line)


def seek_next_line(f):
    for _ in iter(lambda: f.read(1), '\n'):
        ...


def download_file_in_chunks(url, filename, chunk_size=512):
    from requests import get
    response = get(url, stream=True, allow_redirects=True)
    with open(filename, "wb") as handle:
        # handle.write(response.content)
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:  # filter out keep-alive new chunks
                handle.write(chunk)


def follow_file(filename):
    """
    Generator that produces a sequenceof lines being written at the end
    """
    from os import SEEK_END
    from time import sleep

    with open(filename, 'r') as f:
        f.seek(0, SEEK_END)
        while True:
            line = f.readline()
            if line:  # line != ''
                yield line  # Emit a line
            else:
                sleep(0.1)  # Sleep briefly to avoid busy wait


def parse_data(filename):
    """
    Example of iterating over lines of a file with an extra lineno attribute
    """
    with open(filename, 'r') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                _ = int(fields[1])
            except ValueError as e:
                print(f'Line {lineno}: Parse error: {e}')


def parse_csv_data(lines, types, headers=None, indices=None):
    from csv import reader
    rows = reader(lines)
    if indices:
        rows = ([row[index] for index in indices] for row in rows)
    converted = ([func(val) for func, val in zip(types, row)] for row in rows)
    if headers:
        return (dict(zip(headers, row)) for row in converted)
    return converted


def string_filter(s: str, method: Callable) -> str:
    """
    >>> string_filter('1s6 1g7 599h 29h89 0d53', method=str.isdigit)
    '16175992989053'
    >>> string_filter('16 17 599 2989 053', method=str.isalpha)
    ''
    """
    return ''.join(filter(method, s))


def string_to_dict(s: str,
                   *,
                   key_first: bool = True,
                   types: Optional[Sequence] = None) -> dict:
    lst = s.split()
    even_pos, odd_pos = lst[::2], lst[1::2]
    keys, values = (even_pos, odd_pos) if key_first else (odd_pos, even_pos)
    zipped = zip(keys, values)
    if types is None:
        return dict(zipped)
    key_type, value_type = types if key_first else reversed(types)
    return {key_type(key): value_type(value) for key, value in zipped}


def search_lines(lines: TextIO, pattern: str, history: int = 5) -> Generator:
    from collections import deque
    previous_lines: deque = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def yield_from_merging(*iterables, sorting=True, reverse=False, key=None):
    """
    >>> [*yield_from_merging([5, 3, 1, 0], [7, 8, 0, 9, 8])]
    [0, 0, 1, 3, 5, 7, 8, 8, 9]
    >>> [*yield_from_merging([5, 3, 1, 0], [7, 8, 0, 9, 8], reverse=True)]
    [9, 8, 8, 7, 5, 3, 1, 0, 0]
    """
    from heapq import merge
    if sorting:
        iterables = (sorted(iterable, reverse=reverse, key=key)
                     for iterable in iterables)
    yield from merge(*iterables, reverse=reverse, key=key)


def chain(*iterables: Iterable) -> Generator:
    """
    >>> [*chain(['A', 'B', 'C'], [0, 1, 2])]
    ['A', 'B', 'C', 0, 1, 2]
    """
    for i in iterables:
        yield from i


def flatten(nested_lists):
    """Flatten one level of nesting.

    >>> [*flatten([[0, 1], [2, 3]])]
    [0, 1, 2, 3]
    """
    from itertools import chain
    return chain.from_iterable(nested_lists)


def updown(n: int) -> Generator:
    """
    >>> [*updown(3)]
    [1, 2, 3, 2, 1]
    """
    yield from range(1, n)
    yield from range(n, 0, -1)


def chunks(g, n=2):
    """
    Collect data into chunks of a maximum size
    chunks('ABCDEFG', 3) --> ABC DEF G

    """
    from itertools import islice, repeat
    yield from map(lambda it: islice(it, n), repeat(iter(g)))


def chunks_(string, k):
    yield from zip(*(iter(string), ) * k)


def grouper(iterable: Iterable,
            n: int,
            fillvalue: Optional[str] = None) -> Generator[str, None, None]:
    """
    Collect data into fixed-length chunks or blocks
    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx

    >>> big_string = "gfdgfgdgdbvcgjkjhddfgr hfghfgf kjhkhjtgg ghfvbvcbcvfhjkh"
    >>> [''.join(chunk) for chunk #doctest: +NORMALIZE_WHITESPACE
    ... in grouper(big_string, 10, '_')]
    ['gfdgfgdgdb', 'vcgjkjhddf', 'gr hfghfgf',
    ' kjhkhjtgg', ' ghfvbvcbc', 'vfhjkh____']
    """
    from itertools import zip_longest
    args = (iter(iterable), ) * n
    yield from zip_longest(fillvalue=fillvalue, *args)


def unique_stable(it: Iterable, seen: Optional[Iterable] = None) -> Generator:
    """
    List unique elements, preserving order. Remember all elements ever seen.

    >>> ''.join(unique_stable('AAAABBBCCDAABBB'))
    'ABCD'
    >>> ''.join(unique_stable('AAAABBBCCDAABBB', 'B'))
    'ACD'
    """
    from itertools import filterfalse
    seen = set(seen or [])
    for el in filterfalse(seen.__contains__, it):  # if el not in seen
        seen.add(el)
        yield el


def unique_justseen(iterable, key=None):
    """
    List unique elements, preserving order. Remember only the element just seen.
    unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
    unique_justseen('ABBCcAD', str.lower) --> A B C A D

    """
    from itertools import groupby
    from operator import itemgetter
    return map(next, map(itemgetter(1), groupby(iterable, key)))


def amount_unique_elements(seq: Sequence) -> int:
    """
    Amount different mutable/immutable elements

    >>> amount_unique_elements([1, [2], 1, [2], 3])
    4
    """
    return len({id(el) for el in seq})  # len(set(map(id, seq)))


def invert_dict(dct: dict) -> dict:
    """
    >>> invert_dict({'a': 4, 'b': 3, 'c': 2, 'd': 1})
    {4: 'a', 3: 'b', 2: 'c', 1: 'd'}
    """
    from operator import itemgetter
    invert = itemgetter(1, 0)
    items = dct.items()
    return dict(map(invert, items))  # type: ignore


def is_vowel(char):
    """
    >>> [*filter(is_vowel, 'Aardvark')]
    ['A', 'a', 'a']
    """
    return char.lower() in "aeiou"


def maximum_sum(list_of_lists):
    """
    >>> list_of_lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
    >>> maximum_sum(list_of_lists)
    33
    """
    return sum(max(list_of_lists, key=sum))


def sum_nest_elem(lst: List[List[int]], i: int) -> int:
    """
    >>> lst, i = [[1, 2, 3], [40, 50, 60], [9, 8, 7]], 1
    >>> sum_nest_elem(lst, i)
    60
    """
    return sum(sub[i] for sub in lst)


def first_true(iterable, default=False, pred=None):
    """Returns the first true value in the iterable.
    If no true value is found, returns *default*
    If *pred* is not None, returns the first item
    for which pred(item) is true.
    first_true([a,b,c], x) --> a or b or c or x
    first_true([a,b], x, f) --> a if f(a) else b if f(b) else x

    """
    return next(filter(pred, iterable), default)


def quantify(iterable, pred=bool):
    """Count how many times the predicate is true"""
    return sum(map(pred, iterable))


def pattern_in_string(pattern, string):
    n = len(string) - len(pattern) + 1
    # return sum(string[i:].startswith(pattern) for i in range(n))
    return sum(sub_string == pattern
               for sub_string in (string[i:i + len(pattern)]
                                  for i in range(n)))


def tail(n, iterable):
    """Return an iterator over the last n items"""
    # tail(3, 'ABCDEFG') --> E F G
    from collections import deque
    return iter(deque(iterable, maxlen=n))


def take(n, iterable):
    """Return first n items of the iterable as a list"""
    from itertools import islice
    return [*islice(iterable, n)]


def nth(iterable, n, default=None):
    """Returns the nth item or a default value"""
    from itertools import islice
    return next(islice(iterable, n, None), default)


def tabulate(function, start=0):
    """Return function(0), function(1), ..."""
    from itertools import count
    return map(function, count(start))


def ncycles(iterable, n):
    """Returns the sequence elements n times"""
    from itertools import chain, repeat
    return chain.from_iterable(repeat(iterable, n))


def pairwise(iterable):
    """s -> (s0, s1), (s1, s2), (s2, s3), ..."""
    from itertools import tee
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def partition(pred, iterable):
    """
    Use a predicate to partition entries into false entries and true entries
    partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9

    """
    from itertools import filterfalse, tee
    t1, t2 = tee(iterable)
    return filterfalse(pred, t1), filter(pred, t2)
