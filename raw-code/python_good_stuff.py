# -*- coding: utf-8 -*-
help(5)
# Help on int object:
# (etc etc)

dir(5)
# ['__abs__', '__add__', ...]

abs.__doc__
# 'abs(number) -> number
# Return the absolute value of the argument.

num = 13
num.__add__(2)
dir(num)

func.__code__.co_code

import dis
dis.dis(func)

dis.dis(compile("(10, 'abc')", '', 'eval'))
dis.dis(compile("[10, 'abc']", '', 'eval'))

a = ()
b = ()
a is b
# True
id(a)
# 4409020488
id(b)
# 4409020488

a = []
b = []
a is b
# False
id(a)
# 4465566920
id(b)
# 4465370632

a = (1, 2, 3)
id(a)
# 4427578104
del a
b = (1, 2, 4)
id(b)
# 4427578104

a = []
id(a)
# 4465566792
del a
b = []
id(b)
# 4465566792

dir(sys)
sys.argv
sys.executable
sys.exit
sys.path
sys.platform

import sys
import array
import numpy as np

sys.getrefcount

sys.getsizeof(range(10))
# 48
sys.getsizeof(_ for _ in range(10))
# 88
sys.getsizeof(array.array('i', range(10)))
# 128
sys.getsizeof(tuple(range(10)))
# 128
sys.getsizeof(np.array(range(10), dtype='i'))
# 136
sys.getsizeof(list(range(10)))
# 200
sys.getsizeof({i: None for i in range(10)})
# 368
sys.getsizeof(set(range(10)))
# 736


from pympler import asizeof
asizeof.flatsize  # == sys.getsizeof

asizeof.asizeof(_ for _ in range(10))
# 0
asizeof.asizeof(range(10))
# 48
asizeof.asizeof(array.array('i', range(10)))
# 128
asizeof.asizeof(np.array(range(10), dtype='i'))
# 136
asizeof.asizeof(tuple(range(10)))
# 440
asizeof.asizeof(list(range(10)))
# 512
asizeof.asizeof({i: None for i in range(10)})
# 696
asizeof.asizeof(set(range(10)))
# 1048



















hash(tuple())

class SameHash():
    def __hash__(self):
        return 1

a = SameHash()
b = SameHash()
a == b    # False
hash(a), hash(b)    # (1, 1)

{True: 'yes', 1: 'no', 1.0: 'maybe'}
True == 1 == 1.0    # True
hash(True), hash(1), hash(1.0)    # (1, 1, 1)

print(id(False), id(True))
print(id(1 != 1), id(1 == 1))
print(id(bool()), id(bool(1)))

from copy import deepcopy

x = [[0, 0], [1, 1]]
y = deepcopy(x)
print('x', x, id(x), id(x[0]), id(x[1]))
print('y', y, id(y), id(y[0]), id(y[1]))



a = 1_000_000_000

num = 100_000_000   # Only >=3.6

num = 1.5e2    # == 1.5 * (10 ** 2)

a = 100
b = 200
a, b = b, a

bool(bool)    # True
bool(12)    # True
bool('asdsa')    # True
bool(0)    # False
bool('')    # False




bool(None)    # False
answer = None    # if not answer: (True), if answer is None:



score_1, score_2 = 5, 0
winner = "Argentina" if score_1 > score_2 else "Jamaica"    # Ternary operator


print(', '.join(list))    # str.join()

reversed(list)



a, b, *rest = range(5)

# Since Python 3.5
{**{'a': 1}, 'b': 2, **{'c': 3}}
# {'a': 1, 'b': 2, 'c': 3}
[1, 2, *[3, 4]]
# [1, 2, 3, 4]

x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)
# {'c': 4, 'a': 1, 'b': 3}


xP == hP and text[:m] == P and print(0, end=' ')



a = [(), (), ()]
for el in sorted(a):
    print('%s/%s' % el)


