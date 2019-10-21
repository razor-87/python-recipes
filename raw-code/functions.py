# -*- coding: utf-8 -*-


def timeit_(param: str, n: int = 10000) -> float:
    from timeit import timeit
    return timeit(param, number=n, globals=globals())


def unique(seq, idfun=repr):
    seen = {}
    return [seen.setdefault(idfun(e), e) for e in seq if idfun(e) not in seen]


def unique_stable(arr):
    dupes = {}
    for val in arr:
        if val not in dupes:
            dupes.add(val)
            yield val


def chunks(g, n=2):
    # Collect data into chunks of a maximum size
    # chunks('ABCDEFG', 3) --> ABC DEF G
    import itertools
    slicer = lambda it: itertools.islice(it, n)
    yield from map(slicer, itertools.repeat(iter(g)))


def chunks(string, k):
    yield from zip(*(iter(string),) * k)


def chunks(string: str, k: int) -> Generator:
    n = len(string)//k
    return (sub_s for sub_s in (string[i:i + k:] for i in range(len(string))[::n]))


def grouper(iterable, n, fillvalue=''):
    """Collect data into fixed-length chunks or blocks"""
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    from itertools import zip_longest
    args = (iter(iterable),) * n
    # return zip_longest(fillvalue=fillvalue, *args)
    yield from zip_longest(fillvalue=fillvalue, *args)

big_string = 'gfdgfgdgdbvcgjkjhddfgr hfghfgf kjhkhjtgg ghfvbvcbcvfhjhgjkhljhkh'
output = '\n'.join(''.join(chunk) for chunk in grouper(big_string, 10, '_'))



def wrap(string: str, k: int) -> List[str]:
    # textwrap.wrap('AABCAAADA', 3) -> ['AAB', 'CAA', 'ADA']
    import textwrap
    return textwrap.wrap(string, k)


def fill(string: str, max_width: int) -> str:
    # textwrap.fill('AABCAAADA', 3) -> 'AAB\nCAA\nADA'
    import textwrap
    return textwrap.fill(string, width=max_width)


def pattern_in_string(pattern, string):
    n = len(string) - len(pattern) + 1
    # return sum(string[i:].startswith(pattern) for i in range(n))
    return sum(sub_string == pattern
               for sub_string in (string[i:i + len(pattern)] for i in range(n)))


def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n


# shift a list in python
def collections_deque(data, shift):
    items = collections.deque(data)
    items.rotate(-shift)
    return items

def pop_append(data, shift):
    for _ in range(shift):
        data.append(data.pop(0))
    return data


def chain(*iterables):
    for i in iterables:
        yield from i
list(chain(s, t))
# ['A', 'B', 'C', 0, 1, 2]


def vowel(c):
    return c.lower() in 'aeiou'
list(filter(vowel, 'Aardvark'))
# ['A', 'a', 'a']


def get_magic_number(cond):
    return 666 if cond else 999



def make_closure(x):
    def closure():
        nonlocal x
        print(x)
        x *= 2
        print(x)
    return closure
make_closure(2)()
# 2
# 4


def f(x):
    def h():
        nonlocal x
        x = 'abc'
    x += 1
    h()
    return x

f(3)
# 'abc'





def fibonacci(number):
    a = b = 1
    for _ in range(number):
        yield a    # generator
        a, b = b, a + b


def accumulator():
    total = 0
    while True:
        value = yield total
        print('Got: {}'.format(value))
        if not value:
            break
        total += value
generator = accumulator()
generator.send(1)



def check(seq, elem):
    # if elem in seq:
    #     return True
    # return False
    return elem in seq



def gen(a, b):
    (condition)
        yield True
sum(gen(a, b))


def make_adder(n):
    return lambda x: x + n



def rev(lst):
    return lst[::-1]
b = [1, 2, 3]
rev(b)
# [3, 2, 1]

# fastest reversing string in Python
def rev_s(s):
    return s[::-1]



