import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

picture = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    color = picture[x][y]

    while q:
        r, c  = q.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if picture [nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

# 적록색약이 아닌 경우
visited = [[False] * n for _ in range(n)]
normal = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            normal += 1

# 적록색약인 경우 다시 visited 초기화
visited = [[False] * n for _ in range(n)]
red_green = 0
for i in range(n):
    for j in range(n):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            red_green += 1



print(normal, red_green)

