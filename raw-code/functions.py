# -*- coding: utf-8 -*-
import random
from typing import Generator


def collections_deque(data, shift):
    # shift a list in python
    from collections import deque
    items = deque(data)
    items.rotate(-shift)
    return items


def check(seq, elem):
    # if elem in seq:
    #     return True
    # return False
    return elem in seq


def find(required_el, lst):
    try:
        return lst.index(required_el)
    except ValueError:
        return -1


def find_(required_el, lst):
    if required_el in lst:
        return lst.index(required_el)
    return -1


def f_(a, lst=None):
    if lst is None:
        lst = []
    lst.append(a)
    return lst


def unique(seq, idfun=repr):
    seen = {}
    return [seen.setdefault(idfun(e), e) for e in seq if idfun(e) not in seen]


def valid_sign(sign: str):
    # Single-character match
    return sign in {'+', '-'}


def majority_element(arr: list):
    # from collections import Counter
    # return Counter(arr).most_common()[0][0]
    arr.sort()
    return arr[len(arr)//2]


def rev(lst: list):
    """
    >>> rev([1, 2, 3])
    [3, 2, 1]
    """
    return lst[::-1]


def pop_append(data: list, shift: int):
    for _ in range(shift):
        data.append(data.pop(0))
    return data


def chunks(s: str, k: int) -> Generator:
    n = len(s) // k
    return (sub_s for sub_s in (s[i:i + k:] for i in range(len(s))[::n]))


def get_magic_number(cond):
    return 666 if cond else 999


def make_closure(x):
    """
    >>> make_closure(2)()
    2
    4
    """
    def closure():
        nonlocal x
        print(x)
        x *= 2
        print(x)
    return closure


def f(x):
    """
    >>> f(3)
    'abc'
    """
    def h():
        nonlocal x
        x = 'abc'
    x += 1
    h()
    return x


def type_stats(type_obj):
    """
    >>> type_stats(tuple)
    3136
    >>> type_stats(list)
    659
    >>> type_stats(tuple)
    6953
    >>> type_stats(list)
    2455
    """
    import gc
    count = 0
    for obj in gc.get_objects():
        if type(obj) == type_obj:
            count += 1
    return count


def parrot(voltage, state='a stiff', action='voom'):
    """
    >>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
    >>> parrot(**d)
    "-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !"
    """
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")


def better_contains(haystack, needle):
    # Personally, I'm not a fan of the `else`
    # "completion clause" in loops because
    # I find it confusing. I'd rather do
    # something like this:
    for item in haystack:
        if item == needle:
            return
    raise ValueError('Needle not found')
    # Note: Typically you'd write something
    # like this to do a membership test,
    # which is much more Pythonic:
    if needle not in haystack:
        raise ValueError('Needle not found')


def info(object, spacing=10, collapse=1):  # 1 2
    """
    Print methods and doc strings.
    Takes module, class, list, dictionary, or string.
    """
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    print("\n".join(["%s %s" %
                     (method.ljust(spacing),
                      processFunc(str(getattr(object, method).__doc__)))
                     for method in methodList]))


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


def timeit_(param: str, n: int = 10000) -> float:
    from timeit import timeit
    return timeit(param, number=n, globals=globals())


def compare(fs, args):
    import timeit
    from matplotlib import pyplot as plt
    for f in fs:
        plt.plot(args, [timeit.timeit(str(f(arg)), number=10000000)
                        for arg in args], label=f.__name__)
    plt.legend()
    plt.grid(True)
    plt.show()


def rand():
    import random
    c = random.randint(1, 100000)
    a = c * random.randint(1, 100000)
    b = c * random.randint(1, 100000)
    return a, b


def random_product(*args, repeat=1):
    """Random selection from itertools.product(*args, **kwds)"""
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(random.choice(pool) for pool in pools)


def random_permutation(iterable, r=None):
    """Random selection from itertools.permutations(iterable, r)"""
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))


def random_combination(iterable, r):
    """Random selection from itertools.combinations(iterable, r)"""
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)


def random_combination_with_replacement(iterable, r):
    """Random selection from itertools.combinations_with_replacement(iterable, r)"""
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.randrange(n) for i in range(r))
    return tuple(pool[i] for i in indices)


def goodbye(name, adjective):
    print('Goodbye, %s, it was %s to meet you.' % (name, adjective))

import atexit
atexit.register(goodbye, 'Donny', 'nice')
