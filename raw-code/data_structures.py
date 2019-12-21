# -*- coding: utf-8 -*-

"""
https://docs.python.org/3/tutorial/datastructures.html
https://docs.python.org/3/library/collections.html
https://pymotw.com/3/data_structures.html

https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences
https://docs.python.org/3/library/stdtypes.html#memoryview
https://docs.python.org/3/library/stdtypes.html#dictionary-view-objects
"""


# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
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



# https://docs.python.org/3/tutorial/datastructures.html#sets
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
set(a) & set(b)

# Matching subset
set(a) < set(b)




# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
d = {'flux': 1}
d.clear()

{}.fromkeys(chunk)
# 'AAB' -> {'A': None, 'B': None}

dict.fromkeys(range(5), None)
# {0: None, 1: None, 2: None, 3: None, 4: None}
# Dict from parallel sequences of keys and values
arr = [1, "one", 2, "two", 3, "three", 4, "four"]
dict(zip(arr[::2], arr[1::2]))
# {1: 'one', 2: 'two', 3: 'three', 4: 'four'}
dict.get('key', 'not found')
letters[c] = letters.get(c, 0) + 1
dict.update({
    'key': 'value'
})
dict.pop('key')
dict.setdefault('key', 'default')

if key in mydict:
    value = mydict[key]
else:
    value = mydict.setdefault(key, getvalue(key))

# Since Python 3.5
{**{"a": 1}, "b": 2, **{"c": 3}}
# {'a': 1, 'b': 2, 'c': 3}
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)
# {'c': 4, 'a': 1, 'b': 3}

# The standard string repr for dicts is hard to read:
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
my_mapping
# {'b': 42, 'c': 12648430. 'a': 23}

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
# {'a': 1, 'c': 4, 'b': 3}

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





# https://docs.python.org/3/library/collections.html#collections.Counter
# collections.Counter lets you find the most common
# elements in an iterable:
c = collections.Counter('helloworld')
c
# Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})

c.most_common(3)
# [('l', 3), ('o', 2), ('e', 1)]

collections.Counter(list).most_common(3)    # from collection import Counter
collections.Counter(a).most_common(1)[0][1]

sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts

# d_words = collections.defaultdict(int)
# for word in arr:
#     d_words[word] += 1
d_words = collections.Counter(arr)  # two times faster

# Iterator over elements repeating each as many times as its count.
c = Counter('ABCABC')
sorted(c.elements())
# ['A', 'A', 'B', 'B', 'C', 'C']

# Knuth's example for prime factors of 1836:  2**2 * 3**3 * 17**1
prime_factors = Counter({2: 2, 3: 3, 17: 1})
product = 1
for factor in prime_factors.elements():     # loop over factors
    product *= factor                       # and multiply them
product
# 1836
# Note, if an element's count has been set to zero or is a negative
# number, elements() will ignore it.




# https://docs.python.org/3/library/collections.html#collections.defaultdict
collections.defaultdict(int)
collections.defaultdict(list)
collections.defaultdict(set)




# https://docs.python.org/3/library/collections.html#collections.OrderedDict
# docs.python.org/3/library/collections.html#ordereddict-examples-and-recipes
class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        super().move_to_end(key)


class LRU(OrderedDict):
    """Limit size, evicting the least recently looked-up key when full"""

    def __init__(self, maxsize=128, *args, **kwds):
        self.maxsize = maxsize
        super().__init__(*args, **kwds)

    def __getitem__(self, key):
        value = super().__getitem__(key)
        self.move_to_end(key)
        return value

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.maxsize:
            oldest = next(iter(self))
            del self[oldest]





# https://docs.python.org/3/library/array.html
import array
a = array.array('c', s)
print(a)
# array('c', 'Hello, world')
a[0] = 'y'
print(a)
# array('c', 'yello, world')
a.tostring()
# 'yello, world'




