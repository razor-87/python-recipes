# -*- coding: utf-8 -*-
import collections
import itertools
import operator

[*itertools.chain.from_iterable([[1, 2, 3], [4, 5, 6], [7, 8, 9]])]
[*itertools.chain.from_iterable((range(1, 4), range(4, 7), range(7, 10)))]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

s = "Aardvark"
vowel = lambda char: char.lower() in "aeiou"
[*itertools.filterfalse(vowel, s)]
# ['r', 'd', 'v', 'r', 'k']
[*itertools.compress(s, (1, 0, 1, 1, 0, 1))]
# ['A', 'r', 'd', 'a']
[*itertools.dropwhile(vowel, s)]
# ['r', 'd', 'v', 'a', 'r', 'k']
[*itertools.takewhile(vowel, s)]
# ['A', 'a']
[*itertools.takewhile(lambda x: x <= 6, [0, 1, 3, 6, 10, 15, 21, 28])]
# [0, 1, 3, 6]
[*itertools.takewhile(lambda x: x % 2 == 0, [2, 4, 6, 7, 9, 8])]
# [2, 4, 6]

[*itertools.islice(s, 4)]
# ['A', 'a', 'r', 'd']
[*itertools.islice(s, 4, 7)]
# ['v', 'a', 'r']
[*itertools.islice(s, 1, 7, 2)]
# ['a', 'd', 'a']

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
[*itertools.accumulate(sample)]
# [5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
[*itertools.accumulate(sample, min)]
# [5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
[*itertools.accumulate(sample, max)]
# [5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
[*itertools.accumulate([1, 4, 3, 5], max)]
# [1, 4, 4, 5]
[*itertools.accumulate([1, -1, -1, -1, 1, -1, 1, 1], operator.add)]
# [1, 0, -1, -2, -1, -2, -1, 0]
[*itertools.accumulate(range(8))]
# [0, 1, 3, 6, 10, 15, 21, 28]
[*itertools.accumulate(sample, operator.mul)]
# [5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]
[*itertools.accumulate(range(1, 11), operator.mul)]  # list of factorials
# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
[*map(operator.mul, range(11), range(11))]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[*map(operator.mul, range(11), [2, 4, 8])]
# [0, 4, 16]

# [*map(pow, [(2, 5), (3, 2), (10, 3)]))
# -> TypeError: pow expected at least 2 arguments, got 1
[*itertools.starmap(pow, [(2, 5), (3, 2), (10, 3)])]
# [32, 9, 1000]
[*itertools.starmap(operator.mul, enumerate('albatroz', 1))]
# ['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']
[*itertools.starmap(lambda a, b: b / a,
                    enumerate(itertools.accumulate(sample), 1))]
# [5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333,
# 5.0, 4.375, 4.888888888888889, 4.5]

[*itertools.chain('ABC', range(2))]
# ['A', 'B', 'C', 0, 1]
[*itertools.chain(enumerate('ABC'))]
# [(0, 'A'), (1, 'B'), (2, 'C')]
[*itertools.chain.from_iterable(enumerate('ABC'))]
# [0, 'A', 1, 'B', 2, 'C']
for c in itertools.chain(range(3), range(12, 15)):
    print(c)
# 0
# 1
# 2
# 12
# 13
# 14

[*itertools.zip_longest('ABC', range(5))]
# [('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
[*itertools.zip_longest('ABC', range(5), fillvalue='?')]
# [('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]
[*itertools.zip_longest('ABCD', 'xy', fillvalue='-')]
# [('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-')]

[*itertools.product('ABC', range(2))]
# [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
suits = 'spades hearts diamonds clubs'.split()
[*itertools.product('AK', suits)]
# [('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'),
# ('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]
[*itertools.product('ABC')]
# [('A',), ('B',), ('C',)]
[*itertools.product('ABC', repeat=2)]
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'),
# ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
[*itertools.product(range(2), repeat=3)]
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

for i in itertools.count(3):
    print(i)
    if i >= 6:
        break
# 3
# 4
# 5
# 6
[*itertools.islice(itertools.count(1, .3), 3)]
# [1, 1.3, 1.6]
ct = itertools.count()
next(ct)
# 0
next(ct), next(ct), next(ct)
# (1, 2, 3)

cy = itertools.cycle('ABC')
next(cy)
# 'A'
[*itertools.islice(cy, 7)]
# ['B', 'C', 'A', 'B', 'C', 'A', 'B']

rp = itertools.repeat(7)
next(rp), next(rp)
# (7, 7)
[*itertools.repeat(8, 4)]
# [8, 8, 8, 8]
[*map(operator.mul, range(11), itertools.repeat(5))]
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

[*itertools.permutations([1, 2, 3])]
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
[*itertools.permutations('ABC', 2)]
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
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

[*itertools.combinations([1, 2, 3], 2)]
# [(1, 2), (1, 3), (2, 3)]
[*itertools.combinations('ABC', 2)]
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
[*itertools.combinations_with_replacement('ABC', 2)]
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
(*itertools.combinations_with_replacement('ABC', 2),)
# (('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C'))

[*itertools.groupby('LLLLAAGGG')]
# [('L', <itertools._grouper object at 0x102227cc0>),
# ('A', <itertools._grouper object at 0x102227b38>),
# ('G', <itertools._grouper object at 0x102227b70>)]
for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', [*group])
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
    print(length, '->', [*group])
# 3 -> ['rat', 'bat']
# 4 -> ['duck', 'bear', 'lion']
# 5 -> ['eagle', 'shark']
# 7 -> ['giraffe', 'dolphin']
for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', [*group])
# 7 -> ['dolphin', 'giraffe']
# 5 -> ['shark', 'eagle']
# 4 -> ['lion', 'bear', 'duck']
# 3 -> ['bat', 'rat']

[*itertools.tee('ABC')]
# [<itertools._tee object at 0x10222abc8>, <itertools._tee object at 0x10222ac08>]
g1, g2 = itertools.tee('ABC')
next(g1)
# 'A'
next(g2)
# 'A'
next(g2)
# 'B'
[*g1]
# ['B', 'C']
[*g2]
# ['C']
[*zip(*itertools.tee('ABC'))]
# [('A', 'A'), ('B', 'B'), ('C', 'C')]
