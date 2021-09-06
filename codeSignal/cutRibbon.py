def solve(arr,k):
    arr.sort()
    def getLen(mid):
        res = 0
        for num in arr:
            res+= num //mid
            
        return res
    
    l = 1
    r = arr[-1]
    
    while l < r:
        mid = l + r + 1 >> 1
        if getLen(mid) >=k:
            l = mid
        else:
            r = mid - 1
    return l
            

if __name__ == '__main__':
    test = [1,2,3,4,9]
    k = 5
    print(solve(test,k))
            