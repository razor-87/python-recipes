# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-10-04 19:52:29
# @Last Modified by:   razor87
# @Last Modified time: 2020-01-15 21:21:42
import math
from typing import Iterable

1.5e2  # 1.5 * 10**2
# 150.0

(13).__add__(2)
# 15

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

n, k = 52, 2
permutations = math.factorial(n) // math.factorial(n - k)  # nPk
# 2652
combinations = permutations // math.factorial(k)  # nCk
# 1326

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


def last_digit(n: int) -> int:
    # Get the last digit of a number
    return n % 10


def digits(n):
    # How to get the digits of an integer
    while n:
        yield n % 10
        n /= 10


def sum_digits(n: int) -> int:
    # Sum of all digits of a number
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


def length_digits(n: int) -> int:
    # Number of digits in a number
    s = 0
    while n:
        s += 1
        n //= 10
    return s


def reverse_digits(n):
    # Reverse digits in a number
    s = 0
    k = 10**(length_digits(n) - 1)
    while n:
        s += k * (n % 10)
        n /= 10
        k /= 10
    return s


def rotate_vec(vector, angle):
    """
    >>> rotate_vec([[1, 2], [3, 5]], 45)
    array([[-2.02738858, -3.20387365],
           [ 2.42686949,  4.32841699]])
    """
    from numpy import array, cos, sin
    mat = array([[cos(angle), -sin(angle)], [sin(angle), cos(angle)]])
    return mat @ vector


def struct_inverse_sqrt(number):
    """
    https://en.wikipedia.org/wiki/Fast_inverse_square_root
    http://ajcr.net/fast-inverse-square-root-python/

    """
    from struct import pack, unpack
    threehalfs = 1.5
    x2 = number * 0.5
    y = number
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


tower_of_powers(3, [3, 3])


def approx_pi2(n=10000000):
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


def lcm(a, b):
    """
    https://en.wikipedia.org/wiki/Least_common_multiple

    >>> lcm(4, 6)
    12
    >>> lcm(21, 6)
    42
    """
    from math import gcd
    return (a // gcd(a, b)) * b


def lcms(*numbers):
    """
    >>> lcms(8, 9, 21)
    504
    """
    from functools import reduce
    return reduce(lcm, numbers)


def primes():
    """
    https://en.wikipedia.org/wiki/Wilson%27s_theorem

    >>> from itertools import takewhile
    >>> [*takewhile(lambda x: x <= 31, primes())]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    """
    from math import factorial
    p = 2
    while True:
        com = (factorial(p - 1) + 1) % p
        if com == 0:
            yield p
        p += 1
