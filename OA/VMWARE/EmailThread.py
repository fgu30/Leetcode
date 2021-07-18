# from typing import Coroutine


# def solve (emailList):
#     emailMap = dict()
#     ans =[]
#     count = 1
#     for email in emailList:
#         email = [word.strip() for word in email.split(",")][:2]
#         print(email)
#         _email = " ".join(reversed(email))
#         email = " ".join(email)

            
#         if email not in emailMap or _email in emailMap:
#             ##反的等待接收
#             tmp = [count,1]
#             emailMap[_email]=tmp
#             ans.append(tmp)
#             count+=1
#             continue
#         elif email in emailMap:
#             cnt,num  = emailMap[email]
#             emailMap.pop(email)
#             emailMap[_email] = [cnt,num+1]
#             ans.append([cnt,num+1])
#     return ans



def emailThreads(strs):
    msgs = dict()
    tids = 0
    output = []
    for s in strs:
        lst = [word.strip() for word in s.split(",")]
        sender, receiver, content = lst[0], lst[1], lst[2]
        print(lst)
        if '---' not in content:
        # this is a new thread
            tids += 1
            msgs[tuple(lst)] = [tids, 1]
            output.append([tids,1])
        else:
            msg = content.split('---')
            prev = msg[1:]
            last_thread = (receiver, sender, '---'.join(prev))
            _last_thread = (sender, receiver, '---'.join(prev))
            if last_thread in msgs:
                tid, msg_cnt = msgs[last_thread][0], msgs[last_thread][1]
                # output current data point
                output.append([tid, msg_cnt+1])
                msgs[tuple(lst)] = [tid, msg_cnt+1]
                continue
            if _last_thread in msgs:
                tid, msg_cnt = msgs[_last_thread][0], msgs[_last_thread][1]
                # output current data point
                output.append([tid, msg_cnt+1])
                msgs[tuple(lst)] = [tid, msg_cnt+1]
                continue
            
    return output
if __name__ == '__main__':
    testCase = [0]*5
    testCase[0] = "a@gmail.com, b@gmail.com, first";
    testCase[1] = "a@gmail.com, b@gmail.com, first";
    testCase[2] = "b@gmail.com, c@gmail.com, first2";
    testCase[3] = "a@gmail.com, b@gmail.com, second---first";
    testCase[4] = "a@gmail.com, b@gmail.com, third---second---first";
    
    # testCase[4] = "a@gmail.com, b@gmail.com, third---second---first";
    # testCase[5] = "c@gmail.com, b@gmail.com, second2---first2";

    # print(solve(testList))
    # print(solve(testCase)) 
    print(emailThreads(testCase))      
        
    
    
