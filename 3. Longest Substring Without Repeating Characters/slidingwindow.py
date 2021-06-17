'''

slding window O(n)


'''


import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wordSet = collections.defaultdict(int)
        i = 0
        j = 0
        ans = 0
        while(i < len(s)):
            ch = s[i]
            wordSet[ch] +=1
            i+=1
            #被加入的字符的数量一旦超过1 移动j 直到把ch字符的数量酱到1为止
            while(j < i and wordSet[ch] > 1):
                _ch = s[j]
                wordSet[_ch] -= 1
                j+=1
            ans = max(ans,i - j)
        return ans