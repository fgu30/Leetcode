def solve(arr,k):
    arr.sort()
    n = len(arr)
    ans = float('inf')
    l = r = 0
    while r < n :
        if r - l +1== k:
            ans = min(ans,arr[r] - arr[l]+1)
        elif r - l + 1> k:
            l+=1
            continue
        r +=1
    return ans
            
if __name__ == '__main__':
    test =  [2,10,8,17]
    k = 3
    print(solve(test,k))
        
            
    