half_size = len(numbers) // 2
median = sum(numbers[half_size - 1:half_size + 1]) / 2

t = (20, 8)
divmod(*t)

divmod(x, y)  # (x // y, x % y)
divmod(177, 10)
# (17, 7)

pow(x, y, m)  # x**y mod m
pow(3, 4, 5)
# 1




operator.xor



dict.get('key', 'not found')
letters[c] = letters.get(c, 0) + 1

dict.update({
    'key': 'value'
})

dict.pop('key')
dict.setdefault('key', 'default')
dict = OrderedDict()    # from collection import OrderedDict

if key in mydict:
    value = mydict[key]
else:
    value = mydict.setdefault(key, getvalue(key))






my_dict = {}
isinstance(my_dict, abc.Mapping)

word.strip('.,!').lower()

list_a = [(0, 1), (0, 1), (0, 1)]
# import operator
items = sorted(list_a, key=operator.itemgetter(1), reverse=True)

d = dict(a=1, c=3, b=2)
sorted(d.items(), key=lambda item: item[1])
# [('a', 1), ('b', 2), ('c', 3)]
sorted(d.items(), key=operator.itemgetter(1))
# [('a', 1), ('b', 2), ('c', 3)]

list_b = [28, 14, '28', 5, '9', '1']
sorted(list_b, key=int)
sorted(list_b, key=str)

# sort by len
lst_sort = sorted(lst, reverse=True, key=len)

# Sort 2D array using 2nd column
sorted(movie_year, key=lambda row: row[1], reverse=True)


collections.Counter(list).most_common(3)    # from collection import Counter
collections.Counter(a).most_common(1)[0][1]

set1 | set2    # set1.union(set2)
set1 & set2    # set1.intersection(set2)
set1 - set2    # set1.difference(set2)
set1 ^ set2    # set1.symmetric_difference(set2)

g1 = set(globals())
import something
g2 = set(globals())
g2 - g1

set.remove(2)
set.pop()
set.add('el')

frozen = frozenset(['el1', 'el2', 'el3'])    # immuteble set()

# for x in a:
#     for y in b:
#         if x == y:
#             yield (x,y)
return set(a) & set(b)

# Matching subset
set(a) < set(b)








with open(file) as f:
    file.write()
    file.tell()
    file.read()
    file.seek(0)
    file.readline()
    file.readlines()




int_list = [1, 2, 3, 4]
print(*int_list)

for i, item in enumerate(iterable):
    print(i, item)

list(enumerate('abc'))
list(enumerate('abc', 1))


import ast
expr = "[1, 2, 3]"
my_list = ast.literal_eval(expr)


import pdb
pdb.set_trace()

if n in [1, 4, 5, 6]:
    pass

a = [1, 2, 3, 4]
a[::-1]

foo = "yasoob"
foo[::-1]

from pprint import pprint
pprint(my_dict)













import requests

params = {'#q': 'pizza'}
r = requests.get("https://www.google.com", params=params)
print("Status: ", r.status_code)
print(r.url)
print(r.text)

from io import BytesIO
from PIL import Image

r = requests.get("https://img.purch.com/rc/1920x1200/aHR0cDovL3d3dy5zcGFjZS5jb20vaW1hZ2VzL2kvMDAwLzA1Ni8xNzAvb3JpZ2luYWwvb3V0bGllci1nYWxheHktdWdjLTQ4NzktMTkyMC5qcGc=")
print("Status code:", r.status_code)
image = Image.open(BytesIO(r.content))
print(image.size, image.format, image.mode)
path = "./image1." + image.format

try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image")

my_data = {"name": "Nick", "email": "nick@example.co"}
r = requests.post("https://www.w3schools.com/php/welcome.php", data=my_data)






req = requests.get('https://yandex.ru/search/g', params={'text': 'Python'})
req.status_code
req.headers['Content-Type']
req.content  # bytes
req.text

with open('python.html', 'w', encoding='utf-8') as f:
    f.write(req.text)






