def solve(s,l,r):
    if l  == r:
        return s
    n = len(s)
    if r > l:
        "abcde"
        "de abc"
        step = (r - l) % n 
        return "".join(s[-step:]+s[:-step])
    if r < l:
        "abcde"
        "cde ab"
        step = (l - r) % n 
        return "".join(s[step+1:] +s[:step+1])
    
if __name__ == '__main__':
    S = "abcde"
    print(solve(S,1,0))
    print(solve(S,2,0))
    print(solve(S,0,1))
    print(solve(S,0,2))
    