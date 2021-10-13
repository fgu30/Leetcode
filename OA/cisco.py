def solve(arr):
    
    _max = max(arr)
    c = [0]*(_max + 1)
    for i in range(2,_max):
        if c[i] == 0:
            j = i*2
            while j <=_max:
                c[j] = 1
                j += i
                
    return c
if __name__ == '__main__':
    test = [1,3,5,6]
    print(solve(test))