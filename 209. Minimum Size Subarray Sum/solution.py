class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0
        n = len(nums)
        ans = float('inf')
        tmp_sum = 0
        while right < n:
            tmp_sum += nums[right]
            while tmp_sum >= target:
                ans = min(ans,right - left + 1)
                tmp_sum -= nums[left]
                left+=1
            right +=1
        return 0 if ans == float('inf') else ans;
            