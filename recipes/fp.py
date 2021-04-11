# -*- coding: utf-8 -*-
"""
built-in:
    all(iterable)                                -> bool
    any(iterable)                                -> bool
    callable(object)                             -> bool
    dir([object])                                -> list of strings
    enumerate(iterable, start=0)                 -> enumerate object
    filter(function or None, iterable)           -> filter object
    hash(object)                                 -> int
    id(object)                                   -> int
    len(sequence)                                -> int
    map(func, *iterables)                        -> map object
    max(arg1, arg2, *args[, key])                -> value
    max(iterable, *[, key, default])             -> value
    min(arg1, arg2, *args[, key])                -> value
    min(iterable, *[, key, default])             -> value
    range(start, stop[, step])                   -> range object
    range(stop)                                  -> range object
    reversed(sequence)                           -> reversed object
    sorted(iterable, *, key=None, reverse=False) -> list
    sum(iterable, /, start=0)                    -> value
    zip(*iterables)                              -> zip object
"""

import math
from functools import reduce
from operator import add, itemgetter, iconcat, mul

(lambda x, y: x + y)(5, 3)
# 8
gen = (lambda s: (yield from s))('abs')
next(gen), next(gen), next(gen)
# ('a', 'b', 's')


xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
dict(map(itemgetter(1, 0), xs.items()))
# {4: 'a', 3: 'b', 2: 'c', 1: 'd'}
sorted(xs.items(), key=itemgetter(1))  # == key=lambda x: x[1]
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
sorted([(0, 1), (0, 1), (0, 1)], key=itemgetter(1), reverse=True)
# [(0, 1), (0, 1), (0, 1)]
sorted([[1], [1, 1, 1], [1, 1]], reverse=True, key=len)  # sort by len
# [[1, 1, 1], [1, 1], [1]]
sorted(["ba", "ab", "aa", "aaa"], key=lambda x: (len(x), x))
# ['aa', 'ab', 'ba', 'aaa']
list_b = [28, 14, '28', 5, '9', '1']
sorted(list_b, key=int)
# ['1', 5, '9', 14, 28, '28']
sorted(list_b, key=str)
# ['1', 14, 28, '28', 5, '9']
sorted(range(-5, 6), key=abs)
# [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]
arr = [*"Sorting1234"]
sorted((*map(int, (c.isdigit(), c in '02468', c.isupper())), c) for c in arr)
# [(0, 0, 0, 'g'),
#  (0, 0, 0, 'i'),
#  (0, 0, 0, 'n'),
#  (0, 0, 0, 'o'),
#  (0, 0, 0, 'r'),
#  (0, 0, 0, 't'),
#  (0, 0, 1, 'S'),
#  (1, 0, 0, '1'),
#  (1, 0, 0, '3'),
#  (1, 1, 0, '2'),
#  (1, 1, 0, '4')]
sorted(arr, key=lambda c: (c.isdigit(), c in '02468', c.isupper(), c))
# ['g', 'i', 'n', 'o', 'r', 't', 'S', '1', '3', '2', '4']

[*enumerate('abc')]
# [(0, 'a'), (1, 'b'), (2, 'c')]
[*enumerate('abc', 1)]
# [(1, 'a'), (2, 'b'), (3, 'c')]

[*map(lambda a, b: (a, b), range(11), [2, 4, 8])]
# [(0, 2), (1, 4), (2, 8)]
[*map(list, map(range, [0, 2], [5, 11], [1, 2]))]
# [[0, 1, 2, 3, 4], [2, 4, 6, 8, 10]]
l1, l2 = [(1, 1), (2, 2), (3, 3)], [(4, 4), (5, 5), (6, 6)]
[[*map(sum, zip(*t))] for t in zip(l1, l2)]
# [[5, 5], [7, 7], [9, 9]]
{*map(str.upper, {'a', 'b'})}
# {'A', 'B'}
A, B = [1, 2, 3, 4], [2, 3, 5, 7]
[*map(add, A, B)]  # == [*map(sum, zip(A, B))]
# [3, 5, 8, 11]
''.join(map(str, range(20)))
# '012345678910111213141516171819'

