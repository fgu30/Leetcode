```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        f = [0]*n ## f(i) 以i为结尾的数组中maximum subarray的sum最大和
        f[0] = nums[0]
        for i in range(1,n):
            f[i] =  max(nums[i],f[i-1]+ nums[i])
        return max(f)
```
