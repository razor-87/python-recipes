# -*- coding: utf-8 -*-
import collections
import functools
import math
import operator
import random
import timeit


def factorials(n: int, cache: dict = {}) -> int:
    """
    >>> factorials(1)
    1
    >>> factorials(5)
    120
    >>> factorials(10)
    3628800
    >>> factorials(10)
    3628800
    """
    if n in cache:
        return cache[n]
    cache[n] = functools.reduce(operator.mul, range(1, n+1))
    # cache[n] = math.factorial(n)
    return cache[n]


def factorials_2(n: int, cache: dict = collections.defaultdict(int)) -> int:
    """
    >>> factorials_2(1)
    1
    >>> factorials_2(5)
    120
    >>> factorials_2(10)
    3628800
    >>> factorials_2(10)
    3628800
    """
    if n in cache:
        return cache[n]
    cache[n] += functools.reduce(operator.mul, range(1, n+1))
    # cache[n] += math.factorial(n)
    return cache[n]


def factorials_3(n: int, cache: dict = None) -> int:
    """
    >>> factorials_3(1)
    1
    >>> factorials_3(5)
    120
    >>> factorials_3(10)
    3628800
    >>> factorials_3(10)
    3628800
    """
    if cache is None:
        cache = {}
    if n in cache:
        return cache[n]
    # cache[n] = functools.reduce(operator.mul, range(1, n+1))
    cache[n] = math.factorial(n)
    return cache[n]


def factorials_4(n: int, cache: dict = {}) -> int:
    """
    >>> factorials_4(1)
    1
    >>> factorials_4(5)
    120
    >>> factorials_4(10)
    3628800
    >>> factorials_4(10)
    3628800
    """
    try:
        return cache[n]
    except KeyError:
        cache[n] = functools.reduce(operator.mul, range(1, n+1))
        # cache[n] = math.factorial(n)
        return cache[n]


@functools.lru_cache(maxsize=None)
def factorials_5(n: int) -> int:
    """
    >>> factorials_5(1)
    1
    >>> factorials_5(5)
    120
    >>> factorials_5(10)
    3628800
    >>> factorials_5(10)
    3628800
    """
    # return functools.reduce(operator.mul, range(1, n+1))
    return math.factorial(n)





# print(min(timeit.timeit('factorials(random.randint(2, 16))', number=10000, globals=globals()) for __ in range(100)))
# 0.016193381000000118

# print(min(timeit.timeit('factorials_2(random.randint(2, 16))', number=10000, globals=globals()) for __ in range(100)))
# 0.016156021999999992

# print(min(timeit.timeit('factorials_3(random.randint(2, 16))', number=10000, globals=globals()) for __ in range(100)))
# 0.030370596000000027
# 0.019700634000000106 (math.factorial)

# print(min(timeit.timeit('factorials_4(random.randint(2, 16))', number=10000, globals=globals()) for __ in range(100)))
# 0.015959783999999977

# print(min(timeit.timeit('math.factorial(random.randint(2, 16))', number=10000, globals=globals()) for __ in range(100)))
# 0.016384693000000006

# print(min(timeit.timeit('factorials_5(random.randint(2, 16))', number=10000, globals=globals()) for __ in range(100)))
# 0.01523400900000027

# for _ in range(10000):
#     factorials_5(random.randint(2, 16))

# print(factorials_5.cache_info())








def memoize(func):
    """simplest memoizing decorator"""
    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return memoized


import time


def clock(func):
    def clocked(*args):
        t0 = time.time()
        result = func(*args)
        elapsed = time.time() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked


def clock_(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        name = func.__name__
        arg_lst = []
        if args:
            arg_lst.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            pairs = ['%s=%r' % (k, w) for k, w in sorted(kwargs.items())]
            arg_lst.append(', '.join(pairs))
        arg_str = ', '.join(arg_lst)
        print('[%0.8fs] %s(%s) -> %r ' % (elapsed, name, arg_str, result))
        return result
    return clocked


def memoize(fn, slot=None, maxsize=32):
    """Memoize fn: make it remember the computed value for any argument list.
    If slot is specified, store result in that slot of first argument.
    If slot is false, use lru_cache for caching the values."""
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        @functools.lru_cache(maxsize=maxsize)
        def memoized_fn(*args):
            return fn(*args)

    return memoized_fn



import functools
import profile


@functools.lru_cache(maxsize=None)
def fib(n):
    # from literateprograms.org
    # http://bit.ly/hlOQ5m
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    seq = []
    if n > 0:
        seq.extend(fib_seq(n - 1))
    seq.append(fib(n))
    return seq


if __name__ == '__main__':
    profile.run('print(fib_seq(20)); print()')


len(set(id(el) for el in objects))




def memoize_uw(func):
    func.cache = {}


def memoize(*args, **kw):
    if kw:  # frozenset is used to ensure hashability
        key = args, frozenset(kw.items())
    else:
        key = args
    if key not in func.cache:
        func.cache[key] = func(*args, **kw)
    return func.cache[key]
return functools.update_wrapper(memoize, func)



def _memoize(func, *args, **kw):
    if kw:  # frozenset is used to ensure hashability
        key = args, frozenset(kw.items())
    else:
        key = args
    cache = func.cache  # attribute added by memoize
    if key not in cache:
        cache[key] = func(*args, **kw)
    return cache[key]


def memoize(f):
    """
    A simple memoize implementation. It works by adding a .cache dictionary
    to the decorated function. The cache will grow indefinitely, so it is
    your responsibility to clear it, if needed.
    """
    from decorator import decorate
    f.cache = {}
    return decorate(f, _memoize)




def fib1(n):
    sys.setrecursionlimit(100000)
    assert n >= 0
    return n if n <= 1 else fib1(n - 1) + fib1(n - 2)

fib1 = lru_cache(maxsize=None)(fib1)
