# -*- coding: utf-8 -*-
import functools
import operator


prints = functools.partial(print, end=' ')
prints()
print(functools.reduce(lambda x, y: x + y, [1, 2, 3]))


somelist = [(1, 5, 8), (6, 2, 4), (9, 7, 5)]
somelist.sort(key=operator.itemgetter(0))
somelist
# [(1, 5, 8), (6, 2, 4), (9, 7, 5)]

somelist.sort(key=operator.itemgetter(1))
somelist
# [(6, 2, 4), (1, 5, 8), (9, 7, 5)]

somelist.sort(key=operator.itemgetter(2))
somelist
# [(6, 2, 4), (9, 7, 5), (1, 5, 8)]

list_a = [(0, 1), (0, 1), (0, 1)]
# import operator
items = sorted(list_a, key=operator.itemgetter(1), reverse=True)

operatot.itemgetter(-1)
operatot.attrgetter('sort')

operator.xor


functools.reduce(operator.mul, range(1, 11))  # math.factorial(10)
# 3628800


# The lambda keyword in Python provides a
# shortcut for declaring small and
# anonymous functions:
add = lambda x, y: x + y
add(5, 3)
8

# So what's the big fuss about?
# Lambdas are *function expressions*:
(lambda x, y: x + y)(5, 3)
8


sorted(range(-5, 6), key=lambda x: x ** 2)
# [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]

list(filter(lambda x: x % 2 == 0, range(16)))
# [0, 2, 4, 6, 8, 10, 12, 14]

list(map(lambda x: x**2, range(10)))
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

(lambda x: x**2)(2)

(lambda x, y: x + y)(5, 3)
sorted(range(-5, 6), key=lambda x: x ** 2)


# squarity
list(map(lambda a: a**2, range(5)))

# is_positive
list(filter(lambda a: a > 0, range(-2, 3)))


# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = map(str, range(20))
print("".join(nums))


(func1 if y == 1 else func2)(arg1, arg2)
(class1 if y == 1 else class2)(arg1, arg2)


mod_checker = lambda x, mod=0: lambda y: True if y % x == mod else False


reversed(list)
(0, 1, 2, 3) == tuple(reversed([3, 2, 1, 0]))
# True

half_size = len(numbers) // 2
median = sum(numbers[half_size - 1:half_size + 1]) / 2



for i, item in enumerate(iterable):
    print(i, item)

list(enumerate('abc'))
# [(0, 'a'), (1, 'b'), (2, 'c')]
list(enumerate('abc', 1))
# [(1, 'a'), (2, 'b'), (3, 'c')]


targetList = filter(lambda x: len(x) > 0, targetList)



list_b = [28, 14, '28', 5, '9', '1']
sorted(list_b, key=int)
sorted(list_b, key=str)

# sort by len
lst_sort = sorted(lst, reverse=True, key=len)

# Sort 2D array using 2nd column
sorted(movie_year, key=lambda row: row[1], reverse=True)



print(min([i for i in nums if i % 2 != 0]))

enumerate(list)
print(*enumerate('abcde'))


reduce(lambda x, y: x*(y**5), map(int, input().split()), 1)
print(*map(lambda x, y: x ^ y,
           map(int, input().split()), map(int, input().split())))


all({x**3: x == round((x**3)**(1/3)) for x in range(21)}.values())
all(x == round((x**3)**(1/3)) for x in range(21))

max([min(map(int, tuple(s.split()))) for s in input_])

x = [1, 5, 2, 3]
y = list(map(lambda x: x**2, x))
print(*y)

print(min([i for i in map(int, input().split()) if i % 2 != 0]))
print(min(filter(lambda x: x % 2 != 0, map(int, input().split()))))
print(min(map(int, input().split()), key=lambda x: (not x % 2, x)))


list(filter(bool, range(3)))  # <-> [x for x in range(3) if x]


num_list = range(7)
squared_list = [x ** 2 for x in num_list]
list(zip(num_list, squared_list))
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]


any([i % 3 for i in [3, 3, 4, 4, 3]])
# True

# Matching partial list
any(i in files_batch_val for i in yileded_list)

any(True, False, False)
all(True, True, True)

any(map(lambda x: int(input()) == 0, range(int(input()))))


my_list = [[1, 2, 3], [40, 50, 60], [9, 8, 7]]
sum(sub[1] for sub in my_list)
# 60

sum(1 for i in [3, 3, 4, 4, 3] if i == 4)
# 2

sum(nums[i]**nums[i+1] for i in range(len(nums))[::2])

sum(text.encode('utf-8'))

sum(sub == 'CDC' for sub in ("ABCDCDC"[i:i+len('CDC')] for i in range(len("ABCDCDC"))))
# 2
sum(sub_string == pattern for sub_string in (string[i:i + len(pattern)] for i in range(n)))


sum((i in a) - (i in b) for i in n)
sum(bool({i} & a) - bool({i} & b) for i in n)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
[[row[i] for row in matrix] for i in range(4)]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
list(zip(*matrix))
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]

list(zip(*zip(eng, ger)))
# [('one', 'two', 'three'), ('eins', 'zwei', 'drei')]

map(lambda i: map(lambda x, y: x + y, matr_a[i], matr_b[i]), range(len(matr_a)))
map(add, c[i], d[i]) for i in range(len(c))
[map(sum, zip(*t)) for t in zip(X, Y)]

list(map(list, zip(*matrix.lists)))


A = [1, 2, 3, 4]
B = [2, 3, 5, 7]
[A[i] + B[i] for i in range(len(A))]
# [3, 5, 8, 11]
from operator import add
list(map(add, A, B))
# [3, 5, 8, 11]

from operator import add
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reduce(add, L)
# 55
sum(L)
# 55

from operator import add
from operator import mul
U = [1, 2, 3]
V = [2, 3, 5]
reduce(add, map(mul, U, V))
# 23
sum(map(mul, U, V))
# 23

[k for k in range(1, 21) if gcd(k, 20) == 1]
# [1, 3, 7, 9, 11, 13, 17, 19]
is_coprime = lambda k: gcd(k, 20) == 1
list(filter(is_coprime, range(1, 21)))
# [1, 3, 7, 9, 11, 13, 17, 19]


(int)(num) == int(num)




s = 'abcdefghi'
[*zip(s, s, s)]
# [('a', 'a', 'a'), ('b', 'b', 'b'), ('c', 'c', 'c'),
#  ('d', 'd', 'd'), ('e', 'e', 'e'), ('f', 'f', 'f'),
#  ('g', 'g', 'g'), ('h', 'h', 'h'), ('i', 'i', 'i')]
i = iter(s)
[*zip(i, i, i)]
# [('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i')]
(*zip(*(iter('abcdefghi'),)*3),)
# (('a', 'b', 'c'), ('d', 'e', 'f'), ('g', 'h', 'i'))
for part in zip(*(iter('abcdefghi'),)*3):
    print(part)
# ('a', 'b', 'c')
# ('d', 'e', 'f')
# ('g', 'h', 'i')



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





# How to sort a Python dict by value
# (== get a representation sorted by value)
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
# Or:
sorted(xs.items(), key=operator.itemgetter(1))
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]



functools.reduce(lambda x, y: y**x, reversed(arr))
# (3, 2, 2) -> 3**(2**2) -> 81
