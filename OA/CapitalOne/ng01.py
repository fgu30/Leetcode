def solve(words):
    n = len(words)
    ans = [False]*(n-1)
    for i in range(n-1):
        word1 = words[i]
        word2 = words[i+1]
        if word1[0] == word2[0] and word1[-1] == word2[-1]:
            ans[i] = True
    return ans
if __name__ == '__main__':
    test = ["abcd", "abdd", "da", "dd"]
    print(solve(test))
    
