## DFS

### 先判断越界条件

[79.Word Search](https://leetcode-cn.com/problems/word-search/)

## 单调栈

先做比较 再入栈。

[42. Trapping Rain Water](https://leetcode-cn.com/problems/trapping-rain-water/)

```python
   class Solution:
    def trap(self, height: List[int]) -> int:
        helper = []
        ans = 0
        for idx,i in enumerate(height):
            tmp = 0
            #node= (0,1) (idx,num)
            while(helper and helper[-1][1] < i):
                node = helper.pop()
                ans += (node[1] - tmp)*(idx - node[0]-1)
                tmp = node[1]
            if helper:
                ans +=(i - tmp)*(idx - helper[-1][0] - 1)
            helper.append((idx,i))
        return ans
```

for 循环中：
第二个条件:while 循环比较的是当前数字和单调栈中的最小值,不断 pop 比 height[i]小的数， 并没有入栈
第二个条件时，height[i]已经不符合单调栈里的条件，处理自己作为挡板 height 的情况之后，准备入栈
入栈，完成 for 循环
