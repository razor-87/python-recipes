# -*- coding: utf-8 -*-

bin(0xF)
# '0b1111' -> 15

bin(0x10)
# '0b10000' -> 16

bin(0x3f)
# '0b111111' -> 63

bin(0x40)
# '0b1000000' -> 64

bin(0x7F)
# '0b1111111' -> 127

bin(0x80)
# '0b10000000' -> 128

bin(0xFF)
# '0b11111111' -> 255

bin(0x100)
# '0b100000000' -> 256

bin(~0xFF)  # ~255
# '-0b100000000' -> -256

(100).bit_length()
# 7

(0xFF00FF << 8) == (0xFF00FF * 2**8)  # (16711935 << 8) == (16711935 * 2**8)
# True

hex(1_234_987)
# 0x12d82b

hex(9223372036854775807)  # sys.maxsize
# '0x7fffffffffffffff'

hex(0b0010), hex(0b0100), hex(0b1010)
# ('0x2', '0x4', '0xa')

1 << 1  # n << i -> n * (2**i)
# 2

64 >> 2  # n >> i -> n // (2**i)
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


def format_to_8_bit(n: int) -> str:
    """
    >>> format_to_8_bit(10)
    '00001010'
    """
    bits = (n % 2,
            (n >> 1) % 2,
            (n >> 2) % 2,
            (n >> 3) % 2,
            (n >> 4) % 2,
            (n >> 5) % 2,
            (n >> 6) % 2,
            n >> 7)
    return "{7}{6}{5}{4}{3}{2}{1}{0}".format(*bits)


def reverse_bits(n: int) -> int:
    """
    >>> bin(reverse_bits(0b10001111))
    '0b11110001'
    """
    return int(format(n, 'b')[::-1], 2)


def count_bits_set(n: int) -> int:
    """
    >>> count_bits_set_fast(0b101010101)
    5
    >>> count_bits_set_fast(2 << 63)
    1
    >>> count_bits_set_fast((2 << 63) - 1)
    64
    """
    return format(n, 'b').count('1')


def count_bits_set_fast(n: int) -> int:
    """
    https://en.wikipedia.org/wiki/Hamming_weight

    >>> count_bits_set_fast(0b101010101)
    5
    >>> count_bits_set_fast(2 << 63)
    1
    >>> count_bits_set_fast((2 << 63) - 1)
    64
    """
    if 0 <= n < 0x100000000:
        n -= ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        return (((n + (n >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24
    return count_bits_set(n)


def count_bits_set_kernighan(n: int) -> int:
    """
    https://graphics.stanford.edu/~seander/bithacks.html#CountBitsSetKernighan

    >>> count_bits_set_kernighan(0b101010101)
    5
    >>> count_bits_set_kernighan(2 << 63)
    1
    >>> count_bits_set_kernighan((2 << 63) - 1)
    64
    """
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c


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


def is_even_or_odd(n: int) -> bool:
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
    return n & 1 == 0


def is_nth_bit_is_set(n: int, i: int) -> bool:
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
    return bool(n & (1 << i))


def twos_complement(n: int) -> int:
    """
    https://en.wikipedia.org/wiki/Two%27s_complement

    >>> bin(twos_complement(111))
    '0b10000'
    >>> bin(twos_complement(256))
    '0b11111111'
    """
    return ~n + (1 << n.bit_length())


def invert_bits(n: int) -> int:
    """
    >>> bin(0b1100101100101 ^ invert_bits(0b1100101100101))
    '0b1111111111111'
    """
    return n ^ ((1 << n.bit_length()) - 1)


def low_nibble(n: int) -> int:
    """
    >>> bin(low_nibble(0b101010))
    '0b1010'
    """
    return n & 0x0F


def high_nibble(n: int) -> int:
    """
    >>> bin(high_nibble(0b10010000))
    '0b1001'
    """
    return (n >> 4) & 0x0F


def mask(n: int) -> int:
    """
    Return a bitmask of length n.

    >>> bin(mask(5))
    '0b11111'
    """
    return (2 << (n - 1)) - 1 if n >= 0 else 0


def set_nth_bit(n: int, i: int) -> int:
    """
    Set the n-th bit.

    >>> bin(set_nth_bit(0b100000, 0))
    '0b100001'
    >>> bin(set_nth_bit(0b100001, 0))
    '0b100001'
    """
    return n | (1 << i)


def unset_nth_bit(n: int, i: int) -> int:
    """
    Unset the n-th bit.

    >>> bin(unset_nth_bit(0b11111111, 0))
    '0b11111110'
    >>> bin(unset_nth_bit(0b11111110, 0))
    '0b11111110'
    """
    return n & ~(1 << i)


def toggle_nth_bit(n: int, i: int) -> int:
    """
    Toggle the n-th bit.

    >>> bin(toggle_nth_bit(0b10000001, 0))
    '0b10000000'
    >>> bin(toggle_nth_bit(0b10000001, 3))
    '0b10001001'
    """
    return n ^ (1 << i)


def turn_off_rightmost_bit(n: int) -> int:
    """
    Turn off the rightmost 1-bit.

    >>> bin(turn_off_rightmost_bit(0b11111100))
    '0b11111000'
    """
    return n & (n - 1)


def isolate_rightmost_bit(n: int) -> int:
    """
    Isolate the rightmost 1-bit.

    >>> bin(isolate_rightmost_bit(0b11111000))
    '0b1000'
    """
    return n & (-n)


def turn_rightmost_0_bit(n: int) -> int:
    """
    Turn on the rightmost 0-bit.

    >>> bin(turn_rightmost_0_bit(0b11110001))
    '0b11110011'
    """
    return n | (n + 1)


def isolate_rightmost_0_bit(n: int) -> int:
    """
    Isolate the rightmost 0-bit.

    >>> bin(isolate_rightmost_0_bit(0b10000111))
    '0b1000'
    """
    return ~n & (n + 1)


def right_propagate_rightmost_bit(n: int) -> int:
    """
    Right propagate the rightmost 1-bit.

    >>> bin(right_propagate_rightmost_bit(0b10010000))
    '0b10011111'
    """
    return n | (n - 1)