# https://docs.python.org/3/library/struct.html
import struct
import binascii
values = (1, 'ab'.encode('utf-8'), 2.7)
s = struct.Struct('I 2s f')
packed_data = s.pack(*values)
print('Original values:', values)
print('Format string  :', s.format)
print('Uses           :', s.size, 'bytes')
print('Packed Value   :', binascii.hexlify(packed_data))
# Original values: (1, b'ab', 2.7)
# Format string  : I 2s f
# Uses           : 12 bytes
# Packed Value   : b'0100000061620000cdcc2c40'




# https://docs.python.org/3/library/collections.html#collections.namedtuple
from collections import namedtuple
Person = namedtuple(
        'Person',
        ['name', 'age', 'height', 'ears', 'eyes'],
        defaults=(2, 2,)
)
Person('Milton', 25, 174)
map(Person._make, [('Milton', 25, 174), ('Hilton', 35, 194)])
# Person(name='Milton', age=25, height=174, ears=2, eyes=2)
milton = {"name": "Milton", "age": 25, "height": 174, "ears": 2, "eyes": 2}
Person(**milton)


Account = namedtuple('Account', ['type', 'balance'], defaults=[0])
Account._field_defaults
# {'balance': 0}
Account('premium')
# Account(type='premium', balance=0)

class Point(namedtuple('Point', ['x', 'y'])):
    __slots__ = ()
    @property
    def hypot(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __str__(self):
        return 'Point: x=%6.3f  y=%6.3f  hypot=%6.3f' % (self.x, self.y, self.hypot)

for p in Point(3, 4), Point(14, 5/7):
#     print(p)
# Point: x= 3.000  y= 4.000  hypot= 5.000
# Point: x=14.000  y= 0.714  hypot=14.018

Book = namedtuple('Book', ['id', 'title', 'authors'])
Book.__doc__ += ': Hardcover book in active collection'
Book.id.__doc__ = '13-digit ISBN'
Book.title.__doc__ = 'Title of first printing'
Book.authors.__doc__ = 'List of authors sorted by last name'


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




# https://docs.python.org/3/library/typing.html#typing.NamedTuple
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


class Component(NamedTuple):
    part_number: int
    weight: float
    description: Optional[str] = None


class Employee(NamedTuple):
    name: str
    department: str
    salary: int
    is_remote: bool = False  # >= Python.3.6.1
bob = Employee(name='Bob', department='IT', salary=10000, is_remote=True)






# https://docs.python.org/3/library/types.html#types.MappingProxyType
from types import MappingProxyType
data = {'a': 1, 'b':2}
read_only = MappingProxyType(data)
del read_only['a']
# TypeError: 'mappingproxy' object does not support item deletion
read_only['a'] = 3
# TypeError: 'mappingproxy' object does not support item assignment

def frozendict(*args, **kwargs):
    return MappingProxyType(dict(*args, **kwargs))




# https://docs.python.org/3/library/types.html#types.SimpleNamespace
from types import SimpleNamespace
data = SimpleNamespace(a=1, b=2)
data
# namespace(a=1, b=2)
data.c = 3
data
# namespace(a=1, b=2, c=3)

import random
class DataBag(SimpleNamespace):
   def choice(self):
       items = self.__dict__.items()
       return random.choice(tuple(items))

data_bag = DataBag(a=1, b=2)
data_bag
# DataBag(a=1, b=2)
data_bag.choice()
# (b, 2)







# https://docs.python.org/3/library/enum.html
# https://pymotw.com/3/enum/index.html
import enum

class BugStatus(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

# https://docs.python.org/3/library/dataclasses.html
@dataclass
class Person:
    name: str
    age: int

@dataclass
class Coder(Person):
    preferred_language: str = 'Python 3'





# https://docs.python.org/3/library/collections.html#collections.deque
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





# https://docs.python.org/3/library/queue.html
# Support Threading
from queue import Queue, LifoQueue

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





# https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Queue
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





# https://docs.python.org/3/library/heapq.html
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





# https://docs.python.org/3/library/copy.html
from copy import deepcopy
x = [[0, 0], [1, 1]]
y = deepcopy(x)
"x", x, id(x), id(x[0]), id(x[1])
# ('x', [[0, 0], [1, 1]], 105397832, 106669896, 132544264)
