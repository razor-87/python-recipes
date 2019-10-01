# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-09-29 19:47:20
# @Last Modified by:   razor87
# @Last Modified time: 2019-10-01 21:49:44

kilometer = [39.2, 36.5, 37.3, 37.8]
feet = map(lambda x: float(3280.8399) * x, kilometer)
feet = [float(3280.8399) * x for x in kilometer]
# [128608.92408000001, 119750.65635, 122375.32826999998, 124015.74822]
reduced_feet = sum([x for x in feet])
# 494748
uneven = [x / 2 for x in feet if x % 2 == 0]
# [64304.0, 59875.0]
divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]
# [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
[x + 1 if x >= 120000 else x + 5 for x in feet]
# [128609, 119755, 122376, 124016]

list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8]]
[y for x in list_of_list for y in x]
# [1, 2, 3, 4, 5, 6, 7, 8]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[row[i] for row in matrix] for i in range(3)]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

matrix = [[0 for col in range(4)] for row in range(3)]
# [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

[[int(x) for x in feet] for x in feet]
# [[128608, 119750, 122375, 124015],
#  [128608, 119750, 122375, 124015],
#  [128608, 119750, 122375, 124015],
#  [128608, 119750, 122375, 124015]]

squares = [value**2 for value in range(1, 11)]  # list comprehensions
x_labels = [str(num) for num in range(1, 7)]
even_list = [num for num in range(10) if num % 2 == 0]
square_map = {number: number**2 for number in range(5)}
reminders_set = {num % 10 for num in range(100)}

values = [expression for value in collection if condition]
squares = [x * x for x in range(10)]
even_squares = [x * x for x in range(10) if x % 2 == 0]

subjects = {subject: teacher for teacher, subject in teachers.items()}

{f: i for i, f in enumerate(input)}
# {'Duration': 0, 'F0': 1, 'F1': 2, 'F2': 3, 'F3': 4}

{x * x for x in range(-9, 10)}
# {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
{x: x * x for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

[[0] * m for m in range(n)]
[[0 for j in range(m)] for i in range(n)]
[[i * j for j in range(m)] for i in range(n)]
{i: [] for i in range(n)}

[[0] * 3 for _ in range(3)]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0 for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[[0] * 2] * 2 for _ in range(2)]
# [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
[[i * j for j in range(4)] for i in range(4)]
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]]
[[((j**i) // (j * i)) for j in range(1, 5)] for i in range(1, 5)]
# [[1, 1, 1, 1], [0, 1, 1, 2], [0, 1, 3, 5], [0, 2, 6, 16]]
{i: [i**2] for i in range(5)}
# {0: [0], 1: [1], 2: [4], 3: [9], 4: [16]}
{i: tuple(j**i for j in range(1, 5)) for i in range(1, 5)}
# {1: (1, 2, 3, 4), 2: (1, 4, 9, 16), 3: (1, 8, 27, 64), 4: (1, 16, 81, 256)}

{i: None for i in range(6)}
# {0: None, 1: None, 2: None, 3: None, 4: None, 5: None}

[[binomial(n, i) for i in range(n + 1)] for n in range(10)]

S = [x**2 for x in range(10)]
V = [2**i for i in range(13)]
M = [x for x in S if x % 0 == 0]

new_list = [n**2 for n in numbers if n % 2 == 0]

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

type(number**2 for number in range(5))  # generator

# Python's list comprehensions are awesome.
vals = [expression for value in collection if condition]
# This is equivalent to:
vals = []
for value in collection:
    if condition:
        vals.append(expression)

# Example:
even_squares = [x * x for x in range(10) if not x % 2]
even_squares
# [0, 4, 16, 36, 64]

squares = list(map(lambda x: x**2, range(10)))
squares = [x**2 for x in range(10)]
[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

vec = [-4, -2, 0, 2, 4]
[x * 2 for x in vec]
# [-8, -4, 0, 4, 8]
[x for x in vec if x >= 0]
# [0, 2, 4]
[abs(x) for x in vec]
# [4, 2, 0, 2, 4]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
# ['banana', 'loganberry', 'passion fruit']

[(x, x**2) for x in range(6)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[num for elem in vec for num in elem]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

[x for x in arr if x > 0]
[
    ' '.join(map(str, lst))
    for lst in [d[i] if i in d else [-1] for i in arr[n + 1:]]
]
