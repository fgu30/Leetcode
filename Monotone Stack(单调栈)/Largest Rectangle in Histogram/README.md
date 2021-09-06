## brutal force

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        for i in range(n):
            h = heights[i]
            left = i - 1
            while left > 0 and heights[left] >= h:
                left -=1
            right = i + 1
            while right < n and heights[right] >= h:
                right += 1
            res = max(res,(right - left - 1)*h)
        return res
```

## monotone:

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 1: return heights[-1]
        stk = [0]
        res = 0
        for i in range(1,n):
            while stk and heights[i] < heights[stk[-1]]:
                hidx = stk.pop()
                w = i
                if stk:
                    w = i - stk[-1] - 1
                res = max(res,w*heights[hidx])
            stk.append(i)
        ## monotune asc stak in stk
        while stk:
            idx = stk.pop()
            h = heights[idx]
            w = n
            if stk:
                w = n - stk[-1] - 1
            res = max(res,h*w)
        return res
```
