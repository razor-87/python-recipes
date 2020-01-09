# -*- coding: utf-8 -*-
# @Author: razor87
# @Date:   2019-10-01 18:10:45
# @Last Modified by:   razor87
# @Last Modified time: 2020-01-09 20:00:38

bin(0x7F)
# '0b1111111'

bin(int('010101', 2))
# '0b10101'

bin(~0b11111111)  # ~255 -> -256
# '-0b100000000'

bin(0xCA)
# '0b11001010'

bin(0xFF)
# '0b11111111' -> 255

bin(0xF)
# '0b1111' -> 15

bin(0x100)
# '0b100000000' -> 256

bin(0x80)
# '0b10000000' -> 128

bin(0x40)
# '0b1000000' -> 64

bin(10)[2:], len(bin(10)[2:])
# ('1010', 4)

bin(255)[2:], len(bin(255)[2:])
# ('11111111', 8)

bin(100).count('1')
# 3

(100).bit_length()
# 7

(0xFF00FF << 8) == (0xFF00FF * 2**8)  # (16711935 << 8) == (16711935 * 2**8)
# True

0b10101  # int('0b10101', 0)
# 21

0x100  # int('0x100', 16)
# 256

~0
# -1

0b100000000 - 0b100000001
# -1

0b_111_0101_0011
# 1875

hex(1_234_987)
# 0x12d82b

hex(9223372036854775807)  # sys.maxsize
# '0x7fffffffffffffff'

hex(0b0010), hex(0b0100), hex(0b1010)
# ('0x2', '0x4', '0xa')
bin(0x24A)
# '0b1001001010'

''.join(
    map(str, (
        0xCA >> 7,
        (0xCA >> 6) % 2,
        (0xCA >> 5) % 2,
        (0xCA >> 4) % 2,
        (0xCA >> 3) % 2,
        (0xCA >> 2) % 2,
        (0xCA >> 1) % 2,
        0xCA % 2,
    )))
# '11001010'

# n << b -> n * (2**b)
1 << 1  # 1 * (2**1)
# 2

# n >> b -> n // (2**b)
64 >> 2  # 64 // (2**2) -> 64 // 4
# 16

2 << 1  # 2**2 == 1 << 2
# 4 / 0b10 << 0b1 -> 0b100
(3 << 1) + 3  # 3**2
# 9 / (0b11 << 0b1) + 0b11 -> 0b1001
((3 & 1) << 3) | 1
# ((0b11 & 0b1) << 0b11) | 0b1 -> 0b1001
4 << 2  # 4**2 == 1 << 4 == 2 << 3
# 16
(5 << 2) + 5  # 5**2
# 25
(6 << 2) + (6 << 1)  # 6**2
# 36
(7 << 2) + (7 << 1) + 7  # 7**2
# 49
(8 << 3)  # 8**2 == 2**6 == 1 << 6 == 2 << 5
# 64
(9 << 3) + 9  # 9**2
# 81
(10 << 3) + (10 << 1)  # 10**2
# 100
(11 << 3) + (11 << 1) + 11  # 11**2
# 121

# a, b = 5, 10
# a ^= b -> (15, 5)
# b ^= a -> (15, 10)
# a ^= b -> (5, 10)


def add_by_bits(a, b):
    assert a >= 0 and b >= 0
    while b:
        carry = a & b
        a ^= b
        b = carry << 1
    return a


def add_by_bits_r(x, y):
    assert x >= 0 and y >= 0
    if not y:
        return x
    return add_by_bits_r(x ^ y, (x & y) << 1)


def is_div_by_17(n):
    # true for any n of the form 2**k + 1 like 5, 9, 17, 33...
    if n == 0 or n == 17:
        return True
    elif n < 17:
        return False
    return is_div_by_17((n >> 4) - (n & 15))


def divide(n, m):
    # XXX: Exact division only by powers of two
    return n >> (m.bit_length() - 1), n & (m - 1)  # quotient, remainder


def power_by_bits(a, b):
    result = 1
    while b:
        if b & 1:
            result *= a
        b >>= 1
        a *= a
    return result


def reverse_bits(x):
    inp_bits = bin(x)[2:]
    # return int(f"0b{inp_bits[::-1]}", 2)
    return f"0b{inp_bits} -> 0b{inp_bits[::-1]}"


def swap_bits(x, i, j):
    x_old = bin(x)
    low = (x >> i) & 1
    high = (x >> j) & 1
    if low ^ high:
        x ^= (1 << i) | (1 << j)
    return f"{x_old} -> {bin(x)}"


