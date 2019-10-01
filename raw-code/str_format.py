# -*- coding: utf-8 -*-
ord('f')
# 102

chr(102)
# 'f'


''.swapcase()
"-".join(s.split())

from string import ascii_lowercase
list(ascii_lowercase)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



width = len("{0:b}".format(number))
print("{0:{w}n} {0:{w}o} {0:{w}X} {0:{w}b}".format(n, w=width))


s.split('', 1)
s.rsplit()
string.splitlines()


example_string = r'File on disk C:\\'   # Raw string

word = 'eeeee'
print(word.count('e'))    # 5

"2017".isdigit()    # True

"3.14" in "3.1415926"   # True

template = "%s (%s)"
template % ("word")

"{}".format("word")
"{word}".format(word="word")

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

foo = 'foo'
bar = 'bar'
foobar = '%s%s' % (foo, bar)  # It is OK
foobar = '{0}{1}'.format(foo, bar)  # It is better
foobar = '{foo}{bar}'.format(foo=foo, bar=bar)  # It is best


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


''.join(reversed('TURBO'))

'_'.join('hello')
# 'h_e_l_l_o'

print('\n'.join(['0', '1', '2']))
# 0
# 1
# 2


bytes("hello", "ascii")
# b'hello'
