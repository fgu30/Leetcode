## DFS

[79. Word Search](https://leetcode-cn.com/problems/word-search/)

```python
if dfs(i-1,j,k+1)\
or dfs(i+1,j,k+1)\
or dfs(i,j-1,k+1)\
or dfs(i,j+1,k+1) == True:Cancel changes
    return True
```

```python
return dfs(i-1,j,k+1)\
or dfs(i+1,j,k+1)\
or dfs(i,j-1,k+1)\
or dfs(i,j+1,k+1)
```

这个问题想了 2 个小时，两个有本质的区别，正确的是，当有 true 的时候，才返回，而不是返回 or 之后的不在乎 true or false 的结果。

这个问题尤其在 recuision 的时候 需要重点注意，尤其自下而上需要 return 一个结果的时候，要想清楚题问的条件。

## 单调栈

先做比较 再入栈。

[42.接雨水](https://github.com/fgu30/Leetcode/tree/main/42.%20Trapping%20Rain%20Water)

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
