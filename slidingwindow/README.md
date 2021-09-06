# labuladong 滑动窗口模板

```
string s, t;
// 在 s 中寻找 t 的「最小覆盖子串」
int left = 0, right = 0;
string res = s;

while(right < s.size()) {
    window.add(s[right]);
    right++;
    // 如果符合要求，移动 left 缩小窗口
    while (window 符合要求) {
        // 如果这个窗口的子串更短，则更新 res
        res = minLen(res, window);
        window.remove(s[left]);
        left++;
    }
}
return res;

```

```
class Solution:
    def problemName(self, s: str) -> int:
        # Step 1: 定义需要维护的变量们 (对于滑动窗口类题目，这些变量通常是最小长度，最大长度，或者哈希表)
        x, y = ..., ...

        # Step 2: 定义窗口的首尾端 (start, end)， 然后滑动窗口
        start = 0
        for end in range(len(s)):
            # Step 3: 更新需要维护的变量, 有的变量需要一个if语句来维护 (比如最大最小长度)
            x = new_x
            if condition:
                y = new_y

            '''
            ------------- 下面是两种情况，读者请根据题意二选1 -------------
            '''
            # Step 4 - 情况1
            # 如果题目的窗口长度固定：用一个if语句判断一下当前窗口长度是否超过限定长度
            # 如果超过了，窗口左指针前移一个单位保证窗口长度固定, 在那之前, 先更新Step 1定义的(部分或所有)维护变量
            if 窗口长度大于限定值:
                # 更新 (部分或所有) 维护变量
                # 窗口左指针前移一个单位保证窗口长度固定

            # Step 4 - 情况2
            # 如果题目的窗口长度可变: 这个时候一般涉及到窗口是否合法的问题
            # 如果当前窗口不合法时, 用一个while去不断移动窗口左指针, 从而剔除非法元素直到窗口再次合法
            # 在左指针移动之前更新Step 1定义的(部分或所有)维护变量
            while 不合法:
                # 更新 (部分或所有) 维护变量
                # 不断移动窗口左指针直到窗口再次合法

        # Step 5: 返回答案
        return ...

作者：eason734
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/yi-ge-mo-ban-miao-sha-10dao-zhong-deng-n-sb0x/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

- 简单的维护一个长度为 K 的数组，right + 1 then left -1 不需要 while 循环
  [643. Maximum Average Subarray I](https://leetcode-cn.com/problems/maximum-average-subarray-i/)

- hashmaap + sliding window:
  [904. Fruit Into Baskets](https://leetcode-cn.com/problems/fruit-into-baskets/)
