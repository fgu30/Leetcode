def threesum(nums): ## N >= 2
    
    def twoSum(nums,target):## N ==2
        ans = []
        k = 0
        j = len(nums)-1
        while(k < j):
            left = nums[k]
            right = nums[j]
            tmp = nums[k] + nums[j]
            if(tmp == target):
                ans.append([nums[k],nums[j]])
                while(k<j and nums[k] == left):
                    k+=1
                while(k<j and nums[j] == right):
                    j-=1
            elif (tmp < target):
                k+=1
            else:    
                j-=1
        return ans
    def nSum(nums,N,target): ## N > 2
        if N == 2:
            return twoSum(nums,target)
        ans = []
        for i in range(len(nums)-N + 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            tmp =  nSum(nums[i+1:],N-1,target - nums[i])
            ans += [([nums[i]] + _) for _ in tmp] 
        return ans
    
    nums.sort()            
    return nSum(nums,3,0)      

if __name__ == '__main__':
    arr = [-1,0,1,2,-1,-4]
    print(threesum(arr))
    
            
            
            
        
        