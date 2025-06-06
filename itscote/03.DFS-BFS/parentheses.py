from collections import deque

def is_balance(s):
    open_count, close_count = 0, 0
    for i in range(len(s)):
        if s[i] == "(":
            open_count += 1
        else:
            close_count += 1 
        if open_count == close_count:
            return s[:i+1], s[i+1:]

def is_correct(s):
    verify_direction = deque()
    for i in s:
        if i == "(":
            verify_direction.append(i)
        else:
            if not verify_direction:
                return False
            else:
                verify_direction.pop()
    return not verify_direction
        
def reverse(s):
    result = ""
    for i in s:
        if i == "(":
            result += ")"
        else: 
            result += "("
    return result

def solution(p):
    if not p: 
        return ""
    u, v = is_balance(p)
    if is_correct(u):
        return u + solution(v)
    else:
        return "(" + solution(v) + ")" + reverse(u[1:-1])


w = input()
print(solution(w))