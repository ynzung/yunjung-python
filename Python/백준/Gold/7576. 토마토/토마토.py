import sys
from collections import deque
input = sys.stdin.readline

# m: 가로, n: 세로
m, n = map(int, input().split())

# 농장 상태 입력 
farm = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 익은 토마토(값이 1) 좌표를 모두 큐에 추가
q = deque()
for x in range(n):
    for y in range(m):
        if farm[x][y] == 1:
            q.append((x, y))

# bfs
while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            # 안 익은 토마토인 경우 +1일 후 익음
            if farm[nx][ny] == 0:
                farm[nx][ny] = farm[x][y] + 1
                q.append((nx, ny))

day = 0
for x in range(n):
    for y in range(m):
        # 안 익은 토마토가 하나라도 남아있다면 -1 출력 후 종료
        if farm[x][y] == 0:
            print(-1)
            sys.exit(0)
        # 가장 마지막에 익은 날짜 갱신
        day = max(day, farm[x][y])

# 처음 익은 토마토가 1로 시작했기 때문에 실제 걸린 일수는 (최대값 - 1)
print(day - 1)