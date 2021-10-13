from bisect import *
 
a = []
insort(a,3)
insort(a,3)
insort(a,4)
insort(a,4)


print(a)
print(bisect_right(a,3))