import simplejson as json

url = "https://goo.gl/"
payload = {"longUrl": "http://example.com"}
headers = {"Content-Type": "application/json"}
r = requests.post(url, json=payload, headers=headers)
print(json.loads(r.text))
print(r.headers)

cat file.json | python -m json.tool




from collections import defaultdict
import json

def tree():
    """
    Factory that creates a defaultdict that also uses this factory
    """
    return defaultdict(tree)

root = tree()
root['Page']['Python']['defaultdict']['Title'] = 'Using defaultdict'
root['Page']['Python']['defaultdict']['Subtitle'] = 'Create a tree'
root['Page']['Java'] = None

print(json.dumps(root, indent=4))

# The "json" module can do a much better job:
import json
print(json.dumps(my_mapping, indent=4, sort_keys=True))
{
    "a": 23,
    "b": 42,
    "c": 12648430
}
# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
json.dumps({all: 'yup'})
TypeError: keys must be a string

cat json
# {"$id":"1","currentDateTime":"2019-04-25T14:16Z","utcOffset":"00:00:00",
# "isDayLightSavingsTime":false,"dayOfTheWeek":"Thursday","timeZoneName":"UTC",
# "currentFileTime":132006753872039629,"ordinalDate":"2019-115",
# "serviceResponse":null}
null = None
true = True
false = False
with open('json') as f:
    j = eval(f.read())
j
# {'currentFileTime': 132006753872039629, 'isDayLightSavingsTime': False,
# 'dayOfTheWeek': 'Thursday', 'utcOffset': '00:00:00',
# 'serviceResponse': None,
# '$id': '1', 'timeZoneName': 'UTC', 'ordinalDate': '2019-115',
# 'currentDateTime': '2019-04-25T14:16Z'}


db = MySQLdb.connect("localhost", "username", "password", "dbname")
cursor = db.cursor()
sql = "SELECT `name`, `age` FROM `ursers` ORDER BY `age` DESC"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row[0] + row[1])
db.close()




import array
a = array.array('c', s)
print(a)
# array('c', 'Hello, world')
a[0] = 'y'
print(a)
# array('c', 'yello, world')
a.tostring()
# 'yello, world'




with open("/path/to/file") as f:
    for line in f:
        print(line)

f = open("/path/tofile", 'w')
for e in aList:
    f.write(e + "\n")
f.close()







theList = ["a", "b", "c"]
joinedString = ",".join(theList)

targetList = list(set(targetList))
targetList = [v for v in targetList if not v.strip() == '']
targetList = filter(lambda x: len(x) > 0, targetList)









d = {'flux': 1}
d.clear()
li = ['spam', 'egg', 'spam']
li.clear()

a, b, c = range(3)

values = range(5)
a, b, _, _, _ = values
a, b, *rest = values
a, *rest, b = range(5)
*rest, a, b = range(5)

f = open('data.txt')
first, second, *rest, last = f.readlines()
f.close()





import warnings; warnings.simplefilter('ignore')  # Fix NumPy issues.

from numpy import array, cos, sin
def rotate(vector, angle):
    θ = angle
    mat = [[cos(θ), -sin(θ)],
           [sin(θ), cos(θ)]]
    mat = array(mat)
    return mat @ vector





python -m timeit -s 'a = (10, 20, 30)' 'a[1]'
# 10000000 loops, best of 3: 0.0304 usec per loop
python -m timeit -s 'a = [10, 20, 30]' 'a[1]'
# 10000000 loops, best of 3: 0.0309 usec per loop

python -m timeit -s 'a = (10, 20, 30)' 'x, y, z = a'
# 10000000 loops, best of 3: 0.0249 usec per loop
python -m timeit -s 'a = [10, 20, 30]' 'x, y, z = a'
# 10000000 loops, best of 3: 0.0251 usec per loop

