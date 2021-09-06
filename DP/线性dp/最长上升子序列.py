class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0]*(n+5)
        f[0] = float('-inf')
        cnt = 0
        for i in range(n):
            l,r = 0,cnt
            while l < r: # 右边界
                mid = l + r + 1>> 1
                if f[mid] < nums[i]: l = mid
                else:
                    r = mid - 1
            cnt = max(cnt,r+1)
            f[r+1] = nums[i]
        return cnt