'''
You are given a string that represents time in the format hh:mm. Some of the digits are blank (represented by ?). Fill in ? such that the time represented by this string is the maximum possible. Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.
Example 1:

Input: "?4:5?"
Output: "14:59"
Example 2:

Input: "23:5?"
Output: "23:59"
Example 3:

Input: "2?:22"
Output: "23:22"
Example 4:

Input: "0?:??"
Output: "09:59"
Example 5:

Input: "??:??"
Output: "23:59"
'''
def getTime(s):
    n = len(s)
    ans = ['_']*(n)
    ## HH:MM
    if s[0] == "?":
        ans[0] = "2" if s[1] <="3" or s[1] == "?"else "1"
    else:
        ans[0] = s[0]
    print(ans)
    if s[1] == "?":
        ans[1] = "3" if s[0] =="2" or s[0] =="?" else"9"
    else:
        ans[1] = s[1]
    print(ans)
        
    ans[2] = ":"
    ans[3] = "5" if s[3] == "?" else s[3]
    ans[4] = "9" if s[4] == "?" else s[4]
    
    return "".join(ans) 
    
    
if __name__ == '__main__':
    # print(getTime("?4:5?"))
    print(getTime("0?:??"))
    # print(getTime("?4:5?"))
    # print(getTime("2?:22"))
    # print(getTime("??:??"))
    
    
 
         
        
        