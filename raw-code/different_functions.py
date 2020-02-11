# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-09-29 19:22:37
# @Last Modified by:   razor87
# @Last Modified time: 2020-02-11 20:07:06


def array_shift(data, shift):
    # left rotation
    from collections import deque
    items = deque(data)
    items.rotate(-shift)
    return items


def find_idx(required_el, lst):
    if required_el in {*lst}:
        return lst.index(required_el)


def majority_element(arr: list):
    arr.sort()
    return arr[len(arr)//2]


def pop_append(data: list, shift: int):
    for _ in range(shift):
        data.append(data.pop(0))
    return data


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


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


def int_from_bytes(xbytes: bytes) -> int:
    return int.from_bytes(xbytes, 'big')


def int_to_bytes_sign(i: int, *, signed: bool = False) -> bytes:
    length = ((i + ((i * signed) < 0)).bit_length() + 7 + signed) // 8
    return i.to_bytes(length, byteorder='big', signed=signed)


def bytes_to_int_sign(b: bytes, *, signed: bool = False) -> int:
    return int.from_bytes(b, byteorder='big', signed=signed)


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
    """
    Random selection from itertools.product(*args, **kwds)

    """
    from random import choice
    pools = [tuple(pool) for pool in args] * repeat
    return tuple(choice(pool) for pool in pools)


def random_permutation(iterable, r=None):
    """
    Random selection from itertools.permutations(iterable, r)

    """
    from random import sample
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(sample(pool, r))


def random_combination(iterable, r):
    """
    Random selection from itertools.combinations(iterable, r)

    """
    from random import sample
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(sample(range(n), r))
    return tuple(pool[i] for i in indices)


def random_combination_with_replacement(iterable, r):
    """
    Random selection from itertools.combinations_with_replacement(iterable, r)

    """
    from random import randrange
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(randrange(n) for i in range(r))
    return tuple(pool[i] for i in indices)


def countdown(num_sec=3):
    from time import sleep
    for countdown in range(num_sec, 0, -1):
        if countdown > 0:
            print(countdown, end='...')
            sleep(1)
        else:
            print('Go!')


def progress(width=30):
    from time import sleep
    for percent in range(101):
        left = width * percent // 100
        right = width - left
        print('\r[', '#' * left, ' ' * right, ']',
              f' {percent:.0f}%',
              sep='', end='', flush=True)
        sleep(0.1)


def shorthand_dict(names):
    """
    >>> context = {"user_id": 42, "user_ip": "1.2.3.4"}
    >>> mode, action_type = "force", 7
    >>> shorthand_dict(["context", "mode", "action_type"])
    {'context': {'user_id': 42, 'user_ip': '1.2.3.4'},
    ... 'mode': 'force', 'action_type': 7}
    """
    from inspect import currentframe
    lcls = currentframe().f_back.f_locals
    return {k: lcls[k] for k in names}


def string_validators(string: str) -> list:
    """
    >>> string_validators('qA2')
    [True, True, True, True, True]
    >>> string_validators('123')
    [True, False, True, False, False]
    """
    dict_methods = {
        'isalnum': (char.isalnum() for char in string),
        'isalpha': (char.isalpha() for char in string),
        'isdigit': (char.isdigit() for char in string),
        'islower': (char.islower() for char in string),
        'isupper': (char.isupper() for char in string),
    }
    return [*map(any, dict_methods.values())]
