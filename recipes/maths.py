# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-10-04 19:52:29
# @Last Modified by:   razor87
# @Last Modified time: 2019-10-21 11:12:44
import math

1.5e2  # == 1.5 * (10 ** 2)

(13).__add__(2)
# 15

round(x**(1 / 3))  # cubic root

# n(n+1)/2
(100 * 101) // 2  # sum 1..100
# 5050
sum(range(101))
# 5050


divmod(177, 10)  # (x // y, x % y)
# (17, 7)

pow(3, 4, 5)  # x**y mod m - Modular exponentiation
# 1

3**200 % 50
# 1

(33 + 7 - 1) // 7  # (m + n - 1) // n - division with rounding up
# 5

3 / 9  # 0.nnnnnnnnnnn
# 0.3333333333333333

n, k = 52, 2
permutations = math.factorial(n) // math.factorial(n - k)  # nPk
# 2652
combinations = permutations // math.factorial(k)  # nCk
# 1326

math.gcd(100, 75)  # gcd
# 25

# Return True if the values a and b are close to each other and False otherwise.
math.isclose(a, b, rel_tol=1e-09, abs_tol=0.0)

# base-2 logarithm of x
# slow
math.log(x, 2.0)  # -> float
math.log2(x)  # -> float
# fast
math.frexp(x)[1] - 1  # -> int
# faster
n.bit_length() - 1  # -> int


def last_digit(n):
    # Get the last digit of a number
    return n % 10


def digits(n):
    # How to get the digits of an integer
    while n:
        yield n % 10
        n /= 10


def sum_digits(n):
    # Sum of all digits of a number
    s = 0
    while n:
        s += n % 10
        n /= 10
    return s


def length_digits(n):
    # Number of digits in a number
    s = 0
    while n:
        s += 1
        n /= 10
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


def rotate(vector, angle):
    from warnings import simplefilter
    simplefilter('ignore')  # Fix NumPy issues.
    from numpy import array, cos, sin
    θ = angle
    mat = [[cos(θ), -sin(θ)],
           [sin(θ), cos(θ)]]
    mat = array(mat)
    return mat @ vector


def struct_inverse_sqrt(number):
    from struct import pack, unpack
    threehalfs = 1.5
    x2 = number * 0.5
    y = number
    packed_y = pack('f', y)
    i = unpack('i', packed_y)[0]  # treat float's bytes as int
    i = 0x5f3759df - (i >> 1)            # arithmetic with magic number
    packed_i = pack('i', i)
    y = unpack('f', packed_i)[0]  # treat int's bytes as float
    y = y * (threehalfs - (x2 * y * y))  # Newton's method
    return y


def tower_of_powers(arr):
    """
    >>> tower_of_powers((3, 2, 2, 2))
    43046721
    >>> tower_of_powers((2, 2, 2, 2, 0))
    16
    """
    from functools import reduce
    return reduce(lambda x, y: y**x, reversed(arr))


def approx_pi2(n=10000000):
    val = sum(1 / k**2 for k in range(1, n + 1))
    return (6 * val)**0.5


def a078633(n):
    """
    https://oeis.org/A078633
    Smallest number of sticks of length 1 needed to construct n squares
    with sides of length 1
    """
    from math import ceil, sqrt
    return (2 * n) + ceil(2 * sqrt(n))


def lcm(a, b):
    """
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