def findTargetSumWays(nums, target) -> int:
    n = len(nums)
    prefix_up = [0]*(n+1)
    prefix_down = [0]*(n+1)
    for i in range(n):
        prefix_up[i+1] = prefix_up[i] + nums[i]
        prefix_down[i+1] = prefix_down[i] - nums[i]
        
    
    count = [0]
    def dfs(nums,index,target):
        if(index == n):
            if target == 0:
                count[0]+=1
            return
        if(index < n):
            a = prefix_up[n] - prefix_up[index]
            b = prefix_down[n] - prefix_down[index]
            if target > a and target < b:
                return 
        num = nums[index]
        #target -= num
        dfs(nums,index+1,target-num)
        #target += 2*num
        dfs(nums,index+1,target+num)
    dfs(nums, 0, target)
    return count[0]

if __name__ == '__main__':
    testcase = [7,46,36,49,5,34,25,39,41,38,49,47,17,11,1,41,7,16,23,13]
    print(findTargetSumWays(testcase,3))
