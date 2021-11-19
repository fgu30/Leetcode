import bisect

# A = ["mobile","mouse","moneypot","monitor","mousepad"]

# def suggestedProducts(A, word):
#     A.sort()
#     res, prefix, i = [], '', 0
#     for c in word:
#         prefix += c
#         print(i)
#         print(prefix)
#         i = bisect.bisect_left(A, prefix, i)
#         # n a[:i] have e <= x, right
#         # all e in a[:i] have e < x, and all e in left
#         res.append([w for w in A[i:i + 3] if w.startswith(prefix)])
#     return res

# print(suggestedProducts(A,"mouse"))


#-------

# test = ["apple","blux","bluxberry","mango","kiwi"]

# test.sort()

# def solve(test,prefix):
#     i = bisect.bisect_right(test,prefix)
    
#     return i
# print(solve(test,'blue'))
    
a = 'pre'
b = 'prefix'
print(b.startswith(a))