# -*- coding: utf-8 -*-
from typing import Generator, Iterable


def ifile(name: str) -> Generator:
    with open(name, encoding='utf-8') as f:
        yield from f


def elapsed_time() -> Generator:
    from time import monotonic
    start = monotonic()
    while True:
        yield monotonic() - start


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


def fibonacci_gen(num: int) -> Generator:
    """
    >>> [*fibonacci_gen(10)]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    a = b = 1
    for _ in range(num):
        yield a
        a, b = b, a + b


def unique_stable(arr: Iterable) -> Generator:
    dupes = set()
    for val in arr:
        if val not in dupes:
            dupes.add(val)
            yield val


def chunks(g, n=2):
    """
    Collect data into chunks of a maximum size
    chunks('ABCDEFG', 3) --> ABC DEF G
    """
    from itertools import islice, repeat
    yield from map(lambda it: islice(it, n), repeat(iter(g)))


def chunks_(string, k):
    yield from zip(*(iter(string), ) * k)


def grouper(iterable, n, fillvalue=''):
    """
    Collect data into fixed-length chunks or blocks
    grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx

    >>> big_string = "gfdgfgdgdbvcgjkjhddfgr hfghfgf kjhkhjtgg ghfvbvcbcvfhjkh"
    >>> '\n'.join(''.join(chunk) for chunk in grouper(big_string, 10, '_'))
    'gfdgfgdgdb\nvcgjkjhddf\ngr hfghfgf\n kjhkhjtgg\n ghfvbvcbc\nvfhjkh____'
    """
    from itertools import zip_longest
    args = (iter(iterable), ) * n
    yield from zip_longest(fillvalue=fillvalue, *args)


def moving_average(iterable, n=3):
    """
    http://en.wikipedia.org/wiki/Moving_average
    moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    """
    from collections import deque
    from itertools import islice
    it = iter(iterable)
    d = deque(islice(it, n - 1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n


def iter_except(func, exception, first=None):
    """
    Call a function repeatedly until an exception is raised.
    Converts a call-until-exception interface to an iterator interface.
    Like builtins.iter(func, sentinel) but uses an exception instead
    of a sentinel to end the loop.

    priority queue - iter_except(functools.partial(heappop, h), IndexError)
    non-blocking dict - iter_except(d.popitem, KeyError)
    non-blocking set -  iter_except(s.pop, KeyError)
    non-blocking deque - iter_except(d.popleft, IndexError)
    loop over a producer Queue - iter_except(q.get_nowait, Queue.Empty)
    """
    try:
        if first is not None:
            # For database APIs needing an initial cast to db.first()
            yield first()
        while True:
            yield func()
    except exception:
        pass


def roundrobin(*iterables):
    """
    Recipe credited to George Sakkis
    roundrobin('ABC', 'D', 'EF') --> A D E B F C
    """
    import itertools
    num_active = len(iterables)
    nexts = itertools.cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = itertools.cycle(itertools.islice(nexts, num_active))


def unique_everseen(iterable, key=None):
    """
    List unique elements, preserving order. Remember all elements ever seen.
    unique_everseen('AAAABBBCCDAABBB') --> A B C D
    unique_everseen('ABBCcAD', str.lower) --> A B C D
    """
    from itertools import filterfalse
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


def yield_from_merging(*iterables, sorting=True, reverse=False, key=None):
    """
    >>> [*yield_from_merging([5, 3, 1, 0], [7, 8, 0, 9, 8])]
    [0, 0, 1, 3, 5, 7, 8, 8, 9]
    >>> [*yield_from_merging([5, 3, 1, 0], [7, 8, 0, 9, 8], reverse=True)]
    [9, 8, 8, 7, 5, 3, 1, 0, 0]
    """
    from heapq import merge
    if sorting:
        iterables = (sorted(iterable, reverse=reverse, key=None)
                     for iterable in iterables)
    yield from merge(*iterables, reverse=reverse, key=None)
