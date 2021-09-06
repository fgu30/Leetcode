## 85. 最大矩形

[85. 最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/)

- Brutal Force 这个技巧很重要从右下角向上扩散

```Python
# O(n^3)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        res = 0
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    if j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i][j-1] + 1
                else:
                    dp[i][j] = 0
                w = dp[i][j]
                h = i
                while h >= 0:
                    w = min(w,dp[h][j])
                    res = max(res,w*(i-h+1))
                    h-=1
        return res
```

- 单调栈

```Python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0 or len(matrix[0])==0:
            return 0
        m, n = len(matrix), len(matrix[0])
        left = [0]*n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] += 1
                else:
                    left[j] = 0
            res = max(res, self.largestRectangleArea(left))

        return res

```
