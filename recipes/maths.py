# -*- coding: utf-8 -*-
import math
from functools import lru_cache
from typing import Iterable, Generator, List, Sequence, Union
import numpy as np

1.5e2  # 1.5 * 10**2
# 150.0

round(1000**(1 / 3))  # cubic root
# 10
abs(-1)
# 1
divmod(177, 10)  # (x // y, x % y)
# (17, 7)
pow(3, 4, 5)  # x**y mod m - Modular exponentiation
# 1
complex(1, 2)
# (1+2j)

float('inf')  # math.inf
float('-inf')  # -math.inf

(100 * 101) // 2  # n(n+1)/2 == sum 1..100 == sum(range(101))
# 5050
2**11 - 1  # 2^n+1-1 == sum 2^0..2^n == sum(2**p for p in range(n+1))
# 2047

(33 + 7 - 1) // 7  # ((m + n - 1) // n) - division with rounding up
# 5
(77 // 7) * 7 + 7  # ((n // m) * m + m) - top int divisible without remainder
# 84
(77 // 7) * 7 - 7  # ((n // m) * m - m) - bottom int divisible without remainder
# 70

3**200 % 50
# 1

3 / 9  # n/9 == 0.nnnnnnnnnnn
# 0.3333333333333333

math.gcd(100, 75)  # gcd
# 25

# Return True if the values a and b are close to each other and False otherwise.
math.isclose(1.000000002, 1.000000001)
# True
math.isclose(1.000000003, 1.000000001)
# False

# base-2 logarithm of x
x = 2
# -> float
math.log(x, 2.0)  # slow
math.log2(x)
# 1.0
# -> int
math.frexp(x)[1] - 1  # fast
x.bit_length() - 1  # faster
# 1


def digits(n: int) -> Generator[int, None, None]:
    # How to get the digits of an integer
    while n:
        yield n % 10
        n //= 10


def sum_digits(n: int) -> int:
    # Sum of all digits of a number
    return sum(digits(n))


def length_digits(n: int) -> int:
    # Number of digits in a number
    return sum(1 for _ in digits(n))


def median(numbers: Sequence[Union[int, float]]) -> float:
    half_size = len(numbers) // 2
    return sum(numbers[half_size-1:half_size+1]) / 2


def majority_element(arr: Sequence) -> int:
    return sorted(arr)[len(arr) // 2]


def moving_average(iterable, n=3):
    """
    http://en.wikipedia.org/wiki/Moving_average
    moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    """
    from collections import deque
    from itertools import islice
    it = iter(iterable)
    d = deque(islice(it, n - 1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / n


def rand():
    import random
    c = random.randint(1, 100000)
    a = c * random.randint(1, 100000)
    b = c * random.randint(1, 100000)
    return a, b


def permutations(n, k):
    """
    nPk

    >>> permutations(52, 2)
    2652
    """
    from math import factorial
    return factorial(n) // factorial(n - k)


def combinations(n, k):
    """
    nCk

    >>> combinations(52, 2)
    1326
    """
    from math import factorial
    return permutations(n, k) // factorial(k)


def powerset(iterable):
    """
    >>> [*powerset([1,2,3])]
    [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
    """
    from typing import Container
    from itertools import chain, combinations
    s = iterable if isinstance(iterable, Container) else [*iterable]
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def dot_product(vec1, vec2):
    from operator import mul
    return sum(map(mul, vec1, vec2))


def rotate_vec(vector: List[List[int]], angle: int) -> np.ndarray:
    """
    >>> rotate_vec([[1, 2], [3, 5]], 45)
    array([[-2.02738858, -3.20387365],
           [ 2.42686949,  4.32841699]])
    """
    mat = np.array([[np.cos(angle), -np.sin(angle)],
                    [np.sin(angle), np.cos(angle)]])
    return mat @ vector


def struct_inverse_sqrt(n: Union[int, float]) -> float:
    """
    https://en.wikipedia.org/wiki/Fast_inverse_square_root
    http://ajcr.net/fast-inverse-square-root-python/

    >>> struct_inverse_sqrt(0.15625)
    2.5254863388218056
    """
    from struct import pack, unpack
    threehalfs = 1.5
    x2 = n * 0.5
    y = n
    packed_y = pack('f', y)
    i = unpack('i', packed_y)[0]  # treat float's bytes as int
    i = 0x5f3759df - (i >> 1)  # arithmetic with magic number
    packed_i = pack('i', i)
    y = unpack('f', packed_i)[0]  # treat int's bytes as float
    y *= (threehalfs - (x2 * y * y))  # Newton's method
    return y


def tower_of_powers(n: int, powers: Iterable[int]) -> int:
    """
    https://en.wikipedia.org/wiki/Knuth%27s_up-arrow_notation
    https://en.wikipedia.org/wiki/Conway_chained_arrow_notation
    https://en.wikipedia.org/wiki/Tetration

    >>> tower_of_powers(2, [2, 2])
    16
    >>> tower_of_powers(3, [2, 2, 2])
    43046721
    >>> tower_of_powers(3, [3, 3])
    7625597484987
    """
    from functools import reduce
    return n**reduce(pow, powers)


def approx_pi2(n: int = 10000000) -> float:
    """
    https://en.wikipedia.org/wiki/Approximations_of_%CF%80

    >>> approx_pi2(1000)
    3.1406380562059946
    >>> approx_pi2()
    3.1415925580959025
    """
    from math import sqrt
    val = sum(1 / k**2 for k in range(1, n + 1))
    return sqrt(6 * val)


def a002024(n: int) -> list:
    """
    https://oeis.org/A002024

    >>> a002024(1)
    [1]
    >>> a002024(7)
    [1, 2, 2, 3, 3, 3, 4]
    """
    from itertools import chain, islice
    seq = chain.from_iterable(
        (i for _ in range(i)) for i in range(1, 100))
    return [*islice(seq, n)]


def a078633(n: int) -> int:
    """
    https://oeis.org/A078633

    >>> a078633(1)
    4
    >>> a078633(4)
    12
    >>> a078633(50)
    115
    """
    from math import ceil, sqrt
    return (2 * n) + ceil(2 * sqrt(n))


def a007913(n: int) -> int:
    """
    https://oeis.org/A007913

    >>> a007913(1)
    1
    >>> a007913(8)
    2
    >>> a007913(24)
    6
    """
    from sympy.ntheory.factor_ import core
    return core(n)


def is_square_free(n: int) -> bool:
    """
    https://en.wikipedia.org/wiki/Square-free_integer

    >>> is_square_free(1)
    True
    >>> is_square_free(4)
    False
    >>> is_square_free(46)
    True
    """
    from math import sqrt
    for i in range(2, round(sqrt(n)) + 1):
        if n % (i**2) == 0:
            return False
    return True


def lcm(a: int, b: int) -> int:
    """
    https://en.wikipedia.org/wiki/Least_common_multiple

    >>> lcm(4, 6)
    12
    >>> lcm(21, 6)
    42
    """
    from math import gcd
    return (a // gcd(a, b)) * b


def lcms(*numbers: int) -> int:
    """
    >>> lcms(8, 9, 21)
    504
    """
    from functools import reduce
    return reduce(lcm, numbers)


def fermat_number(n: int) -> int:
    """
    https://en.wikipedia.org/wiki/Fermat_number
    https://oeis.org/A000215

    >>> [fermat_number(i) for i in range(5)]
    [3, 5, 17, 257, 65537]
    """
    return 3 if n == 0 else (2 << ((2 << (n - 1)) - 1)) + 1  # 2**(2**n) + 1


@lru_cache(maxsize=None)
def factorial_lru(n: int) -> int:
    """
    https://en.wikipedia.org/wiki/Factorial
    sympy.factorial

    >>> factorial_lru(0)
    1
    >>> factorial_lru(5)
    120
    >>> factorial_lru(10)
    3628800
    """
    from math import factorial
    return factorial(n)


def factorials_gen(n: int) -> Generator[int, None, None]:
    """
    https://oeis.org/A000142

    >>> [*factorials_gen(1)]
    [1, 1]
    >>> [*factorials_gen(5)]
    [1, 1, 2, 6, 24, 120]
    >>> [*factorials_gen(10)]
    [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    """
    return (factorial_lru(i) for i in range(n + 1))


def wilson_primality_test(n: int) -> bool:
    """
    https://en.wikipedia.org/wiki/Wilson%27s_theorem

    >>> assert all(wilson_primality_test(i) for i in [2, 3, 5, 7, 11])
    >>> assert not all(wilson_primality_test(i) for i in [4, 6, 8, 9, 10])
    """
    return ((factorial_lru(n - 1) + 1) % n) == 0


def fermat_primality_test(n: int, k: int = 3) -> bool:
    """
    https://en.wikipedia.org/wiki/Fermat_primality_test

    >>> assert all(fermat_primality_test(i) for i in [2, 3, 5, 7, 11])
    >>> assert not all(fermat_primality_test(i) for i in [4, 6, 8, 9, 10])
    """
    from math import gcd
    from random import randrange
    for _ in range(k):
        random_num = randrange(1, n)
        if gcd(n, random_num) != 1 or pow(random_num, n - 1, n) != 1:
            return False
    return True


def primes_gen(n: int) -> Generator[int, None, None]:
    """
    https://oeis.org/A000040
    sympy.ntheory.isprime
    sympy.ntheory.primerange

    >>> [*primes_gen(31)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    >>> assert len([*primes_gen(2000)]) == 303
    """
    yield 2
    if n <= 1000:
        k = (n.bit_length() - 1) << 1
        yield from (p for p in range(3, n+1, 2) if fermat_primality_test(p, k))
    else:
        yield from (p for p in range(3, n+1, 2) if wilson_primality_test(p))


def fibonacci_gen(num: int) -> Generator:
    """
    >>> [*fibonacci_gen(10)]
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    """
    a = b = 1
    for _ in range(num):
        yield a
        a, b = b, a + b


def binomial_coefficient(n: int, k: int) -> float:
    """
    math.comb(n, k)
    scipy.special.binom(n, k)

    >>> binomial_coefficient(4, 2)
    6.0
    """
    res = 1.0
    for i in range(1, k + 1):
        res *= (n - i + 1) / i
    return res


def pascal_triangle(rows: int) -> list:
    """
    https://oeis.org/A007318

    >>> pascal_triangle(4)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    """
    res = [[1]]
    for _ in range(rows):
        row = res[-1]
        res.append([1, *map(sum, zip(row, row[1:])), 1])
    return res


def pascal_triangle_gen() -> Generator:
    """
    >>> p = pascal_triangle_gen()
    >>> [next(p) for _ in range(5)]
    [(1,), (1, 1), (1, 2, 1), (1, 3, 3, 1), (1, 4, 6, 4, 1)]
    """
    row = (1,)
    while True:
        yield row
        row = (1, *map(sum, zip(row, row[1:])), 1)