python -m timeit -n 100 -s "s = 'A'*10000; import textwrap; textwrap.fill(s)"
# 100 loops, best of 5: 12.3 nsec per loop
python -m timeit -s "s = 'A'*10000; import textwrap; textwrap.fill(s)"
# 20000000 loops, best of 5: 11.8 nsec per loop


import timeit
print(timeit.timeit("a and b", globals=globals()))

print(timeit.timeit('[n**2 for n in range(10) if n%2==0]', number=10000))

print(timeit.timeit("gcd(*rand())", number=100000, globals=globals()))

# The "timeit" module lets you measure the execution
# time of small bits of Python code
timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
# 0.3412662749997253

timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
# 0.2996307989997149

timeit.timeit('"-".join(map(str, range(100)))', number=10000)
# 0.24581470699922647


# fastest reversing string in Python
timeit.timeit('"asdfg"[::-1]', number=1000000)

arr = [str(d) for d in range(101)]
timeit.timeit('sorted(map(int, set(arr)))', number=10000, globals=globals())
# 0.33720446200004517
timeit.timeit('sorted(int(s) for s in set(arr))', number=10000, globals=globals())
# 0.45892249400003493

arr = (str(d) for d in range(101))
timeit.timeit('sorted(map(int, set(arr)))', number=1000000, globals=globals())
# 0.8356489219995638
timeit.timeit('sorted(int(s) for s in set(arr))', number=1000000, globals=globals())
# 0.9175120390000302















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








num_list = range(7)
squared_list = [x ** 2 for x in num_list]
list(zip(num_list, squared_list))

list(filter(bool, range(3)))  # <-> [x for x in range(3) if x]



["%-3d%12d" % (exponent, 10**exponent) for exponent in range(7, 11)]
# ['7      10000000', '8     100000000', '9    1000000000', '10  10000000000']

# list cut on sets
n, arr = 2, list(range(10))
[set(arr[i:i+n]) for i in list(range(len(arr))[::n])]
# [{0, 1}, {2, 3}, {4, 5}, {6, 7}, {8, 9}]





x = [1, 5, 2, 3]
y = list(map(lambda x: x**2, x))
print(*y)

print(min([i for i in map(int, input().split()) if i % 2 != 0]))
print(min(filter(lambda x: x % 2 != 0, map(int, input().split()))))
print(min(map(int, input().split()), key=lambda x: (not x % 2, x)))




list = [x for x in list if x.strip() != '']

(lambda x: x**2)(2)

(lambda x, y: x + y)(5, 3)
sorted(range(-5, 6), key=lambda x: x ** 2)


# squarity
list(map(lambda a: a**2, range(5)))

# is_positive
list(filter(lambda a: a > 0, range(-2, 3)))










import functools
prints = functools.partial(print, end=' ')
prints()
print(functools.reduce(lambda x, y: x + y, [1, 2, 3]))





# Better
# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = [str(n) for n in range(20)]
print("".join(nums))

# Best
# create a concatenated string from 0 to 19 (e.g. "012..1819")
nums = map(str, range(20))
print("".join(nums))

result = process(x) if is_valid(x) else print('invalid item: ', x)

print(min([i for i in nums if i % 2 != 0]))

enumerate(list)
print(*enumerate('abcde'))



reduce(lambda x, y: x*(y**5), map(int, input().split()), 1)
print(*map(lambda x, y: x ^ y,
           map(int, input().split()), map(int, input().split())))

ls = [[*map(int, i.split())] for i in sys.stdin]
(n, e, d), ps, res = ls[0], [*range(ls[0][0] + 1)], 1




# res = 0
# if a > 0:
#     res += 1
# if b > 0:
#     res += 1
# if c > 0:
#     res += 1
res = (a > 0) + (b > 0) + (c > 0)


# integer quotient of division with rounding up
(m + n - 1) // n


# [expression]?[on_true]:[on_false]
[on_true] if [expression] else [on_false]




