import bisect
  
# initializing list
li = [1,2,2,3,4]
a = bisect.bisect_left(li,1)
b = bisect.bisect_right(li,2,3,5)
print(li)
print(b)