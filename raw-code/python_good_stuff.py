# -*- coding: utf-8 -*-
import dis
import sys
import array
import numpy as np


help(5)
dir(5)
# ['__abs__', '__add__', ...]

abs.__doc__
# 'abs(number) -> number
# Return the absolute value of the argument.


dis.dis(func)
func.__code__.co_code

func.__closure__.cell_contents
hasattr(a, 'attr')
getattr(d, cmd)(*args)

(int)(num) == int(num)

dis.dis(compile("(10, 'abc')", '', 'eval'))

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
sys.exit(0)
sys.path
sys.platform
sys.modules

sys.maxsize
# 9223372036854775807

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





class SameHash():
    def __hash__(self): return 1

a, b = SameHash(), SameHash()
a == b
# False
a is b
# False
hash(a), hash(b)
# (1, 1)
id(a), id(b)
# (109078728, 109077320)

hash(())  # hash(tuple())
# 3527539


from copy import deepcopy
x = [[0, 0], [1, 1]]
y = deepcopy(x)
print('x', x, id(x), id(x[0]), id(x[1]))


li = ['spam', 'egg', 'spam']
li.clear()


half_size = len(numbers) // 2
median = sum(numbers[half_size - 1:half_size + 1]) / 2

# Since Python 3.5
[1, 2, *[3, 4]]
# [1, 2, 3, 4]


a, b, c = range(3)
values = range(5)
a, b, _, _, _ = values
a, b, *rest = values
a, *rest, b = range(5)
*rest, a, b = range(5)


[*iterable]
# iterable -> list
(*iterable,)
# iterable -> tuple
[*"string"]
# ['s', 't', 'r', 'i', 'n', 'g']


import array
a = array.array('c', s)
print(a)
# array('c', 'Hello, world')
a[0] = 'y'
print(a)
# array('c', 'yello, world')
a.tostring()
# 'yello, world'


# Python Riddle: 👻 it is a mystery
# What will this expression evaluate to?
{True: 'yes', 1: 'no', 1.0: 'maybe'}
# {True: 'maybe'}
True == 1 == 1.0
# True
hash(True), hash(1), hash(1.0)
# (1, 1, 1)

print(id(False), id(True))
# 8791482468720 8791482468688
print(id(1 != 1), id(1 == 1))
# 8791482468720 8791482468688
print(id(bool()), id(bool(1)))
# 8791482468720 8791482468688


bool(bool)          # True
bool(12)            # True
bool('asdsa')       # True
bool(0)             # False
bool('')            # False
bool(None)          # False
answer = None
answer is None      # True
answer is not None  # True


assert issubclass(bool, int)
assert isinstance(lst, list)
assert isinstance(my_dict, abc.Mapping)
assert isinstance(lst, tuple), 'TypeError'
assert id(obj1) == id(obj2)  # obj1 is obj2
assert el in seq






# [expression]?[on_true]:[on_false]
[on_true] if [expression] else [on_false]  # Ternary operator

result = process(x) if is_valid(x) else print('invalid item: ', x)

number = count if count % 2 else count - 1
name = user.name() if user is not None else 'Guest'

xP == hP and text[:m] == P and print(0, end=' ')

(func1 if expression else func2)(args)


db = MySQLdb.connect("localhost", "username", "password", "dbname")
cursor = db.cursor()
sql = "SELECT `name`, `age` FROM `ursers` ORDER BY `age` DESC"
cursor.execute(sql)
results = cursor.fetchall()
for row in results:
    print(row[0] + row[1])
db.close()







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






__all__ = []



for i in foo:
    if i == 0:
        break
else:
    print("i was never 0")



class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

point = Bunch(datum=y, squared=y*y, coord=x)





def f1(): print("True"); return True
def f2(): print("False"); return False
def f3(): print("True"); return True


any((f1(), f2(), f3()))
# True
# False
# True
# True

all((f1(), f2(), f3()))
# True
# False
# True
# False

