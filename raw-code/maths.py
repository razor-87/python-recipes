# -*- coding: utf-8 -*-

num = 1.5e2    # == 1.5 * (10 ** 2)
num = 100_000_000   # Only >=3.6

# cubic root
round(x**(1/3))

from math import gcd
gcd(100, 75)
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

pow(x, y, m)  # x**y mod m
pow(3, 4, 5)
# 1


# integer quotient of division with rounding up
(m + n - 1) // n




import functools
functools.reduce(operator.mul, range(1, 11))  # math.factorial(10)
# 3628800






import warnings; warnings.simplefilter('ignore')  # Fix NumPy issues.

from numpy import array, cos, sin
def rotate(vector, angle):
    θ = angle
    mat = [[cos(θ), -sin(θ)],
           [sin(θ), cos(θ)]]
    mat = array(mat)
    return mat @ vector
