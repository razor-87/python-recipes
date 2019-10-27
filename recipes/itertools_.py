# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-08-01 11:08:22
# @Last Modified by:   razor87
# @Last Modified time: 2019-10-25 18:10:57
import collections
import itertools
import operator
import random

[*itertools.combinations([1, 2, 3], 2)]
# [(1, 2), (1, 3), (2, 3)]
[*itertools.permutations([1, 2, 3])]
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
[*itertools.accumulate([1, 4, 3, 5], max)]
# [1, 4, 4, 5]

for i in itertools.count(3):
    print(i)
    if i >= 11:
        break

nums = list(itertools.accumulate(range(8)))
list(itertools.takewhile(lambda x: x <= 6, nums))
# [0, 1, 3, 6]

itertools.takewhile(lambda x: x % 2 == 0, [2, 4, 6, 7, 9, 8])

# list(map(pow, [(2, 5), (3, 2), (10, 3)]))
# -> TypeError: pow expected at least 2 arguments, got 1
list(itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)]))
# [32, 9, 1000]

list(itertools.compress('abcd', [0, 1, 1, 0]))
# ['b', 'c']

list(itertools.chain.from_iterable([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
list(itertools.chain.from_iterable((range(1, 4), range(4, 7), range(7, 10))))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

list(itertools.filterfalse(vowel, 'Aardvark'))
# ['r', 'd', 'v', 'r', 'k']
list(itertools.dropwhile(vowel, 'Aardvark'))
# ['r', 'd', 'v', 'a', 'r', 'k']
list(itertools.takewhile(vowel, 'Aardvark'))
# ['A', 'a']
list(itertools.compress('Aardvark', (1, 0, 1, 1, 0, 1)))
# ['A', 'r', 'd', 'a']
list(itertools.islice('Aardvark', 4))
# ['A', 'a', 'r', 'd']
list(itertools.islice('Aardvark', 4, 7))
# ['v', 'a', 'r']
list(itertools.islice('Aardvark', 1, 7, 2))
# ['a', 'd', 'a']

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
list(itertools.accumulate(sample))
# [5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
list(itertools.accumulate(sample, min))
# [5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
list(itertools.accumulate(sample, max))
# [5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
list(itertools.accumulate(sample, operator.mul))
# [5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]
list(itertools.accumulate(range(1, 11), operator.mul))  # list of factorials
# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
list(enumerate('albatroz', 1))
# [(1, 'a'), (2, 'l'), (3, 'b'), (4, 'a'), (5, 't'), (6, 'r'), (7, 'o'), (8, 'z')]
list(map(operator.mul, range(11), range(11)))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list(map(operator.mul, range(11), [2, 4, 8]))
# [0, 4, 16]
list(map(lambda a, b: (a, b), range(11), [2, 4, 8]))
# [(0, 2), (1, 4), (2, 8)]
list(itertools.starmap(operator.mul, enumerate('albatroz', 1)))
# ['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']
# sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
list(
    itertools.starmap(lambda a, b: b / a,
                      enumerate(itertools.accumulate(sample), 1)))
# [5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333,
# 5.0, 4.375, 4.888888888888889, 4.5]
list(itertools.chain('ABC', range(2)))
# ['A', 'B', 'C', 0, 1]
list(itertools.chain(enumerate('ABC')))
# [(0, 'A'), (1, 'B'), (2, 'C')]
list(itertools.chain.from_iterable(enumerate('ABC')))
# [0, 'A', 1, 'B', 2, 'C']
list(zip('ABC', range(5)))
# [('A', 0), ('B', 1), ('C', 2)]
list(zip('ABC', range(5), [10, 20, 30, 40]))
# [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]
list(itertools.zip_longest('ABC', range(5)))
# [('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
list(itertools.zip_longest('ABC', range(5), fillvalue='?'))
# [('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]
list(itertools.product('ABC', range(2)))
# [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
# suits = 'spades hearts diamonds clubs'.split()
list(itertools.product('AK', suits))
# [('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'),
# ('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]
list(itertools.product('ABC'))
# [('A',), ('B',), ('C',)]
list(itertools.product('ABC', repeat=2))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'),
# ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
list(itertools.product(range(2), repeat=3))
# [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0),
# (1, 0, 1), (1, 1, 0), (1, 1, 1)]
rows = itertools.product('AB', range(2), repeat=2)
for row in rows:
    print(row)
# ('A', 0, 'A', 0)
# ('A', 0, 'A', 1)
# ('A', 0, 'B', 0)
# ('A', 0, 'B', 1)
# ('A', 1, 'A', 0)
# ('A', 1, 'A', 1)
# ('A', 1, 'B', 0)
# ('A', 1, 'B', 1)
# ('B', 0, 'A', 0)
# ('B', 0, 'A', 1)
# ('B', 0, 'B', 0)
# ('B', 0, 'B', 1)
# ('B', 1, 'A', 0)
# ('B', 1, 'A', 1)
# ('B', 1, 'B', 0)
# ('B', 1, 'B', 1)

ct = itertools.count()
next(ct)
# 0
next(ct), next(ct), next(ct)
# (1, 2, 3)
list(itertools.islice(itertools.count(1, .3), 3))
# [1, 1.3, 1.6]
cy = itertools.cycle('ABC')
next(cy)
# 'A'
list(itertools.islice(cy, 7))
# ['B', 'C', 'A', 'B', 'C', 'A', 'B']
rp = itertools.repeat(7)
next(rp), next(rp)
# (7, 7)
list(itertools.repeat(8, 4))
# [8, 8, 8, 8]
list(map(operator.mul, range(11), itertools.repeat(5)))
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
list(itertools.combinations('ABC', 2))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
list(itertools.combinations_with_replacement('ABC', 2))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
list(itertools.permutations('ABC', 2))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
list(itertools.groupby('LLLLAAGGG'))
# [('L', <itertools._grouper object at 0x102227cc0>),
# ('A', <itertools._grouper object at 0x102227b38>),
# ('G', <itertools._grouper object at 0x102227b70>)]
for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))
# L -> ['L', 'L', 'L', 'L']
# A -> ['A', 'A',]
# G -> ['G', 'G', 'G']
animals = [
    'duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark',
    'lion'
]
animals.sort(key=len)
animals
# ['rat', 'bat', 'duck', 'bear', 'lion', 'eagle', 'shark', 'giraffe', 'dolphin']
for length, group in itertools.groupby(animals, len):
    print(length, '->', list(group))
# 3 -> ['rat', 'bat']
# 4 -> ['duck', 'bear', 'lion']
# 5 -> ['eagle', 'shark']
# 7 -> ['giraffe', 'dolphin']
for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))
# 7 -> ['dolphin', 'giraffe']
# 5 -> ['shark', 'eagle']
# 4 -> ['lion', 'bear', 'duck']
# 3 -> ['bat', 'rat']
list(itertools.tee('ABC'))
# [<itertools._tee object at 0x10222abc8>, <itertools._tee object at 0x10222ac08>]
g1, g2 = itertools.tee('ABC')
next(g1)
# 'A'
next(g2)
# 'A'
next(g2)
# 'B'
list(g1)
# ['B', 'C']
list(g2)
# ['C']
list(zip(*itertools.tee('ABC')))
# [('A', 'A'), ('B', 'B'), ('C', 'C')]

