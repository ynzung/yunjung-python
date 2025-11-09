import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
cmds = ('D', 'S', 'L', 'R')

def next_num(c, n):
    if c == 'D':
        return (n * 2) % 10000
    if c == 'S':
        if n == 0:  
            return 9999
        return n - 1
    if c == 'L':
        return (n % 1000) * 10 + (n // 1000)
    return (n % 10) * 1000 + (n // 10)

for _ in range(T):
    a, b = map(int, input().split())
    visited = [False] * 10000
    q = deque()
    q.append((a, ""))
    visited[a] = True

    while q:
        num, cmd = q.popleft()
        if num == b:
            print(cmd)
            break
        for c in cmds:
            new_num = next_num(c, num)
            if not visited[new_num]:
                visited[new_num] = True
                q.append((new_num, cmd + c))