# Why Python is Great: Namedtuples
# Using namedtuple is way shorter than
# defining a class manually:
from collections import namedtuple
Car = namedtup1e('Car', 'color mileage')

# Our new "Car" class works as expected:
my_car = Car('red', 3812.4)
my_car.color
'red'
my_car.mileage
3812.4

# We get a nice string repr for free:
my_car
Car(color='red' , mileage=3812.4)

# Like tuples, namedtuples are immutable:
my_car.color = 'blue'
AttributeError: "can't set attribute"


# The get() method on dicts
# and its "default" argument
name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

greeting(382)
"Hi Alice!"

greeting(333333)
"Hi there!"



# How to sort a Python dict by value
# (== get a representation sorted by value)
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

sorted(xs.items(), key=lambda x: x[1])
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]

# Or:
import operator
sorted(xs.items(), key=operator.itemgetter(1))
[('d', 1), ('c', 2), ('b', 3), ('a', 4)]


# Different ways to test multiple
# flags at once in Python
x, y, z = 0, 1, 0
if x == 1 or y == 1 or z == 1:
    print('passed')
if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
if x or y or z:
    print('passed')
if any((x, y, z)):
    print('passed')



# How to merge two dicts
# in Python 3.5+
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

z = {**x, **y}
z
# {'c': 4, 'a': 1, 'b': 3}

# In Python 2.x you could
# use this:
z = dict(x, **y)
z
{'a': 1, 'c': 4, 'b': 3}




# The lambda keyword in Python provides a
# shortcut for declaring small and
# anonymous functions:

add = lambda x, y: x + y
add(5, 3)
8

# You could declare the same add()
# function with the def keyword:
def add(x, y):
    return x + y
add(5, 3)
8

# So what's the big fuss about?
# Lambdas are *function expressions*:
(lambda x, y: x + y)(5, 3)
8

# • Lambda functions are single-expression
# functions that are not necessarily bound
# to a name (they can be anonymous).

# • Lambda functions can't use regular
# Python statements and always include an
# implicit `return` statement.

sorted(range(-5, 6), key=lambda x: x ** 2)
# [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]



# Harmful:
list(filter(lambda x: x % 2 == 0, range(16)))
# [0, 2, 4, 6, 8, 10, 12, 14]

# Better:
[x for x in range(16) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14]



# The standard string repr for dicts is hard to read:
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
my_mapping
{'b': 42, 'c': 12648430. 'a': 23}  # 😞







# Why Python Is Great:
# In-place value swapping
# Let's say we want to swap
# the values of a and b...
a = 23
b = 42

# The "classic" way to do it
# with a temporary variable:
tmp = a
a = b
b = tmp

# Python also lets us
# use this short-hand:
a, b = b, a




# Python Riddle: 👻 it is a mystery
# What will this expression evaluate to?
{True: 'yes', 1: 'no', 1.0: 'maybe'}




# "is" vs "=="
a = [1, 2, 3]
b = a

a is b
True
a == b
True

c = list(a)

a == c
True
a is c
False

# • "is" expressions evaluate to True if two
#   variables point to the same object

# • "==" evaluates to True if the objects
#   referred to by the variables are equal





# Functions are first-class citizens in Python.
# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.
def myfunc(a, b):
    return a + b

funcs = [myfunc]
funcs[0]
<function myfunc at 0x107012230>
funcs[0](2, 3)
5




# Because Python has first-class functions they can
# be used to emulate switch/case statements
def dispatch_dict(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'div': lambda: x / y,
    }.get(operator, lambda: None)()


dispatch_dict('mul', 2, 8)
# 16

dispatch_dict('unknown', 2, 8)
# None









# Python's list slice syntax can be used without indices
# for a few fun and useful things:
# You can clear all elements from a list:
lst = [1, 2, 3, 4, 5]
del lst[:]
lst
# []

# You can replace all elements of a list
# without creating a new list object:
a = lst
lst[:] = [7, 8, 9]
lst
# [7, 8, 9]
a
# [7, 8, 9]
a is lst
# True

