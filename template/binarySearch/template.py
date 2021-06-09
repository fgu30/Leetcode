def leftBound(nums,target):
    n = len(nums)
    left = 0
    right = n - 1
    while(left < right):
        mid = left + right >> 1
        #l,mid || mid+1,right
        if(nums[mid] >= target):
            right = mid
        elif(nums[mid] < target):# 1 2 2 3 4
            left = mid + 1
    
    return left if nums[left] == target else -1

def rightBound(nums,target):
    n = len(nums)
    left = 0
    right = n - 1
    while(left < right):
        mid = left + (right-left + 1) //2
        #l,mid-1|| mid,right [2,2] 
        if(nums[mid] <= target):
            left = mid
        elif(nums[mid] > target):# 1 2 2 3 4
            right = mid - 1

    
    return left if nums[left] == target else -1



if __name__ == '__main__':
    arr = [2,2,2,2,2,2]
    ans = leftBound(arr,2)
    print(ans)
    ansr = rightBound(arr,2)
    print(ansr)
         
        
        
        
    