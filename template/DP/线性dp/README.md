# 所谓线性 DP

- 最长长生子序列：
  [300. Longest Increasing Subsequence](https://leetcode-cn.com/problems/longest-increasing-subsequence/)

  - 朴素 dp O(n^2)

  - 二分优化 O(nLogn): 为什么不用 bisect 来找边界，因为求出 l=r 之后需要判断是否越界，因为 bisect 是插入功能，例如 [1,1] 插入 1，index 为 2

![](/image-20210802015442154.png)
