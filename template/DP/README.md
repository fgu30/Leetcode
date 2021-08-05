## 动态规划总结



闫式DP分析法：

集合划分：化零为整（划分集合），化整为零（状态转移）





[labuladong 动态规划详解(fibbonaci and coin change)](https://labuladong.gitbook.io/algo/mu-lu-ye-2/mu-lu-ye/dong-tai-gui-hua-xiang-jie-jin-jie)
**_Base case 是否是 0？是否是无穷？值得思考_** 求极值的时候

***状态转移的遍历顺序？正序？倒序？斜角？这个问题之前没有考虑过，但是其实非常重要***



-----

#### 子序列问题 subarray 问题

问题的关键点在于集合划分，**f( i )** 如果代表的是在 index **_i_** 的时子序列的长度的话就是错的，将无法解决子序列问题。通常处理的方法是 **_i_** 为 数组中的数字

- Maximum Subarray 问题

[53. Maximum Subarray](https://leetcode-cn.com/problems/maximum-subarray/)

[1143. Longest Common Subsequence](https://leetcode-cn.com/problems/longest-common-subsequence/)

[516. Longest Palindromic Subsequence](https://leetcode-cn.com/problems/longest-palindromic-subsequence/)

---

####

---

- 零钱问题：和 01 背包问题类似，每个 coin 拿还是不拿，拿了 dp[i-coin] + 1

[322. Coin Change](https://leetcode-cn.com/problems/coin-change/)