def bits_rotate_left(byte):
    bit = byte & 0x80
    byte <<= 1
    if bit:
        byte |= 0x01
    byte &= 0xFF
    return byte


def bits_rotate_right(byte):
    byte &= 0xFF
    bit = byte & 0x01
    byte >>= 1
    if bit:
        byte |= 0x80
    return byte


def number_of_set_bits(i):
    # https://en.wikipedia.org/wiki/Hamming_weight
    assert 0 <= i < 0x100000000
    i -= ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24


def find_position_of_msb(n):
    high = 31
    low = 0
    while (high - low) > 1:
        mid = (high + low) // 2
        mask_high = (1 << high) - (1 << mid)
        if (mask_high & n) > 0:
            low = mid
        else:
            high = mid
    print(f"{n} : MSB at {low}. Between {pow(2, low)} and {pow(2, low + 1)}")


def rol(n, rotations=1, width=8):
    """
    Return a given number of bitwise left rotations of an integer n,
    for a given bit field width.

    """
    rotations %= width
    if rotations < 1:
        return n
    n &= mask(width)  # Should it be an error to truncate here?
    return ((n << rotations) & mask(width)) | (n >> (width - rotations))


def ror(n, rotations=1, width=8):
    """
    Return a given number of bitwise right rotations of an integer n,
    for a given bit field width.

    """
    rotations %= width
    if rotations < 1:
        return n
    n &= mask(width)
    return (n >> rotations) | ((n << (width - rotations)) & mask(width))


def sum_powers_of_two(n: int) -> int:
    """
    >>> sum_powers_of_two(5)
    63
    >>> sum_powers_of_two(10) == 2**11 - 1
    True
    """
    return (2 << n) - 1


def is_power_of_two(n: int) -> bool:
    """
    >>> is_power_of_two(1024)
    True
    >>> is_power_of_two(5)
    False
    """
    return n & (n - 1) == 0


def invert_bits(b: int) -> int:
    """
    >>> bin(1 << invert_bits(0b1100101100101).bit_length())
    '0b100000000000'
    """
    return b ^ ((1 << b.bit_length()) - 1)


def low_nibble(b: int) -> int:
    """
    >>> bin(low_nibble(0b101010))
    '0b1010'
    """
    return b & 0x0F


def high_nibble(b: int) -> int:
    """
    >>> bin(high_nibble(0b10010000))
    '0b1001'
    """
    return (b >> 4) & 0x0F


def mask(n: int) -> int:
    """
    Return a bitmask of length n.

    >>> bin(mask(5))
    '0b11111'
    """
    return (2 << (n - 1)) - 1 if n >= 0 else 0


def is_even_or_odd(i: int) -> bool:
    """
    Check if the integer is even or odd.

    >>> is_even_or_odd(0)
    True
    >>> is_even_or_odd(1)
    False
    >>> is_even_or_odd(2)
    True
    >>> is_even_or_odd(101)
    False
    """
    return i & 1 == 0


def is_nth_bit_is_set(i: int, n: int) -> bool:
    """
    Test if the n-th bit is set.

    >>> is_nth_bit_is_set(0b1010, 0)
    False
    >>> is_nth_bit_is_set(0b1010, 1)
    True
    >>> is_nth_bit_is_set(0b1010, 3)
    True
    >>> is_nth_bit_is_set(0b1010, 5)
    False
    """
    return bool(i & (1 << n))


def set_nth_bit(i: int, n: int) -> int:
    """
    Set the n-th bit.

    >>> bin(set_nth_bit(0b100000, 0))
    '0b100001'
    """
    return i | (1 << n)


def unset_nth_bit(i: int, n: int) -> int:
    """
    Unset the n-th bit.

    >>> bin(unset_nth_bit(0b111111, 0))
    '0b111110'
    """
    return i & ~(1 << n)


def toggle_nth_bit(i: int, n: int) -> int:
    """
    Toggle the n-th bit.

    """
    return i ^ (1 << n)


def turn_off_rightmost_bit(i: int) -> int:
    """
    Turn off the rightmost 1-bit.

    """
    return i & (i - 1)


def isolate_rightmost_bit(i: int) -> int:
    """
    Isolate the rightmost 1-bit.

    """
    return i & (-i)


def right_propagate_rightmost_bit(i: int) -> int:
    """
    Right propagate the rightmost 1-bit.

    """
    return i | (i - 1)


def isolate_rightmost_0_bit(i: int) -> int:
    """
    Isolate the rightmost 0-bit.

    """
    return ~i & (i + 1)


def turn_rightmost_0_bit(i: int) -> int:
    """
    Turn on the rightmost 0-bit.

    """
    return i | (i + 1)
