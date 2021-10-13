from collections import Counter

a = 'aabbcc'
count = Counter(a)
print(count)
count['a'] -=1
print(type(count['a']))
print((3 == 3) is not True)