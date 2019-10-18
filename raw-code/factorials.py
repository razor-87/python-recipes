# -*- coding: utf-8 -*-
import collections
import functools
import profile
import math
import operator
import random
import time
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


def fac(n):
    return 1 if n == 1 else fac(n-1)*n
