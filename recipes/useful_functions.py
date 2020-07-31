# -*- coding: utf-8 -*-
from typing import (Any, Callable, Deque, Generator, Iterable, List, Optional,
                    Sequence, TextIO)


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


def datetime_now(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    from datetime import datetime
    return datetime.now().strftime(fmt)


def elapsed_time() -> Generator:
    from time import monotonic
    start = monotonic()
    while True:
        yield monotonic() - start


def shorthand_dict(names):
    """
    >>> context = {"user_id": 42, "user_ip": "1.2.3.4"}
    >>> mode, action_type = "force", 7
    >>> shorthand_dict(["context", #doctest: +NORMALIZE_WHITESPACE
    ... "mode", "action_type"])
    {'context': {'user_id': 42, 'user_ip': '1.2.3.4'},
    'mode': 'force', 'action_type': 7}
    """
    from inspect import currentframe
    lcls = currentframe().f_back.f_locals
    return {k: lcls[k] for k in names}


def ifile(name: str) -> Generator:
    with open(name, encoding='utf-8') as f:
        yield from f


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
            fillvalue: Optional[str] = '') -> Generator[str, None, None]:
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


def amount_unique_elements(seq: Sequence) -> int:
    """
    Amount different mutable/immutable elements

    >>> amount_unique_elements([1, [2], 1, [2], 3])
    4
    """
    return len({id(el) for el in seq})  # len(set(map(id, seq)))
