def solve(nums):
    _sum = sum(nums) ## O(n)
    n = len(nums)
    l = 0
    r = n - 1
    while l < r:
        mid = l + r >> 1
        if sum(nums[:mid]) > (_sum - nums[mid]) //2:
            r = mid - 1
        elif sum(nums[:mid]) < (_sum - nums[mid]) //2:
            l = mid + 1
        else:
            return mid
            
    # O(n) + O(n*logN)
        
if __name__ == '__main__':
    # test = [1,2,3,4,6]
    test = [4,3,10,7,0]
    print(solve(test))
    