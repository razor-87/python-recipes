# -*- coding: utf-8 -*-
import math

1.5e2    # == 1.5 * (10 ** 2)
100_000_000   # Only >=3.6

# cubic root
round(x**(1/3))

math.gcd(100, 75)  # gcd
# 25

# n(n+1)/2
(100 * 101) // 2  # sum 1..100
# 5050
sum(range(101))
# 5050

t = (20, 8)
divmod(*t)

divmod(x, y)  # (x // y, x % y)
divmod(177, 10)
# (17, 7)

pow(x, y, m)  # x**y mod m - Modular exponentiation
pow(3, 4, 5)
# 1


3**200 % 50
# 1



# integer quotient of division with rounding up
(m + n - 1) // n

n / 9
# 0.nnnnnnnnnnn




n, k = 52, 2
permutations = math.factorial(n) // math.factorial(n - k)  # nPk
# 2652
combinations = permutations // math.factorial(k)  # nCk
# 1326



# Return True if the values a and b are close to each other and False otherwise.
math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)


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
    import warnings
    warnings.simplefilter('ignore')  # Fix NumPy issues.
    from numpy import array, cos, sin
    θ = angle
    mat = [[cos(θ), -sin(θ)],
           [sin(θ), cos(θ)]]
    mat = array(mat)
    return mat @ vector


def struct_inverse_sqrt(number):
    import struct
    threehalfs = 1.5
    x2 = number * 0.5
    y = number
    packed_y = struct.pack('f', y)
    i = struct.unpack('i', packed_y)[0]  # treat float's bytes as int
    i = 0x5f3759df - (i >> 1)            # arithmetic with magic number
    packed_i = struct.pack('i', i)
    y = struct.unpack('f', packed_i)[0]  # treat int's bytes as float
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
    return reduce(lambda x, y: y**x, reversed((3, 2, 2, 2)))


def approx_pi2(n=10000000):
    val = sum(1/k**2 for k in range(1, n+1))
    return (6 * val)**0.5
