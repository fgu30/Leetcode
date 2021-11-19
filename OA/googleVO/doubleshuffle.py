from collections import *


arr= [3, 4, 2, 1, 2, 6]

def solve(test):
    dic = Counter(test)
    res = []
    for x in sorted(test,key=abs):
        if dic[x] == 0:continue
        res.append(x)
        dic[x] -=1
        dic[2*x] -=1
    
    return res

print(solve(arr))    