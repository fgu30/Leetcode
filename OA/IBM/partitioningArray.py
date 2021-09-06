
def solve(arr,k):
    n = len(arr)
    if n % k != 0:
        return False
    count = Counter(arr)
    for d in count:
        if count[d] >k :
            return False
    return True    


if __name__ == '__main__':
    test = [1,2,2,3]
    k = 3
    print(solve(test,k))
    