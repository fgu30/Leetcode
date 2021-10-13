## CAT

import collections


a = "abcdefghijklmnopqrstuvwxyz"

cnt = set(a)
_cnt = set()
for char in a:
    if char.isupper():
        if char.lower() not in cnt:
            _cnt.add(char)
    else:
        if char.upper() not in cnt:
            _cnt.add(char)
cnt = cnt - _cnt
res = 0

m = len(cnt)
n = len(a)
another = dict()
i = j = 0
res = float('inf')
print(cnt)
while j < n:
    
    another[a[j]] = another.get(a[j],0) + 1

    while another.keys() & cnt == cnt:
            if another.keys() == cnt:
                res = min(res,j-i+1)
            print(another,2)
            another[a[i]] -=1
            if another[a[i]] == 0:
                another.pop(a[i])
            i+=1
    j+=1
print(res)
    
