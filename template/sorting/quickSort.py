def quicksort(left, right, nums): #in-place
    if(left >= right):
        return
    mid = left + right >> 1
    pivot = nums[mid]
    i = left - 1 
    j = right + 1
    ## 为什么当pivot = num[left] and l,i-1/i,r 会造成死循环
    ## [1，2] pivot=1
    ## i = 0 j = 0
    ## i - 1 = -1
    ## 新的 区间为 [0,-1] [0,1]->[1,2]
    ## 同理 为什么当pivot = num[right] and l,j/j+1,r 会造成死循环
    ## [2，2] pivot=1
    ##    
    ## i = 1 j = 0
    ## j+1 = 1
    ## 新的 区间为 (0,0) (0,1)->[1,2]
    while(i < j):
        i+=1
        while(nums[i] < pivot):
            i += 1
        j-=1
        while(nums[j] > pivot):
            j -=1
        if i < j :
            nums[i],nums[j] = nums[j],nums[i]            
    quicksort(j+1,right,nums)
    quicksort(left,j,nums)

if __name__ == '__main__':
    N = int(input())
    nums = [int(_) for _ in input().split()]
    quicksort(0,N-1,nums)
    for num in nums:
        print(num,end=" ")
    