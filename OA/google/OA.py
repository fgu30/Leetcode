def solution(A:int):
    ans = float('inf')
    helper = 10
    while True:
        a = A // helper
        if a == 0:
            break
        b = A % helper
        print(a,b)
        tmp = abs(a-b)
        ans = tmp if tmp < ans else ans 
        helper *=10
    
    return ans

if __name__ == '__main__':
    print(solution(999999))
    