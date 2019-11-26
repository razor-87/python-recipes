# -*- coding: utf-8 -*-
import binascii
import re
from string import ascii_lowercase, digits, punctuation
from typing import List



str.encode()  # text/unicode -> bytes/utf-8
bytes.decode()  # bytes/utf-8 -> text/unicode

bytes("hello", "ascii")
# b'hello'

bytes.hex()

ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'
punctuation
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

ord('f')
# 102

chr(102)
# 'f'

ascii()

binascii.hexlify(data)

word.strip('.,!').lower()

''.swapcase()
"-".join(s.split())

# Building a string
s = ''.join(f(x) for x in l)

''.join(reversed('TURBO'))

'_'.join('hello')
# 'h_e_l_l_o'

print('\n'.join(['0', '1', '2']))
# 0
# 1
# 2

''.join(reversed('aaabbb'))
# bbbaaa
''.join(reversed('aabbaa')) == 'aabbaa'
# True


s.split('', 1)
s.rsplit()
str.splitlines()

"111".zfill(10)
# '0000000111'

example_string = r'File on disk C:\\'   # Raw string

word = 'eeeee'
print(word.count('e'))    # 5

"2017".isdigit()    # True

"3.14" in "3.1415926"   # True

# Only >=3.6
# grouping decimal numbers by thousands
one_million = 1_000_000

# grouping hexadecimal addresses by words
addr = 0xCAFE_F00D

# grouping bits into nibbles in a binary literal
flags = 0b_0011_1111_0100_1110

# same, for string conversions
flags = int('0b_1111_0000', 2)


# Only >=3.6
word = "word"
f"{word}"

num = 2 / 3
f"{num:.3f}"
# 0.667

a, b = 10, 20
f"The sum of the values is {a + b}."

f"{0.1:.25f}"
f"{0.1.as_integer_ratio()[0]/0.1.as_integer_ratio()[1]:.25f}"
# 0.1000000000000000055511151

0.1.as_integer_ratio()
# (3602879701896397, 36028797018963968)

f"{42:10d}"
# '        42'

f"{100000000:,}"
# '100,000,000'

f"{100:b}"
# '1100100'

f"{100:x}"
# '64'

f"{100:o}"
# '144'

f"{100:e}"
# '1.000000e+02'

f"{.10:.0%}"
# '10%'

f"{100:+}"
# '+100'


"{0}".format("word")
"{word}".format(word="word")

width = len("{0:b}".format(5))
"{0:{w}n} {0:{w}o} {0:{w}X} {0:{w}b}".format(5, w=width)
f"{5:{width}n} {5:{width}o} {5:{width}X} {5:{width}b}"

foo, bar = "foo", "bar"
"{0}{1}".format(foo, bar)  # It is better
"{foo}{bar}".format(foo=foo, bar=bar)  # It is best
"{1}{0}".format(*(foo, bar))
# 'barfoo'


s = 'abc acd abc'
s.find('abc')
s.rfind('abc')
s.replace('abc', 'cba', 1)
s.count('abc')


raw = ("g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.",
       "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr",
       "gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.",
       "lmu ynnjw ml rfc spj.")
table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
raw.translate(table)
"map".translate(str.maketrans("abcdefghijklmnopqrstuvwxyz",
                              "cdefghijklmnopqrstuvwxyzab"))



"0123456789"[6:3:-1]
# "654"

foo = "yasoob"
foo[::-1]
# 'boosay'


["%-3d%12d" % (exponent, 10**exponent) for exponent in range(7, 11)]
# ['7      10000000', '8     100000000', '9    1000000000', '10  10000000000']


correct = 'correct'
phonetic_correct = 'phonetic_correct'
typo = 'typo'
phonetic_typo = 'phonetic_typo'
phonetic_distance = 'phonetic_distance'

print(f'No Spacing:')
print(f'{correct}|{phonetic_correct}|{typo}|{phonetic_typo}|{phonetic_distance}|\n')
# No Spacing:
# correct|phonetic_correct|typo|phonetic_typo|phonetic_distance|

print(f'Right Aligned:')
print(f'{correct:>10}|{phonetic_correct:>20}|{typo:>10}|{phonetic_typo:>20}|{phonetic_distance:>20}|\n')
# Right Aligned:
#    correct|    phonetic_correct|      typo|       phonetic_typo|   phonetic_distance|

print(f'Left Aligned:')
print(f'{correct:<10}|{phonetic_correct:<20}|{typo:<10}|{phonetic_typo:<20}|{phonetic_distance:<20}|\n')
# Left Aligned:
# correct   |phonetic_correct    |typo      |phonetic_typo       |phonetic_distance   |

print(f'Centre Aligned:')
print(f'{correct:^10}|{phonetic_correct:^20}|{typo:^10}|{phonetic_typo:^20}|{phonetic_distance:^20}|')
# Centre Aligned:


def wrap(string: str, k: int) -> List[str]:
    # textwrap.wrap('AABCAAADA', 3) -> ['AAB', 'CAA', 'ADA']
    import textwrap
    return textwrap.wrap(string, k)


def fill(string: str, max_width: int) -> str:
    # textwrap.fill('AABCAAADA', 3) -> 'AAB\nCAA\nADA'
    import textwrap
    return textwrap.fill(string, width=max_width)


def most_amount_sub(string, sub):
    n = 1
    while b*n in string:
        n += 1
    return n - 1


def rev_s(s: str) -> str:
    # fastest reversing string in Python
    return s[::-1]


def remove_spaces(x: str) -> str:
    return x.replace(' ', '')








# "[^"\s,):]
# [^"\s,):]"
# leap([\s\w+])year

re.I  # re.IGNORECASE
re.DEBUG


len(max(re.findall(r'(1+)', '3441153111154354113111111')))
# 6

bool(re.findall(r'c{1}(\w*)w{1}(\w*)h{1}(\w*)', 'dcsdgfwgdh'))
# True

# +-float
pattern = re.compile(r'^[-+]?[0-9]*\.[0-9]+$')
pattern.match('text')
print(bool(pattern.match('text')))

# split
regex_pattern = r"[,.]"
re.split(regex_pattern, '100,000,000.000')
# ['100', '000', '000', '000']


sentence = "this is a test, not testing."
it = re.finditer('\\btest\\b', sentence)
for match in it:
    print("match position: " + str(match.start()) + "-" + str(match.end()))

# search 123-123 like strings
m = re.search(r'\d+-\d+', line)
if m:
    current = m.group(0)

# email
r"[a-z][\w._-]*@[a-z]+\.[a-z]{1,3}$"
r"^[\w-]{1,}@[a-zA-Z0-9]{1,}\.\w{1,3}$"


print(re.escape('http://www.python.org'))
# http://www\.python\.org
legal_chars = ascii_lowercase + digits + "!#$%&'*+-.^_`|~:"
print('[%s]+' % re.escape(legal_chars))
# [abcdefghijklmnopqrstuvwxyz0123456789!\#\$%\&'\*\+\-\.\^_`\|\~:]+
operators = ['+', '-', '*', '/', '**']
print('|'.join(map(re.escape, sorted(operators, reverse=True))))
# /|\-|\+|\*\*|\*