for c in itertools.chain(range(3), range(12, 15)):
    print(c)

# itertools.permutations() generates permutations
# for an iterable. Time to brute-force those passwords ;-)
for p in itertools.permutations('ABCD'):
    print(p)
# ('A', 'B', 'C', 'D')
# ('A', 'B', 'D', 'C')
# ('A', 'C', 'B', 'D')
# ('A', 'C', 'D', 'B')
# ('A', 'D', 'B', 'C')
# ('A', 'D', 'C', 'B')
# ('B', 'A', 'C', 'D')
# ('B', 'A', 'D', 'C')
# ('B', 'C', 'A', 'D')
# ('B', 'C', 'D', 'A')
# ('B', 'D', 'A', 'C')
# ('B', 'D', 'C', 'A')
# ('C', 'A', 'B', 'D')
# ('C', 'A', 'D', 'B')
# ('C', 'B', 'A', 'D')
# ('C', 'B', 'D', 'A')
# ('C', 'D', 'A', 'B')
# ('C', 'D', 'B', 'A')
# ('D', 'A', 'B', 'C')
# ('D', 'A', 'C', 'B')
# ('D', 'B', 'A', 'C')
# ('D', 'B', 'C', 'A')
# ('D', 'C', 'A', 'B')
# ('D', 'C', 'B', 'A')

