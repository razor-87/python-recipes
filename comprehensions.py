# -*- coding: utf-8 -*-

[[0] * 3 for _ in range(3)]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0 for j in range(3)] for i in range(3)]
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[[0] * 2] * 2 for _ in range(2)]
# [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
[[0] * m for m in range(5)]
# [[], [0], [0, 0], [0, 0, 0], [0, 0, 0, 0]]
[[i * j for j in range(4)] for i in range(4)]
# [[0, 0, 0, 0], [0, 1, 2, 3], [0, 2, 4, 6], [0, 3, 6, 9]]
[[((j**i) // (j * i)) for j in range(1, 5)] for i in range(1, 5)]
# [[1, 1, 1, 1], [0, 1, 1, 2], [0, 1, 3, 5], [0, 2, 6, 16]]
[[i * j for j in range(3)] for i in range(5)]
# [[0, 0, 0], [0, 1, 2], [0, 2, 4], [0, 3, 6], [0, 4, 8]]
[x**2 for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[(x, x**2) for x in range(6)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
[x**2 for x in range(10) if not x & 1]  # if x % 2 == 0
# [0, 4, 16, 36, 64]
[2**i for i in range(13)]
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[y for x in lists for y in x]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
[[row[i] for row in lists] for i in range(3)]
# [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
[(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
[x for x in range(100) if x % 3 == 0 and x % 5 == 0]
# [0, 15, 30, 45, 60, 75, 90]
[abs(x) for x in [-4, -2, 0, 2, 4]]
# [4, 2, 0, 2, 4]
[str(num) for num in range(1, 7)]
# ['1', '2', '3', '4', '5', '6']
[char for char in ['d', '1', 'f', '5'] if char.isdigit()]
# ['1', '5']
[fruit.strip() for fruit in ['  banana', '  loganberry ', 'passion fruit  ']]
# ['banana', 'loganberry', 'passion fruit']
[s for s in ['fsd', 'gf', '  ', 'dsf', ' '] if s.strip()]
# ['fsd', 'gf', 'dsf']
n, arr = 2, range(10)
[{*arr[i:i+n]} for i in arr[::n]]  # cut on sets
# [{0, 1}, {2, 3}, {4, 5}, {6, 7}, {8, 9}]

(*(x for x in range(21) if not x & 1),)  # if x % 2 == 0
# (0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
(*(x for x in range(21) if x & 1),)  # if x % 2 != 0
# (1, 3, 5, 7, 9, 11, 13, 15, 17, 19)

{x * x for x in range(-9, 10)}
# {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
{num % 10 for num in range(100)}
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

{x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
{i: [i**2] for i in range(5)}
# {0: [0], 1: [1], 2: [4], 3: [9], 4: [16]}
{i: (*(j**i for j in range(1, 5)),) for i in range(1, 5)}
# {1: (1, 2, 3, 4), 2: (1, 4, 9, 16), 3: (1, 8, 27, 64), 4: (1, 16, 81, 256)}
{x**3: x == round((x**3)**(1/3)) for x in range(5)}
# {0: True, 1: True, 8: True, 27: True, 64: True}
{str(i): i for i in range(5)}
# {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}
{i: [] for i in range(5)}
# {0: [], 1: [], 2: [], 3: [], 4: []}
{i: None for i in range(6)}
# {0: None, 1: None, 2: None, 3: None, 4: None, 5: None}
{f: i for i, f in enumerate(['Duration', 'F0', 'F1', 'F2', 'F3'])}
# {'Duration': 0, 'F0': 1, 'F1': 2, 'F2': 3, 'F3': 4}
{value: key for key, value in {'key': 'value'}.items()}
# {'value': 'key'}
