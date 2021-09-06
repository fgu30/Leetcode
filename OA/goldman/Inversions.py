# a = (1,2)
# b = set()
# b.add((1,2))
# print(b)
# b.add((1,2))
# print(b)
def solve(nums):
    n = len(nums)
    ans = set()
    tmp = []
    def dfs(idx):
        if len(tmp) == 3:
            ans.add(tuple(tmp[:]))
            return 
        for i in range(idx,n):
            if tmp and nums[i] >= tmp[-1]:
                continue
            tmp.append(nums[i])
            dfs(i+1)
            tmp.pop()

    dfs(0)
    return len(ans)

if __name__ == '__main__':
    test = [4,2,2,1]
    print(solve(test))
    