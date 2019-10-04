# -*- coding: utf-8 -*-
import re

# "[^"\s,):]
# [^"\s,):]"
# leap([\s\w+])year

len(max(re.findall(r'(1+)', '3441153111154354113111111')))
# 6

bool(re.findall(r'c{1}(\w*)w{1}(\w*)h{1}(\w*)', 'dcsdgfwgdh'))
# True

# +-float
pattern = re.compile(r'^[-+]?[0-9]*\.[0-9]+$')
pattern.match('text')
print(bool(pattern.match('text')))

# split
import re
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

re.IGNORECASE | re.DEBUG
