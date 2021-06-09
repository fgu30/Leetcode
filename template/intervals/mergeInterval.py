def merge(lists):
    #sort排序
    l = float('-inf')
    r = float('-inf')
    lists.sort()
    res = []
    for list in lists:
        #next intetval left > right ,so add old one to the ans list
        if(list[0] > r):
            #exclude the first one[-inf,-inf]
            if(l != float('-inf')):
                res.append([l,r])
            l = list[0]
            r = list[1]          
        else:
            r = max(r,list[1])
        
    # add last list to ans
    if(l != float('inf')):
        res.append([l,r])
    return res
            
]
        
    
    
    