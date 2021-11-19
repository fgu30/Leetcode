class Solution:
    def decodeCiphertext(self, s: str, rows: int) -> str:
        m = len(s) // rows
        res = []
        for i in range(m):
            while i < len(s):
                res.append(s[i])
                i += m + 1
        return ''.join(res).rstrip()