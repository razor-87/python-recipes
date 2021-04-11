# -*- coding: utf-8 -*-
from itertools import (
    accumulate,
    chain,
    combinations,
    combinations_with_replacement,
    compress,
    count,
    cycle,
    dropwhile,
    filterfalse,
    groupby,
    islice,
    permutations,
    product,
    repeat,
    starmap,
    takewhile,
    tee,
    zip_longest
)
from operator import add, mul

# accumulate
sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
[*accumulate(sample)]
# [5, 9, 11, 19, 26, 32, 35, 35, 44, 45]
[*accumulate(sample, min)]
# [5, 4, 2, 2, 2, 2, 2, 0, 0, 0]
[*accumulate(sample, max)]
# [5, 5, 5, 8, 8, 8, 8, 8, 9, 9]
[*accumulate([1, 4, 3, 5], max)]
# [1, 4, 4, 5]
[*accumulate([1, -1, -1, -1, 1, -1, 1, 1], add)]
# [1, 0, -1, -2, -1, -2, -1, 0]
[*accumulate(range(8))]
# [0, 1, 3, 6, 10, 15, 21, 28]
[*accumulate(sample, mul)]
# [5, 20, 40, 320, 2240, 13440, 40320, 0, 0, 0]
[*accumulate(range(1, 11), mul)]  # list of factorials
# [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

# chain
[*chain.from_iterable((range(1, 4), range(4, 7), range(7, 10)))]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
[*chain('ABC', range(2))]
# ['A', 'B', 'C', 0, 1]
[*chain(enumerate('ABC'))]
# [(0, 'A'), (1, 'B'), (2, 'C')]
[*chain.from_iterable(enumerate('ABC'))]
# [0, 'A', 1, 'B', 2, 'C']

# filterfalse, compress, dropwhile, takewhile
vowel, s = lambda char: char.lower() in "aeiou", "Aardvark"
[*filterfalse(vowel, s)]
# ['r', 'd', 'v', 'r', 'k']
[*compress(s, (1, 0, 1, 1, 0, 1))]
# ['A', 'r', 'd', 'a']
[*dropwhile(vowel, s)]
# ['r', 'd', 'v', 'a', 'r', 'k']
[*takewhile(vowel, s)]
# ['A', 'a']
[*takewhile(lambda x: x % 2 == 0, [2, 4, 9, 8])]
# [2, 4]

# count
[*zip(count(), 'abc')]
# [(0, 'a'), (1, 'b'), (2, 'c')]
[*islice(count(1, .3), 3)]
# [1, 1.3, 1.6]
for i, c in zip(count(1, 3), ['a', 'b', 'c']):
    print(f'{i}: {c}')
# 1: a
# 4: b
# 7: c
g = map(str, count())
next(g), next(g), next(g)
# ('0', '1', '2')

# cycle
cy = cycle('ABC')
next(cy)
# 'A'
[*islice(cy, 7)]
# ['B', 'C', 'A', 'B', 'C', 'A', 'B']
g = (f(range(10)) for f in cycle((min, max)))
next(g), next(g), next(g)
# (0, 9, 0)

# repeat
rp = repeat(7)
next(rp), next(rp)
# (7, 7)
[*repeat(8, 4)]
# [8, 8, 8, 8]
[*map(mul, range(11), repeat(5))]
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# islice
[*islice(s, 4)]
# ['A', 'a', 'r', 'd']
[*islice(s, 4, 7)]
# ['v', 'a', 'r']
[*islice(s, 1, 7, 2)]
# ['a', 'd', 'a']

# groupby
for char, group in groupby('AaaBbC', key=str.upper):
    print(f"{char} -> {[*group]}")
# A -> ['A', 'a', 'a']
# B -> ['B', 'b']
# C -> ['C']
animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear', 'bat', 'dolphin', 'shark']
for length, group in groupby(sorted(animals, key=len), len):
    print(f"{length} -> {[*group]}")
# 3 -> ['rat', 'bat']
# 4 -> ['duck', 'bear']
# 5 -> ['eagle', 'shark']
# 7 -> ['giraffe', 'dolphin']

# starmap
# [*map(pow, [(2, 5), (3, 2), (10, 3)]))
# -> TypeError: pow expected at least 2 arguments, got 1
[*starmap(pow, [(2, 5), (3, 2), (10, 3)])]
# [32, 9, 1000]
[*starmap(mul, enumerate('albatroz', 1))]
# ['a', 'll', 'bbb', 'aaaa', 'ttttt', 'rrrrrr', 'ooooooo', 'zzzzzzzz']
[*starmap(lambda a, b: b / a, enumerate(accumulate(sample), 1))]
# [5.0, 4.5, 3.6666666666666665, 4.75, 5.2, 5.333333333333333,
# 5.0, 4.375, 4.888888888888889, 4.5]

# tee
[*tee('ABC')]
# [<_tee at 0x521f208>, <_tee at 0x521f3c8>]
g1, g2 = tee('ABC')
next(g1), next(g2), next(g2)
# ('A', 'A', 'B')
[*g1], [*g2]
# (['B', 'C'], ['C'])
[*zip(*tee('ABC'))]
# [('A', 'A'), ('B', 'B'), ('C', 'C')]
[*map(mul, *tee(range(11)))]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# zip_longest
[*zip_longest('ABC', range(5))]
# [('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]
[*zip_longest('ABC', range(5), fillvalue='?')]
# [('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]
[*zip_longest('ABCD', 'xy', fillvalue='-')]
# [('A', 'x'), ('B', 'y'), ('C', '-'), ('D', '-')]

# product
[*product('ABC', range(2))]
# [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]
suits = 'spades hearts diamonds clubs'.split()
[*product('AK', suits)]
# [('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'),
# ('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]
[*product('ABC')]
# [('A',), ('B',), ('C',)]
[*product('ABC', repeat=2)]
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'),
# ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]
[*product(range(2), repeat=3)]
# [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0),
# (1, 0, 1), (1, 1, 0), (1, 1, 1)]
[*product('AB', range(2), repeat=2)]
# [('A', 0, 'A', 0),
#  ('A', 0, 'A', 1),
#  ('A', 0, 'B', 0),
#  ('A', 0, 'B', 1),
#  ('A', 1, 'A', 0),
#  ('A', 1, 'A', 1),
#  ('A', 1, 'B', 0),
#  ('A', 1, 'B', 1),
#  ('B', 0, 'A', 0),
#  ('B', 0, 'A', 1),
#  ('B', 0, 'B', 0),
#  ('B', 0, 'B', 1),
#  ('B', 1, 'A', 0),
#  ('B', 1, 'A', 1),
#  ('B', 1, 'B', 0),
#  ('B', 1, 'B', 1)]

# permutations
[*permutations([1, 2, 3])]
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
[*permutations('ABC', 2)]
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
[*permutations('ABC')]
# [('A', 'B', 'C'),
#  ('A', 'C', 'B'),
#  ('B', 'A', 'C'),
#  ('B', 'C', 'A'),
#  ('C', 'A', 'B'),
#  ('C', 'B', 'A')]

# combinations
[*combinations([1, 2, 3], 2)]
# [(1, 2), (1, 3), (2, 3)]
[*combinations('ABC', 2)]
# [('A', 'B'), ('A', 'C'), ('B', 'C')]
[*combinations_with_replacement('ABC', 2)]
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]
(*combinations_with_replacement('ABC', 2), )
# (('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C'))
