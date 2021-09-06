def mergeSort(nums):
    n = len(nums)
    tmp = [0]*n
    def sort(left,right,nums):
        if left >= right:
            return;
        mid = left + right >>1
        sort(left,mid,nums)
        sort(mid+1,right,nums)
        i = left
        j = mid + 1
        k = 0
        while(i <= mid and j <= right):
            if nums[i] < nums[j]:
                tmp[k] = nums[i]
                i+=1
                k+=1
            else:
                tmp[k] = nums[j]
                j+=1
                k+=1
        while(i <= mid):
            tmp[k] = nums[i]
            i+=1
            k+=1            
        while(j <= right):
            tmp[k] = nums[j]
            j+=1
            k+=1
        m = left
        n = 0
        while(m <= right):
            nums[m] = tmp[n]
            m+=1
            n+=1
    sort(0,n-1,nums)
    
if __name__ == '__main__':
    arr = [3,2,1,4,7,5]
    mergeSort(arr)
    print(arr)
           
        
    
    