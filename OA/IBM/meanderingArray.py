def solve(arr):
    n = len(arr)
    arr.sort()
    l = r = 0
    ans = []
    k = n -1
    while r <= k :
        ans.append(arr[k])
        l+=1
        k-=1
        if l == n:
            break
        ans.append(arr[r])
        l+=1
        r+=1
    return ans
if __name__ == '__main__':
    test = [-1,1,2,3,-5]
    print(solve(test))
        
