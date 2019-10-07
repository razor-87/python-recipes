# -*- coding: utf-8 -*-
import io
import sys


sys.stdin
sys.stdin.read()
sys.stdin.readline()
sys.stdin.readlines()



sys.stdin = io.StringIO("1\n2\n3\n4\n5\n6\n7\n8\n9")




f = open('data.txt')
first, second, *rest, last = f.readlines()
f.close()



lines = list(map(str.strip, sys.stdin.readlines()))

a = []
a = list(map(int, input().split()))
print(' '.join(map(str, a)))
print(*a)

a, b = map(int, input().split())
a, b = sys.stdin.read().split()

reader = (int(line.strip()) for line in sys.stdin.readlines())
N = next(reader)

input_list = next(sys.stdin).split()



ls = [[*map(int, i.split())] for i in sys.stdin]
(n, e, d), ps, res = ls[0], [*range(ls[0][0] + 1)], 1


_, arr = (tuple(map(int, lst))
          for lst in map(str.split, map(str.strip, sys.stdin.readlines())))
_, arr = sys.stdin.readline(), tuple(sys.stdin.readline().split())




inp = input().split()
name, price = ' '.join(inp[:-1]), int(inp[-1])



arr = tuple(
    tuple(map(float, lst))
    for lst in map(str.split, map(str.strip, sys.stdin.readlines()[1:])))


[tuple(map(int, el.split())) for el in map(str.strip, sys.stdin.readlines()[1:])]


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

(*map(int, input().split()),)
# 45 66 34 -> (45, 66, 34)

({*map(int, input().split())} for _ in range(2))


with open('input00.txt') as f:
    _, arr = f.readline(), tuple(f.readline().split())

with open("input07.txt") as f:
    _, n, m = (f.readline(), map(int, f.readline().split()),
               ({*map(int, f.readline().split())} for _ in range(2)))


with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)





with open(file) as f:
    file.write()
    file.tell()
    file.read()
    file.seek(0)
    file.readline()
    file.readlines()

file.writelines()



with open("/path/to/file") as f:
    for line in f:
        print(line)

f = open("/path/tofile", 'w')
for e in aList:
    f.write(e + "\n")
f.close()



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
