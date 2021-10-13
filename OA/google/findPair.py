from collections import defaultdict

def findK(nums):
    _map = defaultdict(list)
    n = len(nums)
    for i in range(n):
        _map[nums[i] - i].append(i)
        _map[nums[i] + i].append(i)
    res = 0
    for group in _map.values():
        res = max(res,(group[-1]-group[0]))
    return res
    
print(findK([1,4,6,-2]))