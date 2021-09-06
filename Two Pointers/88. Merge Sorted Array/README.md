[88. Merge Sorted Array](https://leetcode-cn.com/problems/merge-sorted-array/)

---

启发于 mergesort 方法

```Python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # N,M = len(nums1),len(nums2)
        k = m + n -1
        m-=1
        n-=1
        while m >= 0 and n >=0:
            if nums1[m] > nums2[n]:
                nums1[k] = nums1[m]
                m-=1
            else:
                nums1[k] = nums2[n]
                n-=1
            k-=1
        while m >= 0:
            nums1[k] = nums1[m]
            k-=1
            m-=1
        while n >= 0:
            nums1[k] = nums2[n]
            k-=1
            n-=1



```

---

把 nums2 塞入 nums1

```Python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        m-=1
        n-=1
        while n >= 0:
            if m >= 0 and nums1[m] > nums2[n]:
                nums1[i] = nums1[m]
                i-=1
                m-=1
            else:
                nums1[i] = nums2[n]
                i-=1
                n-=1
```
