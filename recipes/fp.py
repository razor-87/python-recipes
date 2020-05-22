# -*- coding: utf-8 -*-
"""
built-in:
    all(iterable) -> bool
    any(iterable) -> bool
    callable(object) -> bool
    dir([object]) -> list of strings
    enumerate(iterable, start=0) -> enumerate object
    filter(function or None, iterable) -> filter object
    hash(object) -> int
    id(object) -> int
    len(sequence) -> int
    map(func, *iterables) -> map object
    max(iterable, *[, key, default]) -> value
    max(arg1, arg2, *args[, key]) -> value
    min(iterable, *[, key, default]) -> value
    min(arg1, arg2, *args[, key]) -> value
    range(stop) -> range object
    range(start, stop[, step]) -> range object
    reversed(sequence) -> reversed object
    sorted(iterable, *, key=None, reverse=False) -> list
    sum(iterable, /, start=0) -> value
    zip(*iterables) -> zip object
"""
import collections
import functools
import itertools
import math
import operator
from typing import List

(lambda x: x**2)(2)
# 4
(lambda x, y: x + y)(5, 3)
# 8
gen = (lambda s: (yield from s))('abs')
next(gen), next(gen), next(gen)
# ('a', 'b', 's')

[*reversed([3, 2, 1, 0])] == [0, 1, 2, 3]
# True

[f"{op}()" for op in dir(operator) if not op.startswith('_')][:3]
# ['abs()', 'add()', 'and_()']

xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sorted(xs.items(), key=operator.itemgetter(1))  # == key=lambda x: x[1]
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]
sorted([(0, 1), (0, 1), (0, 1)], key=operator.itemgetter(1), reverse=True)
# [(0, 1), (0, 1), (0, 1)]
sorted([[1], [1, 1, 1], [1, 1]], reverse=True, key=len)  # sort by len
# [[1, 1, 1], [1, 1], [1]]
sorted(["ba", "ab", "aa", "aaa"], key=lambda x: (len(x), x))
# ['aa', 'ab', 'ba', 'aaa']
sorted(collections.Counter("abbccc").most_common(), key=lambda x: (-x[1], x))
# [('c', 3), ('b', 2), ('a', 1)]
list_b = [28, 14, '28', 5, '9', '1']
sorted(list_b, key=int)
# ['1', 5, '9', 14, 28, '28']
sorted(list_b, key=str)
# ['1', 14, 28, '28', 5, '9']
sorted(range(-5, 6), key=lambda x: x**2)
# [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]
arr = [*"Sorting1234"]
sorted(arr, key=lambda c: (c.isdigit(), c in '02468', c.isupper(), c))
# ['g', 'i', 'n', 'o', 'r', 't', 'S', '1', '3', '2', '4']
sorted((int(c.isdigit()), int(c in '02468'), int(c.isupper()), c) for c in arr)
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

[*enumerate('abc')]
# [(0, 'a'), (1, 'b'), (2, 'c')]
[*enumerate('abc', 1)]
# [(1, 'a'), (2, 'b'), (3, 'c')]
[*enumerate('abcde')]
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]
[*enumerate('albatroz', 1)]
# [(1, 'a'), (2, 'l'), (3, 'b'), (4, 'a'), (5, 't'), (6, 'r'), (7, 'o'), (8, 'z')]

# create a concatenated string from 0 to 19 (e.g. "012..1819")
"".join(map(str, range(20)))
# '012345678910111213141516171819'
[*map(lambda a, b: (a, b), range(11), [2, 4, 8])]
# [(0, 2), (1, 4), (2, 8)]
[*map(lambda x: x**2, range(10))]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
l1, l2 = [(1, 1), (2, 2), (3, 3)], [(4, 4), (5, 5), (6, 6)]
[[*map(sum, zip(*t))] for t in zip(l1, l2)]
# [[5, 5], [7, 7], [9, 9]]
{*map(str.upper, {'a', 'b'})}
# {'A', 'B'}
[*map(collections.Counter, itertools.combinations_with_replacement('ABC', 2))]
# [Counter({'A': 2}),
#  Counter({'A': 1, 'B': 1}),
#  Counter({'A': 1, 'C': 1}),
#  Counter({'B': 2}),
#  Counter({'B': 1, 'C': 1}),
#  Counter({'C': 2})]
A, B = [1, 2, 3, 4], [2, 3, 5, 7]
[*map(operator.add, A, B)]  # == [A[i] + B[i] for i in range(len(A))]
# [3, 5, 8, 11]
[*map(''.join, itertools.permutations('abc'))]
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