def remove_spaces(x: str) -> str:
    return x.replace(' ', '')



def my_range(n):
    i = 0
    while i < n:
        yield i**2
        i += 1
for i in my_range(10):
    print(i)


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print([*numbers(11)])
# [0, 2, 4, 6, 8, 10]



def type_stats(type_obj):
    import gc
    count = 0
    for obj in gc.get_objects():
        if type(obj) == type_obj:
            count += 1
    return count

type_stats(tuple)
# 3136
type_stats(list)
# 659
type_stats(tuple)
# 6953
type_stats(list)
# 2455



def rand():
    import random
    c = random.randint(1, 100000)
    a = c * random.randint(1, 100000)
    b = c * random.randint(1, 100000)
    return a, b

def compare(fs, args):
    from matplotlib import pyplot as plt
    for f in fs:
        plt.plot(args, [timeit.timeit(str(f(arg)), number=10000000)
                        for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()
# compare([fib1, fib3], list(range(50)))



def find(required_el, lst):
    try:
        return lst.index(required_el)
    except ValueError:
        return -1

def find_(required_el, lst):
    if required_el in lst:
        return lst.index(required_el)
    return -1




def stringify_list(num_list):
    return list(map(str, num_list))

def multiply(a, b):    # from functools import reduce
    return a * b
reduce(multiply, [1, 2, 3, 4, 5])


def greeter(person, greeting):    # from functools import partial
    return '{}, {}!'.format(greeting, person)
hier = partial(greeter, greeting='Hi')


def grouper(iterable, n, fillvalue=None):
    from itertools import zip_longest
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def smth_loops(width, height, depth, ...):
    from itertools import product
    shape = [width, height, depth]
    for i, j, k in product(*map(range, shape)):
        ...


def maximum_sum(list_of_lists):
    # return max(sum(l) for l in list_of_lists)
    return sum(max(list_of_lists, key=sum))

list_of_lists = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
print(maximum_sum(list_of_lists))  # -> 33







def fact(x, cache={0: 1}):
    if x not in cache:
        cache[x] = x * fact(x - 1)
    return cache[x]



def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L




def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)
# This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !




def do_something(string, start_position=0, end_position=None):
    ...

do_something(start_position=1, string='abc')



# Personally, I'm not a fan of the `else`
# "completion clause" in loops because
# I find it confusing. I'd rather do
# something like this:
def better_contains(haystack, needle):
    for item in haystack:
        if item == needle:
            return
    raise ValueError('Needle not found')
    # Note: Typically you'd write something
    # like this to do a membership test,
    # which is much more Pythonic:
    if needle not in haystack:
        raise ValueError('Needle not found')



def info(object, spacing=10, collapse=1): #1 2
    """Print methods and doc strings.
    Takes module, class, list, dictionary, or string."""
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print("\n".join(["%s %s" %
                     (method.ljust(spacing),
                      processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList]))


if __name__ == "__main__":
    print info.__doc__




def sum_nest_elem(lst: List[List[int]], i: int) -> int:
    """
    >>> lst, i = [[1, 2, 3], [40, 50, 60], [9, 8, 7]], 1
    >>> sum_nest_elem(lst, i)
    60
    """
    return sum(sub[i] for sub in lst)






def goodbye(name, adjective):
    print('Goodbye, %s, it was %s to meet you.' % (name, adjective))

import atexit
atexit.register(goodbye, 'Donny', 'nice')



def bytes2human(n):
    # http://code.activestate.com/recipes/578019
    # >>> bytes2human(10000)
    # '9.8K'
    # >>> bytes2human(100001221)
    # '95.4M'
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n



def majority_element(arr):
    # from collections import Counter
    # return Counter(arr).most_common()[0][0]
    arr.sort()
    return arr[len(arr)//2]


# Single-character match
def valid_sign(sign):
    return sign in {'+', '-'}


def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq

if __name__ == '__main__':
    profile.run('print(fib_seq(20)); print()')
