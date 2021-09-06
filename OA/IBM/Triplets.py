def solve(arr,target):
    arr.sort()
    n = len(arr)
    ans = 0
    for i in range(n):
        _sum = target - arr[i]
        j,k = i+1,n-1
        while j <k :
            if arr[j] + arr[k] >_sum:
                k-=1
            else:
                print(i,j,k)
                ans+=(k - j)
                j+=1
    return ans
    
if __name__ == '__main__':
    test = [1,2,3,4,5]
    t = 8
    
    print(solve(test,t))
    