arr = [(1, 'a'), (3, 'c'), (4, 'e'), (-1, 'z')]
max(arr)
# (4, 'e')
max(arr, key=lambda x: x[1])
# (-1, 'z')
min(arr, key=lambda x: x[1])
# (1, 'a')

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

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
functools.reduce(operator.add, L)  # == sum(L)
# 55
U, V = [1, 2, 3], [2, 3, 5]
functools.reduce(operator.add, map(operator.mul, U, V))  # == sum(map(operator.mul, U, V))
# 23
functools.reduce(operator.iconcat, [[1], [2], [3]], [])
# [1, 2, 3]
functools.reduce(operator.mul, range(1, 11))  # == math.factorial(10)
# 3628800
functools.reduce(operator.add, [1, 2, 3])
# 6
functools.reduce(pow, [3, 2, 2])  # == 3**(2**2)
# 81
functools.reduce(operator.mul, ((3 << 1) + 3 for _ in range(1, 101)))  # == 3**200
# 265613988875874769338781322035779626829233452653394495974574961739092490901302182994384699044001

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
for part in zip(*(iter(s),) * 3):
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

any((False, False, True))
# True
any(i % 3 for i in [3, 3, 4, 4, 3])
# True
a, g = (i for i in (1, 1, 0, 1, 1)), (i for i in range(5))
any(map(lambda x: next(a) == 0, g)), [*a], [*g]
# (True, [1, 1], [3, 4])
any(i in [3, 4] for i in [1, 2, 3])  # Matching partial list
# True

all((True, True, False))
# False
all(x == round((x**3)**(1 / 3)) for x in range(5))
# True
all({x**3: x == round((x**3)**(1 / 3)) for x in range(5)}.values())
# True

# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    print('passed')
if 1 in (x, y, z):
    print('passed')
if x or y or z:
    print('passed')
if any((x, y, z)):
    print('passed')
# if x and y and z:
#     print('passed')
if all((x, y, z)):
    print('passed')


def make_closure(x):
    """
    >>> make_closure(2)()
    2
    4
    """
    def closure():
        nonlocal x
        print(x)
        x *= 2
        print(x)

    return closure


def get_multiplier(a):
    """
    >>> multiply_by_3 = get_multiplier(3)
    >>> multiply_by_3(10)
    30
    """
    def out(b):
        return a * b

    return out


def dot_product_(vec1, vec2, sum=sum, map=map, mul=operator.mul):
    """
    Note, many of the above recipes can be optimized by replacing global lookups
    with local variables defined as default values. For example,
    the dotproduct recipe can be written as:
    """
    return sum(map(mul, vec1, vec2))


def vowel(char):
    """
    >>> [*filter(vowel, 'Aardvark')]
    ['A', 'a', 'a']
    """
    return char.lower() in "aeiou"


def stringify_list(num_list):
    return [*map(str, num_list)]


def maximum_sum(list_of_lists):
    """
    >>> list_of_lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
    >>> maximum_sum(list_of_lists)
    33
    """
    # return max(sum(l) for l in list_of_lists)
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

    """
    # first_true([a,b,c], x) --> a or b or c or x
    # first_true([a,b], x, f) --> a if f(a) else b if f(b) else x
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


def greeter(person, greeting):
    """
    >>> hier = functools.partial(greeter, greeting='Hi')
    >>> hier("man")
    'Hi, man!'
    """
    return f"{greeting}, {person}!"


def file_processing(file_name, processing):
    with open(f"{file_name}") as f:
        for line in iter(f.readline, ''):
            processing(line)


def seek_next_line(f):
    for _ in iter(lambda: f.read(1), '\n'):
        pass


def tail(n, iterable):
    """Return an iterator over the last n items"""
    # tail(3, 'ABCDEFG') --> E F G
    return iter(collections.deque(iterable, maxlen=n))


def zip_(*iterables):
    """
    >>> [*zip_([1, 3, 5], [2, 4, 6])]
    [(1, 2), (3, 4), (5, 6)]
    >>> [*zip([1, 3, 5], [2, 4, 6])] == [*zip_([1, 3, 5], [2, 4, 6])]
    True
    """
    return map(lambda *args: tuple(args), *iterables)
