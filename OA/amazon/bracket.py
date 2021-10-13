def solve(s):
    stk = []
    n = len(s)
    cnt = 0
    for i in range(n): #自然消掉括号
        br = s[i]
        if stk and stk[-1] == '{' and br =='}':
            stk.pop()   
        else:
            stk.append(br)
    
    if len(stk) == 0 :
        return 0
    
    if len(stk)% 2 == 1:
        return -1
    print(stk)
    while stk:
        br = stk.pop()
        _br = stk.pop()
        
        if _br == br:
            cnt+=1
        elif br != _br:
            
            cnt+=2
    return cnt
        
        
if __name__ == '__main__':
    s = "}}{{"
    print(solve(s))
    
    