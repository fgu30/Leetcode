'''
https://leetcode.com/discuss/interview-question/1237034/roblox-karat-initial-screening-course-pair-course-schedule
'''
from collections import *


# def course_to_take(prereq_courses):
#     graph = defaultdict(list)
#     in_degrees = defaultdict(int)

#     for course_pair in prereq_courses:
#         pre_req, course = course_pair
#         graph[pre_req].append(course)
#         if pre_req not in in_degrees:
#             in_degrees[pre_req] = 0
#         in_degrees[course] += 1

#     queue = deque()
#     for key in in_degrees.keys():
#         if in_degrees[key] == 0:
#             queue.append(key)

#     res = []
#     while queue:
#         vertex = queue.popleft()
#         res.append(vertex)

#         for child in graph[vertex]:
#             in_degrees[child] -= 1
#             if in_degrees[child] == 0:
#                 queue.append(child)

#     if len(res) != len(in_degrees):
#         return []
#     return res[len(res)//2] if len(res) % 2 != 0 else res[(len(res)//2)-1]

# if __name__ == '__main__':
#     prereqs_courses1 = [
#  	["Foundations of Computer Science", "Operating Systems"],
#  	["Data Structures", "Algorithms"],
#  	["Computer Networks", "Computer Architecture"],
#  	["Algorithms", "Foundations of Computer Science"],
#  	["Computer Architecture", "Data Structures"],
# 	["Software Design", "Computer Networks"]
#     ]
#     print(course_to_take(prereqs_courses1))


# def solve(coursesList):
#     _map = defaultdict(set)
#     idSet = set()
#     for pair in coursesList:
#         id,course = pair
#         idSet.add(id)
#         _map[id].add(course)
#     ans = dict()
#     while len(idSet) > 1:
#         tmpId = idSet.pop()
#         for id in idSet:
#             ans["{},{}".format(tmpId,id)] = list(_map[tmpId] & _map[id])

#     return ans

# if __name__ == '__main__':
#     student_course_pairs_1 = [
# 	["58", "Linear Algebra"],
# 	["94", "Art History"],
# 	["94", "Operating Systems"],
# 	["17", "Software Design"],
# 	["58", "Mechanics"],
# 	["58", "Economics"],
# 	["17", "Linear Algebra"],
# 	["17", "Political Science"],
# 	["94", "Economics"],
# 	["25", "Economics"],
# 	["58", "Software Design"],
#     ]
#     print(solve(student_course_pairs_1))
    
#     a = {'94,17': [], '94,58': ['Economics'], '94,25': ['Economics'], '17,58': ['Software Design', 'Linear Algebra'], '17,25': [], '58,25': ['Economics']}
#     b = {
#             "58,17": ["Software Design", "Linear Algebra"],
#             "58,94": ["Economics"],
#             "58,25": ["Economics"],
#             "94,25": ["Economics"],
#             "17,94": [],
#             "17,25": []
#             }


def top(coursesList):
    inDegree = defaultdict(int)
    G = defaultdict(list)
    # build grpah 
    q = deque([])
    for pre,course in coursesList:
        G[pre].append(course)
        if pre not in inDegree:
            inDegree[pre] = 0
        inDegree[course] += 1
    for k,v in inDegree.items():
        if v == 0:
            q.append(k)
    ans = []
    while q:
        course = q.popleft()
        ans.append(course)
        for c in G[course]:
            inDegree[c] -=1
            if inDegree[c] == 0:
                q.append(c)
    n = len(ans)
    mid = n //2
    print(ans)
    return  ans[mid-1] if n % 2 == 0 else ans[mid]

if __name__ == '__main__':
    prereqs_courses1 = [
        ["Foundations of Computer Science", "Operating Systems"],
        ["Data Structures", "Algorithms"],
        ["Computer Networks", "Computer Architecture"],
        ["Algorithms", "Foundations of Computer Science"],
        ["Computer Architecture", "Data Structures"],
        ["Software Design", "Computer Networks"]
    ]
    
    prereqs_courses2 = [
	["Data Structures", "Algorithms"],
	["Algorithms", "Foundations of Computer Science"],
	["Foundations of Computer Science", "Logic"]
    ]
    print(top(prereqs_courses1))
    
    print(top(prereqs_courses2))
    
                
    
    