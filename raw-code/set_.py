# -*- coding: utf-8 -*-

set1 | set2    # set1.union(set2)
set1 & set2    # set1.intersection(set2)
set1 - set2    # set1.difference(set2)
set1 ^ set2    # set1.symmetric_difference(set2)

g1 = set(globals())
import something
g2 = set(globals())
g2 - g1

set.remove(2)
set.pop()
set.add('el')

frozen = frozenset(['el1', 'el2', 'el3'])    # immuteble set()

# for x in a:
#     for y in b:
#         if x == y:
#             yield (x,y)
return set(a) & set(b)

# Matching subset
set(a) < set(b)


# list cut on sets
n, arr = 2, list(range(10))
[set(arr[i:i+n]) for i in list(range(len(arr))[::n])]
# [{0, 1}, {2, 3}, {4, 5}, {6, 7}, {8, 9}]