f1() or f2() or f3()
# True
# True

f1() and f2() and f3()
# True
# False
# False






# amount different mutable/immutable elements
objects = [1, [2], 1, [2], 3]
len({id(el) for el in objects})  # len(set(id(el) for el in objects))
# 4


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



# s = ''
# for x in list:
#     s += some_function(x)
slist = [some_function(elt) for elt in somelist]
s = ''.join(slist)



# if x == 0 or x == 1
# if x <= 1
if x in {0, 1}: ...

# if t in s:
#     print(pattern_in_string(t, s))
# else:
#     print(0)
print(pattern_in_string(t, s) if t in s else 0)




# res = 0
# if a > 0:
#     res += 1
# if b > 0:
#     res += 1
# if c > 0:
#     res += 1
res = (a > 0) + (b > 0) + (c > 0)




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

now = datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))




# Attribute access on nullable value
a and a.x
a and a.f()
match = re.match(r, s)
return match and match.group(0)

# Finding first matching element
try:
    x = next(i for i, n in enumerate(l) if n > 0)
except StopIteration:
    print('No positive numbers')
else:
    print('The index of the first positive number is', x)

# Truncating
del l[j:]
del l[:i]
# Anti-idiom:
l = l[:j]
l = l[i:]

# Sorted list from an iterable
d = {'a': 1, ...}
l = sorted(d)



# Building a string
s = ''.join(f(x) for x in l)

# Dict from parallel sequences of keys and values
dict(zip(keys, values))

# Data type choice
set1 = set([tuple(entry.items()) for entry in list1])
set2 = set([tuple(entry.items()) for entry in list2])
common = set1.intersection(set2)
common = [dict(entry) for entry in common]




# Membership testing with sets and dictionaries is much faster, O(1), than
# searching sequences, O(n). When testing "a in b", b should be a set or
# dictionary instead of a list or tuple.





# "is" vs "=="
# • "==" evaluates to True if the objects
#   referred to by the variables are equal
# • "is" expressions evaluate to True if two
#   variables point to the same object
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






# Functions are first-class citizens in Python.
# They can be passed as arguments to other functions,
# returned as values from other functions, and
# assigned to variables and stored in data structures.
def myfunc(a, b):
    return a + b

funcs = [myfunc]
funcs[0]
# <function myfunc at 0x107012230>
funcs[0](2, 3)
# 5




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



# Avoiding branch prediction failure
# There are many ways to help your code avoid branch prediction failure.
# One way is to re-structure code so that conditional statements don’t appear
# inside of loops. This can be done with clever bitwise operations or simple
# code re-writes, e.g. changing
for x in data:
    if f(z):
        g(x)
    else:
        g(x)
# into
if f(z):
    for x in data:
        g(x)
else:
    for x in data:
        h(x)
# This is somewhat cumbersome because we are duplicating logic
# (i.e. the for-loop) but even this can be abstracted away:
def loop_with(data, func):
    for x in data:
        func(x)

loop_with(data, g if f(z) else h)




# A simple way to choose one of two possible values
L1 = [1, 2, 0, 3, 0, 5]
L2 = [(p, 0xFF)[p == 0] for p in L1]  # [0xFF if p == 0 else p for p in L1]
L2
# [1, 2, 255, 3, 255, 5]



# Future-proof APIs with keyword-only arguments
def f(*, a=1, b=2, c=4, **kwargs):
    return sum([a, b, c]) + sum(kwargs.values())



# Data classes
@dataclass
class Person:
    name: str
    age: int

@dataclass
class Coder(Person):
    preferred_language: str = 'Python 3'



from collections import namedtuple
Person = namedtuple(
        'Person',
        ['name', 'age', 'height', 'ears', 'eyes'],
        defaults=(2, 2,)
)
Person('Milton', 25, 174)
# Person(name='Milton', age=25, height=174, ears=2, eyes=2)



from typing import NamedTuple

