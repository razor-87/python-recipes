# -*- coding: utf-8 -*-
import math
import operator
import random
import timeit

NUMS = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 200, 256, 500, 1000, 5000, 10000, 15000,
    50000, 150_000, 500_000
]


def square_root_bi(x, epsilon=0.01):
    low = 0
    high = max(1, x)
    ans = (high + low) / 2
    while abs(ans**2 - x) >= epsilon:
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans


def newton_sqrt(n):
    approx = 0.5 * n
    better = 0.5 * (approx + n / approx)
    while better != approx:
        approx = better
        better = 0.5 * (approx + n / approx)
    return approx


def square_root_nr(x, epsilon=0.01):
    # Newton-Raphson for square root
    guess = x / 2
    diff = guess * guess - x
    while abs(diff) >= epsilon:
        guess = guess - diff / (2 * guess)
        diff = guess * guess - x
    # print('Square root of', x, 'is about', guess)
    return guess


def sqrt_random(x, epsilon=0.01):
    assert x > 0
    bound_lower = 1
    bound_upper = x * 0.25 + 1
    # times = 0
    while True:
        guess = random.uniform(bound_lower, bound_upper)
        diff = guess * guess - x
        # times += 1
        # print((f"times: {times} | guess: {guess} | diff: {diff} | "
        #        f"bound_lower: {bound_lower} | bound_upper: {bound_upper}"))
        if (abs(diff) <= epsilon) or (bound_upper - bound_lower <= epsilon * 2):
            # print(f"math.sqrt({x}) = {round(guess, 2)}\n")
            return guess
        if diff > 0:
            bound_upper = guess
        else:
            bound_lower = guess


def newton_sqrt_isclose(n, verbose=False):
    guess = n / 2
    while True:
        if verbose:
            print('guess ->', guess)
        better_guess = (guess + n / guess) / 2
        if math.isclose(guess, better_guess):
            return better_guess
        guess = better_guess


# def compare(fs, args=NUMS):
#     from matplotlib import pyplot as plt
#     for f in fs:
#         plt.plot(args, [(timeit.timeit(str(f(arg)), number=100000)) * 10000
#                         for arg in args],
#                  label=f.__name__)
#     plt.xlim(1, args[-1])
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# compare([square_root_bi, sqrt_random, square_root_nr, newton_sqrt,
#          math.sqrt, newton_sqrt_isclose])


def rand():
    c = random.randint(1, 100000)
    a = c * random.randint(1, 100000)
    return a


print(
    'square_root_bi: ',
    operator.add(
        timeit.timeit('square_root_bi(NUMS[random.randint(0, len(NUMS)-1)])',
                      number=10000,
                      globals=globals()),
        timeit.timeit('square_root_bi(rand())',
                      number=10000, globals=globals()) / 2))
print(
    'sqrt_random: ',
    operator.add(
        timeit.timeit('sqrt_random(NUMS[random.randint(0, len(NUMS)-1)])',
                      number=10000,
                      globals=globals()),
        timeit.timeit('sqrt_random(rand())',
                      number=10000, globals=globals()) / 2))
print(
    'newton_sqrt_isclose: ',
    operator.add(
        timeit.timeit('newton_sqrt_isclose(NUMS[random.randint(0, len(NUMS)-1)])',
                      number=10000,
                      globals=globals()),
        timeit.timeit('newton_sqrt_isclose(rand())',
                      number=10000,
                      globals=globals()) / 2))
print(
    'square_root_nr: ',
    operator.add(
        timeit.timeit('square_root_nr(NUMS[random.randint(0, len(NUMS)-1)])',
                      number=10000,
                      globals=globals()),
        timeit.timeit('square_root_nr(rand())',
                      number=10000, globals=globals()) / 2))
print(
    'newton_sqrt: ',
    operator.add(
        timeit.timeit('newton_sqrt(NUMS[random.randint(0, len(NUMS)-1)])',
                      number=10000,
                      globals=globals()),
        timeit.timeit('newton_sqrt(rand())',
                      number=10000, globals=globals()) / 2))
print(
    '**0.5: ',
    operator.add(
        timeit.timeit('round(NUMS[random.randint(0, len(NUMS)-1)]**0.5)',
                      number=10000,
                      globals=globals()),
        timeit.timeit('round(rand()**0.5)',
                      number=10000, globals=globals()) / 2))
print(
    'math.sqrt: ',
    operator.add(
        timeit.timeit('math.sqrt(NUMS[random.randint(0, len(NUMS)-1)])',
                      number=10000,
                      globals=globals()),
        timeit.timeit('math.sqrt(rand())',
                      number=10000, globals=globals()) / 2))
