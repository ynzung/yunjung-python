from collections import deque

def check(a, b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count

def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    q = deque()
    q.append((begin, 0))
    
    while q:
        nxt, times = q.popleft()
        if nxt == target:
            return times
        
        for word in words:
            change = check(word, nxt)
            if change == 1:
                q.append((word, times + 1))