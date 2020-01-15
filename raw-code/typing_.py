# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2020-01-15 11:36:27
# @Last Modified by:   razor87
# @Last Modified time: 2020-01-15 20:24:18
from typing import Generic, overload, TypeVar, Tuple

T = TypeVar('T')


class Vector(Generic[T]):
    def __init__(self, x: T, y: T) -> None:
        self.x = x
        self.y = y

    def translate(self, dx: T, dy: T) -> None:
        self.x += dx  # error: Unsupported left operand type for + ("T")
        self.y += dy  # error: Unsupported left operand type for + ("T")


@overload
def process(response: None) -> None: ...

@overload
def process(response: int) -> Tuple[int, str]: ...

@overload
def process(response: bytes) -> str: ...

def process(response): ...  # actual implementation
