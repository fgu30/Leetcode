def helper(num,pre_op,stack):
    if pre_op == '+': stack.append(num)
    elif pre_op == '-': stack.append(-1* num)
    elif pre_op == '*': stack.append(stack.pop()*num)
    elif pre_op == '/': stack.append(int(stack.pop()/ num))

def solve(chars):
    stack = []
    num,pre_op = 0, '+'
    
    while len(chars)>0:
        char = chars.pop(0)
        
        if '0' <= char <= '9':
            num = num*10 + int(char)
        elif char in '+-*/':
            helper(num,pre_op,stack)
            num,pre_op = 0,char
        elif char == '(':
            num = solve(chars)
        elif char == ')':
            helper(num,pre_op,stack)
            break
    return sum(stack)
s = '((1+2)*3)/4'

print(solve(list(s) +'[' + ']'))

    