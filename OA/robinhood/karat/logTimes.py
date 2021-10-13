''''
Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an access time, the ID of the user making the access, and the resource ID.
The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day.

For example:
logs1 = [
["58523", "user_1", "resource_1"],
["62314", "user_2", "resource_2"],
["54001", "user_1", "resource_3"],
["200", "user_6", "resource_5"],
["215", "user_6", "resource_4"],
["54060", "user_2", "resource_3"],
["53760", "user_3", "resource_3"],
["58522", "user_22", "resource_1"],
["53651", "user_5", "resource_3"],
["2", "user_6", "resource_1"],
["100", "user_6", "resource_6"],
["400", "user_7", "resource_2"],
["100", "user_8", "resource_6"],
["54359", "user_1", "resource_3"],
]

Example 2:
logs2 = [
["300", "user_1", "resource_3"],
["599", "user_1", "resource_3"],
["900", "user_1", "resource_3"],
["1199", "user_1", "resource_3"],
["1200", "user_1", "resource_3"],
["1201", "user_1", "resource_3"],
["1202", "user_1", "resource_3"]
]

Question 1 - Write a function that takes the logs and returns each users min and max access timestamp
Example Output:
user_3:[53760,53760]
user_2:[54060,62314]
user_1:[54001,58523]
user_7:[400,400]
user_6:[2,215]
user_5:[53651,53651]
user_4:[58522,58522]
user_8:[100,100]


Question 2 - Write a function that takes the logs and returns the resource with the highest number of accesses in any 5 minute window, together with how many accesses it saw.

Expected Output:
most_requested_resource(logs1) # => ('resource_3', 3)

Follow Up Question 3 -
Write a function that takes the logs as input, builds the transition graph and returns it as an adjacency list with probabilities. Add START and END states.

Specifically, for each resource, we want to compute a list of every possible next step taken by any user, together with the corresponding probabilities. The list of resources should include START but not END, since by definition END is a terminal state.

Expected output for logs1:
transition_graph(logs1) # =>
{
'START': {'resource_1': 0.25, 'resource_2': 0.125, 'resource_3': 0.5, 'resource_6': 0.125},
'resource_1': {'resource_6': 0.333, 'END': 0.667},
'resource_2': {'END': 1.0},
'resource_3': {'END': 0.4, 'resource_1': 0.2, 'resource_2': 0.2, 'resource_3': 0.2},
'resource_4': {'END': 1.0},
'resource_5': {'resource_4': 1.0},
'resource_6': {'END': 0.5, 'resource_5': 0.5}
}

For example, of 8 total users, 4 users have resource_3 as a first visit (user_1, user_2, user_3, user_5), 2 users have resource_1 as a first visit (user_6, user_22), 1 user has resource_2 as a first visit (user_7), and 1 user has resource_6 (user_8) so the possible next steps for START are resource_3 with probability 4/8, resource_1 with probability 2/8, and resource_2 and resource_6 with probability 1/8.

These are the resource paths per user for the first logs example, ordered by access time:
{
'user_1': ['resource_3', 'resource_3', 'resource_1'],
'user_2': ['resource_3', 'resource_2'],
'user_3': ['resource_3'],
'user_5': ['resource_3'],
'user_6': ['resource_1', 'resource_6', 'resource_5', 'resource_4'],
'user_7': ['resource_2'],
'user_8': ['resource_6'],
'user_22': ['resource_1'],
}

Expected output for logs2:
transition_graph(logs2) # =>
{
'START': {'resource_3': 1.0},
'resource_3': {'resource_3: 0.857, 'END': 0.143}
}
'''
# https://leetcode.com/discuss/interview-question/1144222/karat-interview-for-robinhood-swe

from collections import defaultdict
from typing import DefaultDict


def solveOne(logs):
    ans = dict()
    for time,id,resource in logs:
        time = int(time)
        if id not in ans:
            ans[id] = [time,time]
        else:
            if time < ans[id][0]:
                ans[id][0] = time
            elif time > ans[id][1]:
                ans[id][1] = time 
    return ans
    
import heapq as hq

def solveTwo(logs):
    resourceMap = defaultdict(list)
    res = 0
    resName = ''
    logs.sort(key=lambda w:(w[2],w[0]))
    for time,id,resource in logs:
        time = int(time)
        while resourceMap[resource] and time - resourceMap[resource][0] > 300:
            hq.heappop(resourceMap[resource])
        
        hq.heappush(resourceMap[resource],time)
        if len(resourceMap[resource]) > res:
            resName = resource
            res = len(resourceMap[resource])
    return resName,res 
        
        
                    
    

def build_transition_graph(logs):
    
    user_dict = {}
    res_dict = {}
    # Sort the logs by usr and then by ts. use int() since it is string and sorting wont work well with string
    logs.sort(key=lambda x: (x[1], int(x[0])))

    # Fill in the user dict, adding start and end for transitions
    for ts, usr, res in logs:
        if usr not in user_dict:
            user_dict[usr] = ['START']
        user_dict[usr].append(res)

    for usr in user_dict:
        user_dict[usr].append('END')

    # Iterate through the user dict and set counts per transition, keeping track of total users per resource
    for usr in user_dict:
        for i in range(1, len(user_dict[usr])):
            prev_res, cur_res = user_dict[usr][i-1], user_dict[usr][i]
            if prev_res not in res_dict:
                res_dict[prev_res] = {'total': 0}
            if cur_res not in res_dict[prev_res]:
                res_dict[prev_res][cur_res] = 0
            res_dict[prev_res][cur_res] += 1
            res_dict[prev_res]['total'] += 1

    # Fill the transition graph with resources and their probabilities
    transition_graph = {}
    for res in res_dict:
        transition_graph[res] = {}
        for nex_res in res_dict[res]:
            if nex_res == 'total':
                continue
            prob = res_dict[res][nex_res]/res_dict[res]['total']
            transition_graph[res][nex_res] = prob
    return transition_graph

if __name__ == '__main__':
    logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
    ]


    logs2 = [
    ["300", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"]
    ]
    
    print(build_transition_graph(logs1))
    # print("x"*100)
    # print(build_transition_graph(logs2))
    # print("x"*100)
    # print(solveTwo(logs1))
    