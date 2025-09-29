import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
map = [[int(x) for x in input().strip()] for _ in range(N)] 

visited = [[-1] * (N) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y] = 0 # 방문 처리

    count = 1   # 집 개수 (x, y) 집은 이미 단지에 포함
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N: # map 안에 있고
                if map[nx][ny] == 1 and visited[nx][ny] == -1: # 집이면서 방문하지 않은 곳
                    visited[nx][ny] = 0 # 방문 처리
                    q.append((nx, ny)) 
                    count += 1  # 집 개수 증가
    return count

total_count = 0 # 총 단지 수
house =  [] # 각 단지 내 집의 수
for i in range(N): 
    for j in range(N):
        if map[i][j] == 1 and visited[i][j] == -1: # 집이면서 방문하지 않은 곳
            total_count += 1
            house.append(bfs(i,j))  

print(total_count)
house.sort()
for h in house:
    print(h)