arr = [(1, 'a'), (3, 'c'), (4, 'e'), (-1, 'z')]
max(arr)
# (4, 'e')
max(arr, key=lambda x: x[1])
# (-1, 'z')
min(arr, key=lambda x: x[1])
# (1, 'a')
[min(i) for i in zip([1, 5, 8], [3, 4, 7])]
# [1, 4, 7]

[*filter(lambda x: x % 2 == 0, range(16))]
# [0, 2, 4, 6, 8, 10, 12, 14]
[*filter(lambda a: a > 0, range(-2, 3))]  # is_positive
# [1, 2]
[*filter(bool, range(3))]  # == [x for x in range(3) if x]
# [1, 2]
[*filter(lambda k: math.gcd(k, 20) == 1, range(1, 21))]
# [1, 3, 7, 9, 11, 13, 17, 19]
[*filter(lambda x: x.isdigit(), ['d', '1', 'f', '5'])]
# ['1', '5']
len([*filter(lambda x: x & 1 == 0, range(1001))])
# 501

my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
sum(sub[1] for sub in my_list)
# 60
sum(1 for i in [3, 3, 4, 4, 3] if i == 4)
# 2
sum("text".encode('utf-8'))
# 453
a, b = {1, 2, 3}, {4, 5, 6}
sum((i in a) - (i in b) for i in [2, 6, 3, 2, 5, 1])
# 2
sum(x & 1 == 0 for x in range(1001))
# 501
sum([[1], [2], [3]], [])
# [1, 2, 3]
U, V = [1, 2, 3], [2, 3, 5]
sum(map(mul, U, V))  # == sum(map(int.__mul__, U, V))
# 23

reduce(iconcat, [[1], [2], [3]], [])
# [1, 2, 3]
reduce(mul, range(1, 11))  # == math.factorial(10)
# 3628800
reduce(pow, [3, 2, 2])  # == 3**(2**2)
# 81
reduce(mul, ((3 << 1) + 3 for _ in range(1, 51)))  # == 3**100
# 515377520732011331036461129765621272702107522001

[*zip('ABC', range(5))]
# [('A', 0), ('B', 1), ('C', 2)]
[*zip('ABC', range(5), [10, 20, 30, 40])]
# [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]
[*zip(range(7), [x**2 for x in range(7)])]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]
eng, ger = ['one', 'two', 'three'], ['eins', 'zwei', 'drei']
[*zip(eng, ger)]
# [('one', 'eins'), ('two', 'zwei'), ('three', 'drei')]
[*zip(*zip(eng, ger))]
# [('one', 'two', 'three'), ('eins', 'zwei', 'drei')]
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
[*zip(*matrix)]
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
s = 'abcdefghi'
[*zip(s, s, s)]
# [('a', 'a', 'a'), ('b', 'b', 'b'), ('c', 'c', 'c'),
#  ('d', 'd', 'd'), ('e', 'e', 'e'), ('f', 'f', 'f'),
#  ('g', 'g', 'g'), ('h', 'h', 'h'), ('i', 'i', 'i')]
i = iter(s)
[*zip(i, i, i)]
# [('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i')]
[*zip(*(iter(s), ) * 3)]
# [('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i')]
for part in zip(*(iter(s), ) * 3):
    print(part)
# ('a', 'b', 'c')
# ('d', 'e', 'f')
# ('g', 'h', 'i')
nums = range(10)
[*zip(nums[::2], nums[1::2])]
# [(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
dict(zip(nums[::2], nums[1::2]))  # == dict.update(zip(nums[::2], nums[1::2]))
# {0: 1, 2: 3, 4: 5, 6: 7, 8: 9}
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
[*zip(*pairs)]  # Unzipping a Sequence
# (1, 2, 3, 4), ('a', 'b', 'c', 'd')

any([])
# False
k, g = map(iter, ((1, 1, 0, 1, 1), range(5)))
any(map(lambda _: next(k) == 0, g)), [*k], [*g]
# (True, [1, 1], [3, 4])
any(i in [3, 4] for i in [1, 2, 3])  # Matching partial list
# True

all([])
# True
all(x == round((x**3)**(1 / 3)) for x in range(5))
# True
all({x**3: x == round((x**3)**(1 / 3)) for x in range(5)}.values())
# True
