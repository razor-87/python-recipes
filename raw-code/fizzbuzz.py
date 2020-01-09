# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-12-20 16:41:20
# @Last Modified by:   razor87
# @Last Modified time: 2020-01-09 20:08:21
from typing import List, Union


def fizzbuzz(arr: List[int]) -> List[Union[str, int]]:
    """
    >>> fizzbuzz([30, 42, 28, 50, 15])
    ['fizzbuzz', 'fizz', 28, 'buzz', 'fizzbuzz']
    """
    ret = [
        ''.join((('', 'fizz')[n % 3 == 0], ('', 'buzz')[n % 5 == 0])) or n
        for n in arr
    ]
    return ret
