from collections import defaultdict
def arrayAdditionAndSum(a, b, queries):
    n = len(a)
    m = len(b)
    # print(queries)
    _mapA = dict()
    _mapB = dict()
    for i in range(n):
        _mapA[a[i]] = _mapA.get(a[i],0) +1
    for i in range(m):
        _mapB[b[i]] = _mapB.get(b[i],0) +1

    def findpair(x):
        res = 0
        for ka in _mapA:
            if x - ka in _mapB:
                res+= _mapA[ka]*_mapB[x-ka]
        return res
    ans = []
    for query in queries:
        if query[0] == 0:
            A,idx,x = query
            num = b[idx]
            # if num not in _mapB:
            #     _mapB[num] = 1
            # else:
            _mapB[num] -=1
            if _mapB[num] == 0:
                _mapB.pop(num)
            num = num + x
            b[idx] = num
            if num not in _mapB:
                _mapB[num] = 1
            else:
                _mapB[num] +=1
        else:
            A,x = query
            ans.append(findpair(x))
    return ans
            
    
