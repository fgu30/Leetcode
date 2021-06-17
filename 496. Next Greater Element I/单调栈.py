class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = dict()
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                node = stack.pop()
                hashmap[node] = num
            stack.append(num)
        for i in range(len(nums1)):
            if nums1[i] in hashmap:
                nums1[i] = hashmap[nums1[i]]
            else:
                nums1[i] = -1
        return nums1