# You can also create a (shallow) copy of a list:
b = lst[:]
b
# [7, 8, 9]
b is lst
# False

args = [3, 6]
list(range(*args))
# [3, 4, 5]




# collections.Counter lets you find the most common
# elements in an iterable:
import collections
c = collections.Counter('helloworld')
c
# Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})

c.most_common(3)
# [('l', 3), ('o', 2), ('e', 1)]





# When To Use __repr__ vs __str__?
# Emulate what the std lib does:
import datetime
today = datetime.date.today()

# Result of __str__ should be readable:
str(today)
'2017-02-02'

# Result of __repr__ should be unambiguous:
repr(today)
'datetime.date(2017, 2, 2)'

# Python interpreter sessions use
# __repr__ to inspect objects:
today
datetime.date(2017, 2, 2)



import datetime
now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))













# Python 3.3+ has a std
# lib module for displaying
# tracebacks even when Python
# "dies", e.g with a segfault:
import faulthandler
faulthandler.enable()

# Can also be enabled with
# "python -X faulthandler"
# from the command line.

# Learn more here:
# https://docs.python.org/3/library/faulthandler.html















# Pythonic ways of checking if all
# items in a list are equal:
lst = ['a', 'a', 'a']
# I ordered those from "most Pythonic" to "least Pythonic"
# and  "least efficient" to "most efficient".
# The len(set()) solution is idiomatic,  but constructing
# a set is less efficient memory and speed-wise.
len(set(lst)) == 1
# True
all(x == lst[0] for x in lst)
# True
lst.count(lst[0]) == len(lst)
# True





# In Python 3.4+ you can use
# contextlib.suppress() to selectively
# ignore specific exceptions:
import contextlib
with contextlib.suppress(FileNotFoundError):
    os.remove('somefile.tmp')

# This is equivalent to:
try:
    os.remove('somefile.tmp')
except FileNotFoundError:
    pass
# contextlib.suppress docstring:
#
# "Return a context manager that suppresses any
#  of the specified exceptions if they occur in the body
#  of a with statement and then resumes execution with
#  the first statement following the end of
#  the with statement."


from contextlib import contextmanager
@contextmanager
def tag(name):
    print("[%s]" % name)
    yield
    print("[/%s]" % name)



# In Python 3 you can use a bare "*" asterisk
# in function parameter lists to force the
# caller to use keyword arguments for certain
# parameters:
def f(a, b, *, c='x', d='y', e='z'):
    return 'Hello'

# To pass the value for c, d, and e you
# will need to explicitly pass it as
# "key=value" named arguments:
f(1, 2, 'p', 'q', 'v')
# TypeError: "f() takes 2 positional arguments but 5 were given"

f(1, 2, c='p', d='q',e='v')
# 'Hello'



# Python 3.5+ allows passing multiple sets
# of keyword arguments ("kwargs") to a
# function within a single call, using
# the "**" syntax:
def process_data(a, b, c, d):
    print(a, b, c, d)

x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}

process_data(**x, **y)
# 1 2 3 4
process_data(**x, c=23, d=42)
# 1 2 23 42





import operator


# itertools.starmap
list(map(pow, [(2, 5), (3, 2), (10, 3)]))
# -> TypeError: pow expected at least 2 arguments, got 1



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







# Intialize the list
my_list = [1, 3, 6, 10]
a = (x**2 for x in my_list)

next(a)
# output: 1

next(a)
# output: 9

next(a)
# output: 36

next(a)
# output: 100

next(a)
# output: StopIteration

# s = ''
# for x in list:
#     s += some_function(x)
slist = [some_function(elt) for elt in somelist]
s = ''.join(slist)






with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)


number = count if count % 2 else count - 1
name = user.name() if user is not None else 'Guest'








pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]





all({x**3: x == round((x**3)**(1/3)) for x in range(21)}.values())
all(x == round((x**3)**(1/3)) for x in range(21))

