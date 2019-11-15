# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-10-04 20:17:35
# @Last Modified by:   razor87
# @Last Modified time: 2019-11-15 18:30:22
import collections
import functools
import itertools
import math
import operator


# Math operations: add(), sub(), mul(), floordiv(), abs(), …
# Logical operations: not_(), truth().
# Bitwise operations: and_(), or_(), invert().
# Comparisons: eq(), ne(), lt(), le(), gt(), and ge().
# Object identity: is_(), is_not().
operator.itemgetter(-1)
operator.attrgetter('sort')
operator.xor

somelist = [(1, 5, 8), (6, 2, 4), (9, 7, 5)]
somelist.sort(key=operator.itemgetter(0))
# [(1, 5, 8), (6, 2, 4), (9, 7, 5)]
somelist.sort(key=operator.itemgetter(1))
# [(6, 2, 4), (1, 5, 8), (9, 7, 5)]

list_a = [(0, 1), (0, 1), (0, 1)]
items = sorted(list_a, key=operator.itemgetter(1), reverse=True)

# How to sort a Python dict by value
# (== get a representation sorted by value)
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}
sorted(xs.items(), key=lambda x: x[1])
# Or:
sorted(xs.items(), key=operator.itemgetter(1))
# [('d', 1), ('c', 2), ('b', 3), ('a', 4)]

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]

# sort by len
sorted([[1], [1, 1, 1], [1, 1]], reverse=True, key=len)
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

sorted(range(-5, 6), key=lambda x: x ** 2)
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

(lambda x: x**2)(2)
# 4
(lambda x, y: x + y)(5, 3)
# 8

mod_checker = lambda x, mod=0: lambda y: True if y % x == mod else False

(0, 1, 2, 3) == (*reversed([3, 2, 1, 0]),)
# True

[*enumerate('abc')]
# [(0, 'a'), (1, 'b'), (2, 'c')]
[*enumerate('abc', 1)]
# [(1, 'a'), (2, 'b'), (3, 'c')]
[*enumerate('abcde')]
# [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

# create a concatenated string from 0 to 19 (e.g. "012..1819")
"".join(map(str, range(20)))

[*map(lambda x: x**2, range(10))]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

map(lambda i: map(lambda x, y: x + y, matr_a[i], matr_b[i]), range(len(matr_a)))
(map(operator.add, c[i], d[i]) for i in range(len(c)))
(map(sum, zip(*t)) for t in zip(X, Y))
map(list, zip(*matrix.lists))
{*map(str.upper, {'a', 'b'})}
# {'A', 'B'}

(*map(collections.Counter, itertools.combinations_with_replacement('ABC', 2)),)
# (Counter({'A': 2}),
#  Counter({'A': 1, 'B': 1}),
#  Counter({'A': 1, 'C': 1}),
#  Counter({'B': 2}),
#  Counter({'B': 1, 'C': 1}),
#  Counter({'C': 2}))

A = [1, 2, 3, 4]
B = [2, 3, 5, 7]
[A[i] + B[i] for i in range(len(A))]
# [3, 5, 8, 11]
[*map(operator.add, A, B)]
# [3, 5, 8, 11]

max(min(map(int, tuple(s.split()))) for s in input_)
min(i for i in nums if i % 2 != 0)
min(i for i in map(int, input().split()) if i % 2 != 0)
min(filter(lambda x: x % 2 != 0, map(int, input().split())))
min(map(int, input().split()), key=lambda x: (not x % 2, x))

[*filter(lambda x: x % 2 == 0, range(16))]
# [0, 2, 4, 6, 8, 10, 12, 14]
[*filter(lambda a: a > 0, range(-2, 3))]  # is_positive
# [1, 2]
[*filter(bool, range(3))]  # == [x for x in range(3) if x]
# [1, 2]
[*filter(lambda k: math.gcd(k, 20) == 1, range(1, 21))]
# [1, 3, 7, 9, 11, 13, 17, 19]
(*filter(lambda x: x.isdigit(), ['d', '1', 'f', '5']),)
# ('1', '5')
len((*filter(lambda x: x & 1 == 0, range(1001)),))
# 501

my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
sum(sub[1] for sub in my_list)
# 60
sum(1 for i in [3, 3, 4, 4, 3] if i == 4)
# 2

sum(nums[i]**nums[i+1] for i in range(len(nums))[::2])

sum(text.encode('utf-8'))

sum((i in a) - (i in b) for i in n)
sum(bool({i} & a) - bool({i} & b) for i in n)

sum(x & 1 == 0 for x in range(1001))
# 501

L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
functools.reduce(operator.add, L)
# 55
sum(L)
# 55

U = [1, 2, 3]
V = [2, 3, 5]
functools.reduce(operator.add, map(operator.mul, U, V))
# 23
sum(map(operator.mul, U, V))
# 23

sum([[1], [2], [3]], [])
functools.reduce(operator.iconcat, [[1], [2], [3]], [])
# [1, 2, 3]

functools.reduce(operator.mul, range(1, 11))  # math.factorial(10)
# 3628800

functools.reduce(lambda x, y: x + y, [1, 2, 3])
# 6

functools.reduce(lambda x, y: y**x, reversed(arr))
# (3, 2, 2) -> 3**(2**2) -> 81

functools.reduce(operator.mul, ((3 << 1) + 3 for _ in range(1, 101)))  # 3**200
# 265613988875874769338781322035779626829233452653394495974574961739092490901302182994384699044001

functools.reduce(lambda x, y: x*(y**5), map(int, input().split()), 1)
print(*map(lambda x, y: x ^ y,
           map(int, input().split()), map(int, input().split())))

prints = functools.partial(print, end='end')
prints()
# end

[*zip(range(7), [x ** 2 for x in range(7)])]
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
(*zip(*(iter(s),)*3),)
# (('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i'))
for part in zip(*(iter(s),)*3):
    print(part)
# ('a', 'b', 'c')
# ('d', 'e', 'f')
# ('g', 'h', 'i')

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
all(x == round((x**3)**(1/3)) for x in range(5))
# True
all({x**3: x == round((x**3)**(1/3)) for x in range(5)}.values())
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


# Note, many of the above recipes can be optimized by replacing global lookups
# with local variables defined as default values. For example,
# the dotproduct recipe can be written as:
def dot_product_(vec1, vec2, sum=sum, map=map, mul=operator.mul):
    return sum(map(mul, vec1, vec2))
