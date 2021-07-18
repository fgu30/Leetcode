```python
if dfs(i-1,j,k+1)\
or dfs(i+1,j,k+1)\
or dfs(i,j-1,k+1)\
or dfs(i,j+1,k+1) == True:
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
