def eraseOneDigit(firstnum, secondnum, thirdnum):
    _sum = int(thirdnum) - int(secondnum)
    n = len(firstnum)
    if firstnum == str(_sum):
        return True    
    # def removeZero(s):
    #     n = len(s)
    #     if n == 1:
    #         return s
    #     # for i in range(n-1):
    #     #     if s[i] == '0':
    #     #         continue
    #     i = 0
    #     while i < n -1:
    #         if s[i] != '0':
    #             break
    #         i+=1
    #     return s[i:]
    firstnum = list(firstnum)
    _sum = str(_sum)
    if n >= 3:
        i = 1
        while i < n -1:
            if firstnum[i] != '0':
                break
            i+=1
        if firstnum[i:] == _sum:
            return True
    for i in range(1,n):
        s = "".join(firstnum[:i] + firstnum[i+1:])
        if _sum == s:
            return True
    
            
    return False
        

if __name__ == '__main__':
    ans =  eraseOneDigit('10534','67','1120')
    print(ans)