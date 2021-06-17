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