"0123456789"[6:3:-1]
# "654"


# cubic root
round(x**(1/3))

from math import gcd
gcd(100, 75)
# 25


dict.fromkeys(range(5), None)
# {0: None, 1: None, 2: None, 3: None, 4: None}
dict(zip(map(float, lst[::2]), lst[1::2]))



max([min(map(int, tuple(s.split()))) for s in input_])



import functools
functools.reduce(operator.mul, range(1, 11))  # math.factorial(10)
# 3628800

sorted((''.join(tup) for i in rang
                   for tup in itertools.combinations(sorted(string), i)),
                  key=lambda x: (len(x), x))


from collections import defaultdict
defaultdict(int)
defaultdict(list)
defaultdict(set)


assert issubclass(bool, int)
assert isinstance(lst, list)
assert isinstance(lst, tuple), 'TypeError'
assert id(obj1) == id(obj2) # obj1 is obj2
assert el in seq


# amount different mutable/immutable elements
objects = [1, [2], 1, [2], 3]
len({id(el) for el in objects})  # len(set(id(el) for el in objects))
# 4

tuple(filter(lambda x: x.isdigit(), ['d', '1', 'f', '5']))
tuple(x for x in ['d', '1', 'f', '5'] if x.isdigit())
# ('1', '5')


pi: float = 3.142
deq: Deque = collections.deque()


hasattr(a, 'attr')

getattr(d, cmd)(*args)
tuple(getattr(deq, el[0])() if len(el) == 1 else getattr(deq, el[0])(el[1])
      for el in raw_commands)


func.__closure__.cell_contents

sys.modules
sys.path

__all__ = []



file.writelines()


operatot.itemgetter(-1)
operatot.attrgetter('sort')

mod_checker = lambda x, mod=0: lambda y: True if y % x == mod else False



sys.exit(0)

from code import interact





(0, 1, 2, 3) == tuple(reversed([3, 2, 1, 0]))
# True
''.join(reversed('aaabbb'))
# bbbaaa
''.join(reversed('aabbaa')) == 'aabbaa'
# True




import io
import sys
sys.stdin = io.StringIO("1\n2\n3\n4\n5\n6\n7\n8\n9")


# if x == 0 or x == 1
# if x <= 1
if x in {0, 1}: ...

# if t in s:
#     print(pattern_in_string(t, s))
# else:
#     print(0)
print(pattern_in_string(t, s) if t in s else 0)




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







{}.fromkeys(chunk)
# 'AAB' -> {'A': None, 'B': None}


[*iterable]
(*iterable,)



for i in foo:
    if i == 0:
        break
else:
    print("i was never 0")


(func1 if y == 1 else func2)(arg1, arg2)
(class1 if y == 1 else class2)(arg1, arg2)



class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

point = Bunch(datum=y, squared=y*y, coord=x)


# n(n+1)/2
(100 * 101) // 2  # sum 1..100
# 5050
sum(range(101))
# 5050







import re

# "[^"\s,):]
# [^"\s,):]"
# leap([\s\w+])year

len(max(re.findall(r'(1+)', '3441153111154354113111111')))
# 6

bool(re.findall(r'c{1}(\w*)w{1}(\w*)h{1}(\w*)', 'dcsdgfwgdh'))
# True

# +-float
pattern = re.compile(r'^[-+]?[0-9]*\.[0-9]+$')
pattern.match('text')
print(bool(pattern.match('text')))

# split
import re
regex_pattern = r"[,.]"
re.split(regex_pattern, '100,000,000.000')
# ['100', '000', '000', '000']


sentence = "this is a test, not testing."
it = re.finditer('\\btest\\b', sentence)
for match in it:
    print("match position: " + str(match.start()) + "-" + str(match.end()))

# search 123-123 like strings
m = re.search(r'\d+-\d+', line)
if m:
    current = m.group(0)

re.IGNORECASE | re.DEBUG
