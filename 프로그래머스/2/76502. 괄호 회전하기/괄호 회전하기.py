from collections import deque

def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
            
    return len(stack) == 0

def solution(s):
    answer = 0
    q = deque(s)
    
    for _ in range(len(s)):
        if is_valid(q):
            answer += 1
        q.rotate(-1)  # 왼쪽으로 1칸 회전
        
    return answer