# -*- coding: utf-8 -*-
import sys
import io


sys.stdin
sys.stdin.read()
sys.stdin.readline()
sys.stdin.readlines()
sys.stdin = io.StringIO("1\n2\n3\n4\n5\n6\n7\n8\n9")



lines = list(map(str.strip, f_in.readlines()))

a = []
a = list(map(int, input().split()))
print(' '.join(map(str, a)))
print(*a)

a, b = map(int, input().split())
a, b = sys.stdin.read().split()

reader = (line.strip() for line in sys.stdin.readlines())
N = int(next(reader))

input_list = next(sys.stdin).split()



ls = [[*map(int, i.split())] for i in sys.stdin]
(n, e, d), ps, res = ls[0], [*range(ls[0][0] + 1)], 1



_, arr = (tuple(map(int, lst))
          for lst in map(str.split, map(str.strip, sys.stdin.readlines())))
_, arr = sys.stdin.readline(), tuple(sys.stdin.readline().split())

with open('input00.txt') as f:
    _, arr = f.readline(), tuple(f.readline().split())



inp = input().split()
name, price = ' '.join(inp[:-1]), int(inp[-1])



arr = tuple(
    tuple(map(float, lst))
    for lst in map(str.split, map(str.strip, sys.stdin.readlines()[1:])))


arr = np.array([tuple(map(int, el.split())) for el in map(str.strip, sys.stdin.readlines()[1:])], int)


*n, m = (tuple(map(float, row.strip().split())) for row in sys.stdin.readlines())
print(np.polyval(*n, *m))


a, b = (tuple(map(int, row.strip().split())) for row in sys.stdin.readlines())


_, *arr = map(int, sys.stdin.read().split())
# -> List[int]


arr = tuple(input() for _ in range(int(input())))
# 3
# 1 0
# 2 $ -> ('1 0', '2 $', '3 1')
# 3 1


x, y = (int(input()) for _ in range(2))

(x, y), ex = map(int, input().split()), input()


a, b = (tuple(map(int, input().split())) for _ in range(2))

p, x = [*map(float, input().split())], int(input())

n, _ = map(int, input().split())

lst = [input().split() for _ in range(n)]

lst = [input().split() for _ in range((*map(int, input().split()),)[0])]

shapes = (*map(int, input().split()),)




def f_open(filename='input.txt', mock=False):
    try:
        with open(filename) as f:
            inp = f
    except FileNotFoundError:
        import sys
        if mock:
            import io
            sys.stdin = io.StringIO(mock)
        inp = sys.stdin
    return inp


fake = '2\nA\nB : A\n1\nC C'
print(f_open(mock=fake).read())
