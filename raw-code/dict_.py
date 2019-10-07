# -*- coding: utf-8 -*-

from collections import defaultdict
defaultdict(int)
defaultdict(list)
defaultdict(set)


my_dict = {}
isinstance(my_dict, abc.Mapping)


d = {'flux': 1}
d.clear()
li = ['spam', 'egg', 'spam']
li.clear()


{}.fromkeys(chunk)
# 'AAB' -> {'A': None, 'B': None}



dict.fromkeys(range(5), None)
# {0: None, 1: None, 2: None, 3: None, 4: None}
dict(zip(map(float, lst[::2]), lst[1::2]))


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



# Since Python 3.5
{**{'a': 1}, 'b': 2, **{'c': 3}}
# {'a': 1, 'b': 2, 'c': 3}
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}
z = {**x, **y}
print(z)
# {'c': 4, 'a': 1, 'b': 3}


# The standard string repr for dicts is hard to read:
my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
my_mapping
{'b': 42, 'c': 12648430. 'a': 23}  # 😞



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



from pprint import pprint
pprint(my_dict)





# collections.Counter lets you find the most common
# elements in an iterable:
import collections
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



from types import MappingProxyType
def frozendict(*args, **kwargs):
    return MappingProxyType(dict(*args, **kwargs))



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



# docs.python.org/3/library/collections.html#ordereddict-examples-and-recipes
class LastUpdatedOrderedDict(OrderedDict):
    'Store items in the order the keys were last added'

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        super().move_to_end(key)


class LRU(OrderedDict):
    'Limit size, evicting the least recently looked-up key when full'

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
