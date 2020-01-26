# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2017-09-09 14:03:30
# @Last Modified by:   razor87
# @Last Modified time: 2020-01-26 18:04:19
import dis
import sys
import array
import numpy as np
from pympler import asizeof

sys.argv
sys.executable
sys.exit(0)
sys.path
sys.platform
sys.modules
sys.getrefcount
sys.maxsize  # 9223372036854775807

sys.getsizeof(range(10))  # == asizeof.flatsize
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


dir(5)
# ['__abs__', '__add__', ...]
dir(sys)
# ['__breakpointhook__', '__displayhook__', '__doc__', ...]
abs.__doc__  # 'abs(number) -> number
# Return the absolute value of the argument.

dis.dis(func)
func.__code__.co_code
func.__closure__.cell_contents
hasattr(a, 'attr')
getattr(d, cmd)(*args)

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



class SameHash():
    def __hash__(self):
        return 1

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



half_size = len(numbers) // 2
median = sum(numbers[half_size - 1:half_size + 1]) / 2


[*"string"]  # iterable -> list
# ['s', 't', 'r', 'i', 'n', 'g']

*[1, 2, 3, 4],
(*[1, 2, 3, 4],)  # iterable -> tuple
# (1, 2, 3, 4)

[1, 2, *[3, 4]]  # Since Python 3.5
# [1, 2, 3, 4]

animals = [
    'bird',
    'fish',
    'elephant',
]
for (first_char, *_, last_char) in animals:
    print(first_char, last_char)
# b d
# f h
# e t

a, b, c = range(3)
a, b, c
# (0, 1, 2)
values = range(5)
a, b, _, _, _ = values
a, b
# (0, 1)
a, b, *rest = values
a, b, rest
# (0, 1, [2, 3, 4])
a, b, c, d, e, *rest = values
a, b, c, d, e, rest
# (0, 1, 2, 3, 4, [])

*lst, = range(5)  # == [*lst]
lst
# [0, 1, 2, 3, 4]
*lst2, = (1, 2, 3)
lst2
# [1, 2, 3]
for *b, in [(1, 2, 3), (4, 5, 6, 7)]:
    print(b)
# [1, 2, 3]
# [4, 5, 6, 7]



# Python Riddle: 👻 it is a mystery
# What will this expression evaluate to?
{True: 'yes', 1: 'no', 1.0: 'maybe'}
# {True: 'maybe'}
True == 1 == 1.0
# True
hash(True), hash(1), hash(1.0)
# (1, 1, 1)

(id(False), id(True)) == (id(1 != 1), id(1 == 1)) == (id(bool()), id(bool(1)))
# True

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




class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

point = Bunch(datum=y, squared=y*y, coord=x)



def __repr__(self):
    return f"<{type(self).__name__}(id={self.id})>"



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

any(f() for f in (f1, f2, f3))  # == f1() or f2() or f3()
# True
# True

all(f() for f in (f1, f2, f3))  # == f1() and f2() and f3()
# True
# False
# False



# Else Clauses on Loop Statements
for i in foo:
    if i == 0:
        break
else:
    print("i was never 0")


lst = []
while x:
    print("Then")
    lst.pop()
else:
    print("Else")
# Else


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


# Data type choice
set1 = set([tuple(entry.items()) for entry in list1])
set2 = set([tuple(entry.items()) for entry in list2])
common = set1.intersection(set2)
common = [dict(entry) for entry in common]



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




import atexit
def goodbye(name, adjective):
    print('Goodbye, %s, it was %s to meet you.' % (name, adjective))
atexit.register(goodbye, 'Donny', 'nice')


import gc
def cleanup():
    # do any cleanup work here...

    # call the garbage collector?
    gc.collect()
    pass
atexit.register(cleanup)



# In Python 3.4+ you can use
# contextlib.suppress() to selectively
# ignore specific exceptions:
from contextlib import suppress
with suppress(FileNotFoundError):
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

@contextmanager
def managed_resource(*args, **kwds):
    # Code to acquire resource, e.g.:
    resource = acquire_resource(*args, **kwds)
    try:
        yield resource
    finally:
        # Code to release resource, e.g.:
        release_resource(resource)

with managed_resource(timeout=3600) as resource:
    # Resource is released at the end of this block,
    # even if code in the block raises an exception


@contextmanager
def make_context():
    print('  entering')
    try:
        yield {}
    except RuntimeError as err:
        print('  ERROR:', err)
    finally:
        print('  exiting')



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
        h(x)
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




def f(*, a=1, b=2, c=4, **kwargs):
    # Future-proof APIs with keyword-only arguments
    return sum([a, b, c]) + sum(kwargs.values())



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
