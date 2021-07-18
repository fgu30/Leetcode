import collections 
def solve(arr):
    wordsMap = [collections.Counter(word) for word in arr]
    ans = []
    prev = None
    for i in range(len(arr)):
        if i>0 and wordsMap[i] == wordsMap[i-1]:
            continue      
        ans.append(arr[i])
    return ans

if __name__ == '__main__':
    string = ['code','doce','ecod','framer','frame']
    print(solve(string))