# -*- coding: utf-8 -*-
import re
import string

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
re.compile(r"^[\w-]{1,}@[a-zA-Z0-9]{1,}\.\w{1,3}")


print(re.escape('http://www.python.org'))
# http://www\.python\.org
legal_chars = string.ascii_lowercase + string.digits + "!#$%&'*+-.^_`|~:"
print('[%s]+' % re.escape(legal_chars))
# [abcdefghijklmnopqrstuvwxyz0123456789!\#\$%\&'\*\+\-\.\^_`\|\~:]+
operators = ['+', '-', '*', '/', '**']
print('|'.join(map(re.escape, sorted(operators, reverse=True))))
# /|\-|\+|\*\*|\*
