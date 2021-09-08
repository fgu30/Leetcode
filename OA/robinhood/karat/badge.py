'''
Q1 
'''

def findMatch(records):
    inRoom = set() 
    _exit = set()
    _enter = set()
    for record in records:
        name,signal = record
        if signal == 'exit':
            if name not in inRoom:
                _enter.add(name)
            else:
                inRoom.remove(name)
        elif signal == 'enter':
            if name in inRoom:
                _exit.add(name)
            else:
                inRoom.add(name)
                
            
    return [list(_exit) + list(inRoom),list(_enter)]
    
    
'''
Q2
'''

from collections import defaultdict

# def security_check(access_list):
#     return_result = dict()
#     access_data_dict = dict()
#     for employee in access_list:
#         if employee[0] not in access_data_dict:
#             access_data_dict[employee[0]] = [employee[1]]
#         else:
#             access_data_dict[employee[0]].append(employee[1])

#     for name, val in access_data_dict.items():
#         if len(val) >= 3:
#             val = sorted([int(p) for p in val]) #this sort takes O(nlogn) and I changed the value type to int so I get it in the right order.
#             start = 0
#             start_time = val[start]
#             time_result = [start_time]
#             for x in range(start + 1, len(val)):
#                 if val[x] - start_time <= 100:
#                     time_result.append(val[x])
#                     if len(time_result) >= 3:
#                         if name not in return_result:
#                             return_result[name] = time_result
#                 else:
#                     start += 1
#                     start_time = val[start]
#                     time_result = [start_time]

#     return return_result
            
def solve(times):
    
    ans = dict()
    timeHolder = defaultdict(list)
    for name,time in times:
        timeHolder[name].append(time)
    for k,v in timeHolder.items():
        v = sorted([int(_) for _ in v])
        if len(v) >= 3:
            start = 0
            startTime = v[start]
            tmp = [startTime]
            for i in range(start+1,len(v)):
                if v[i] - startTime <=100:
                    tmp.append(v[i])
                    if len(tmp) >= 3:
                        if k not in ans:
                            ans[k] = tmp
                else:
                    start +=1
                    startTime = v[start]
                    tmp = [startTime]
    return ans
                        
            
            
        
        
    
    
    
    
if __name__ == '__main__':
    badge_records = [
        ["Martha",   "exit"],
        ["Paul",     "enter"],
        ["Martha",   "enter"],
        ["Martha",   "exit"],
        ["Jennifer", "enter"],
        ["Paul",     "enter"],
        ["Curtis",   "enter"],
        ["Paul",     "exit"],

    ]
    
    
    badge_times = [
        ["Paul",     "1355"],
        ["Jennifer", "1910"],
        ["John",      "835"],
        ["John",      "830"],
        ["Paul",     "1315"],
        ["John",     "1615"],
        ["John",     "1640"],
        ["Paul",     "1405"],
        ["John",      "855"],
        ["John",      "930"],
        ["John",      "915"],
        ["John",      "730"],
        ["John",      "940"],
        ["Jennifer", "1335"],
        ["Jennifer",  "730"],
        ["John",     "1630"],
        ["Jennifer",    "5"]
        ]

    print(findMatch(badge_records)) 
    print(solve(badge_times))    
                
            
                
                
                
                
            