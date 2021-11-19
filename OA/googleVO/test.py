from sortedcontainers import SortedDict
from bisect import *
sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
print(max(sd.keys()[0]))

A= [2]
insort_right(A,3)
print(A)