lst = list(itertools.zip_longest('ABCD', 'xy', fillvalue='-'))
# Ax By C- D-

(*itertools.combinations_with_replacement('ABC', 2),)
# (('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C'))


# https://docs.python.org/3/library/itertools.html#itertools-recipes
def take(n, iterable):
    """Return first n items of the iterable as a list"""
    return list(itertools.islice(iterable, n))


def prepend(value, iterator):
    """Prepend a single value in front of an iterator"""
    # prepend(1, [2, 3, 4]) -> 1 2 3 4
    return itertools.chain([value], iterator)


def tabulate(function, start=0):
    """Return function(0), function(1), ..."""
    return map(function, itertools.count(start))


def tail(n, iterable):
    """Return an iterator over the last n items"""
    # tail(3, 'ABCDEFG') --> E F G
    return iter(collections.deque(iterable, maxlen=n))


def consume(iterator, n=None):
    """Advance the iterator n-steps ahead. If n is None, consume entirely."""
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(itertools.islice(iterator, n, n), None)


def nth(iterable, n, default=None):
    """Returns the nth item or a default value"""
    return next(itertools.islice(iterable, n, None), default)


def all_equal(iterable):
    """Returns True if all the elements are equal to each other"""
    g = itertools.groupby(iterable)
    return next(g, True) and not next(g, False)


def padnone(iterable):
    """Returns the sequence elements and then returns None indefinitely.

    Useful for emulating the behavior of the built-in map() function.
    """
    return itertools.chain(iterable, itertools.repeat(None))


def ncycles(iterable, n):
    """Returns the sequence elements n times"""
    return itertools.chain.from_iterable(itertools.repeat(tuple(iterable), n))


def dotproduct(vec1, vec2):
    return sum(map(operator.mul, vec1, vec2))


def flatten(nested_lists):
    """Flatten one level of nesting"""
    return itertools.chain.from_iterable(nested_lists)


def repeatfunc(func, times=None, *args):
    """Repeat calls to func with specified arguments.

    Example:  repeatfunc(random.random)
    """
    if times is None:
        return itertools.starmap(func, itertools.repeat(args))
    return itertools.starmap(func, itertools.repeat(args, times))


def pairwise(iterable):
    """s -> (s0,s1), (s1,s2), (s2, s3), ..."""
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def grouper(iterable, n, fillvalue=None):
    """Collect data into fixed-length chunks or blocks"""
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"""
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def roundrobin(*iterables):
    """roundrobin('ABC', 'D', 'EF') --> A D E B F C"""
    # Recipe credited to George Sakkis
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


def partition(pred, iterable):
    """Use a predicate to partition entries into false entries and true entries"""
    # partition(is_odd, range(10)) --> 0 2 4 6 8   and  1 3 5 7 9
    t1, t2 = itertools.tee(iterable)
    return itertools.filterfalse(pred, t1), filter(pred, t2)


def powerset(iterable):
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1))


def unique_everseen(iterable, key=None):
    """List unique elements, preserving order. Remember all elements ever seen."""
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in itertools.filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


def unique_justseen(iterable, key=None):
    """List unique elements, preserving order. Remember only the element just seen."""
    # unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
    # unique_justseen('ABBCcAD', str.lower) --> A B C A D
    return map(next,
               map(operator.itemgetter(1), itertools.groupby(iterable, key)))
