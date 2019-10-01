# -*- coding: utf-8 -*-
from typing import Iterable, Union


# @profile
def linear_search(n: int, arr: Iterable[int], i: int = 0) -> Union[int, str]:
    x = (*arr, n)
    while x[i] != n:
        i += 1
    if i < len(x) - 1:
        del x
        return f'i: {i}, n: {n}'
    del x
    return -1


if '__name__' == '__main__':
    # arr = [5, 3, 7, 9, 4]
    # import random
    # arr = (random.randint(0, 100) for _ in range(100))
    arr = range(1000)
    linear_search(9, arr)
    linear_search(7, arr)
    linear_search(10, arr)
    linear_search(0, arr)
    linear_search(1010, arr)
    linear_search(2550, arr)
    linear_search(1110, arr)
    linear_search(1000, arr)