class Person(NamedTuple):
    # Type hints are optional, you don't have to use them but they are great!
    # I encorage you to learn more about them :)
    name: str
    age: int
    height: int
    ears: int = 2
    eyes: int = 2

milton = Person('Milton', 25, 174)
milton
# Person(name='Milton', age=25, height=174, ears=2, eyes=2)
caitlyn = Person(name='Caitlyn', age=25, height=174, ears=1)
caitlyn
# Person(name='Caitlyn', age=25, height=174, ears=1, eyes=2)

# Immutability
milton.name = 'Miguel'



# Append[1]        O(1)
# Pop last         O(1)
# Pop intermediate O(k)
# Insert           O(n)
# Delete Item      O(n)
# How to use a Python list as a stack (LIFO):
myStack = []
myStack.append('a')
myStack.append('b')
myStack.append('c')
myStack
# ['a', 'b', 'c']
myStack.pop()
# 'c'
myStack.pop()
# 'b'
myStack.pop()
# 'a'
myStack.pop()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# IndexError: pop from empty list




# append     O(1)
# appendleft O(1)
# pop        O(1)
# popleft    O(1)
# remove     O(1)
from collections import deque

# How to use collections.deque as a stack (LIFO):
myStack = deque()
myStack.append('a')
myStack.append('b')
myStack.append('c')
myStack
# deque(['a', 'b', 'c'])
myStack.pop()
# 'c'
myStack.pop()
# 'b'
myStack.pop()
# 'a'
myStack.pop()
# Traceback (most recent call last):
#   File "<console>", line 1, in <module>
# IndexError: pop from an empty deque

# How to use collections.deque as a FIFO queue:
q = deque()
q.append('eat')
q.append('sleep')
q.append('code')
q
# deque(['eat', 'sleep', 'code'])
q.popleft()
# 'eat'
q.popleft()
# 'sleep'
q.popleft()
# 'code'
q.popleft()
# IndexError: "pop from an empty deque"



# Support Threading
from queue import LifoQueue

# How to use queue.LifoQueue as a stack:
myStack = LifoQueue()
myStack.put('a')
myStack.put('b')
myStack.put('c')
myStack
# <queue.LifoQueue object at 0x7f408885e2b0>
myStack.get()
# 'c'
myStack.get()
# 'b'
myStack.get()
# 'a'
myStack.get_nowait()  # myStack.get() <--- Blocks / waits forever...
# Traceback (most recent call last):
# File "<console>", line 1, in <module>
# File "/usr/lib/python3.7/queue.py", line 198, in get_nowait
#   return self.get(block=False)
# File "/usr/lib/python3.7/queue.py", line 167, in get
#   raise Empty
# queue.Empty

# How to use queue.Queue as a FIFO queue:
q = Queue()
q.put('eat')
q.put('sleep')
q.put('code')
q
# <queue.Queue object at 0x1070f5b38>
q.get()
# 'eat'
q.get()
# 'sleep'
q.get()
# 'code'
q.get_nowait()
# queue.Empty
q.get()
# Blocks / waits forever...


# How to use multiprocessing.Queue as a FIFO queue:
from multiprocessing import Queue
q = Queue()
q.put('eat')
q.put('sleep')
q.put('code')
q
# <multiprocessing.queues.Queue object at 0x1081c12b0>
q.get()
# 'eat'
q.get()
# 'sleep'
q.get()
# 'code'
q.get()
# Blocks / waits forever...




import heapq
laptop_costs = {
    "Compaq": 499,
    "Dell": 530,
    "Apple": 999,
    "HP": 750,
    "ASUS": 650
}
key_values = [*zip(laptop_costs.values(), laptop_costs.keys())]
heapq.nsmallest(2, key_values)  # The 2 cheapest laptops
# [(499, 'Compaq'), (530, 'Dell')]
heapq.nlargest(2, key_values)  # The 2 expensive laptops
# [(999, 'Apple'), (750, 'HP')]
