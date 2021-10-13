#非常巧妙的后续遍历+hashmap #利用 hashamp 对应 head:newhead 的关系 iterative 方法

- [138. Copy List with Random Pointer](https://leetcode-cn.com/problems/copy-list-with-random-pointer/)

### LinkedList 总结;

### 快慢指针问题：

```python
fast = head.next
slow = head
#奇数时，slow在mid
#偶数时候，在mid -1
# 能达到[left,slow],[slow.next,right]分割不造成死循环

fast = head
slow = head
#偶数时在mid+1
#奇数时候在mid
#这种会死循环
```

![如图](./merge.png)

### 相关问题

#### 1.merge linkedlist 问题：
