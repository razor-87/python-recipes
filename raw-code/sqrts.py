# -*- coding: utf-8 -*-
"""
sqrt_random         : 0.244644
i_sqrt              : 0.057472
sqrt_newton         : 0.054136
i_sqrt_             : 0.039157
**0.5               : 0.031894
math.sqrt           : 0.027638
"""
import math
import random
import timeit

NUMS = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200, 256, 500, 1000, 5000, 10000, 15000,
    50000, 150_000, 500_000
]

sqrts = {
    "sqrt_random": ('sqrt_random(NUMS[random.randint(0, len(NUMS)-1)])',
                    'sqrt_random(rand())'),
    "i_sqrt":
    ('i_sqrt(NUMS[random.randint(0, len(NUMS)-1)])', 'i_sqrt(rand())'),
    "sqrt_newton": ('sqrt_newton(NUMS[random.randint(0, len(NUMS)-1)])',
                    'sqrt_newton(rand())'),
    "i_sqrt_":
    ('i_sqrt_(NUMS[random.randint(0, len(NUMS)-1)])', 'i_sqrt_(rand())'),
    "**0.5":
    ('round(NUMS[random.randint(0, len(NUMS)-1)]**0.5)', 'round(rand()**0.5)'),
    "math.sqrt":
    ('math.sqrt(NUMS[random.randint(0, len(NUMS)-1)])', 'math.sqrt(rand())')
}


def sqrt_random(x, epsilon=0.01):
    assert x > 0
    bound_low = 1
    bound_up = x * 0.25 + 1
    while True:
        guess = random.uniform(bound_low, bound_up)
        diff = guess * guess - x
        if (abs(diff) <= epsilon) or (bound_up - bound_low <= epsilon * 2):
            return guess
        if diff > 0:
            bound_up = guess
        else:
            bound_low = guess


def sqrt_newton(n):
    """Newton-Raphson for square root"""
    approx = 0.5 * n
    better = 0.5 * (approx + n / approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + n / approx)
    return approx


def i_sqrt(n):
    i = n.bit_length() >> 1  # i = floor( (1 + floor(log_2(n))) / 2 )
    m = 1 << i  # m = 2^i
    #
    # Fact: (2^(i + 1))^2 > n, so m has at least as many bits
    # as the floor of the square root of n.
    #
    # Proof: (2^(i+1))^2 = 2^(2i + 2) >= 2^(floor(log_2(n)) + 2)
    # >= 2^(ceil(log_2(n) + 1) >= 2^(log_2(n) + 1) > 2^(log_2(n)) = n. QED.
    #
    while m * m > n:
        m >>= 1
        i -= 1
    for k in range(i - 1, -1, -1):
        x = m | (1 << k)
        if x * x <= n:
            m = x
    return m


def i_sqrt_(n):
    # if not isinstance(n, int):
    #     raise TypeError('an int is required')
    # if n < 0:
    #     raise ValueError('math domain error')
    guess = (n >> n.bit_length() // 2) + 1
    result = (guess + n // guess) // 2
    while abs(result - guess) > 1:
        guess = result
        result = (guess + n // guess) // 2
    while result * result > n:
        result -= 1
    return result


def rand():
    c = random.randint(1, 100000)
    a = c * random.randint(1, 100000)
    return a


def mean(*args):
    return sum(args) / len(args)


def timeit_(param):
    return timeit.timeit(param, number=10000, globals=globals())


def main():
    for k, v in sqrts.items():
        print(f"{k:<20}: {mean(*(timeit_(p) for p in v)):>7f}")


if __name__ == '__main__':
    main()
