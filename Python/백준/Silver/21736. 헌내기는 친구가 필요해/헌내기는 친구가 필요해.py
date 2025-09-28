import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, M = map(int, input().split())

compus = [list(input().strip()) for _ in range(N)]

# 도연이 위치 찾아서 x, y에 좌표 저장
x, y = 0, 0
for i in range(N):
    for j in range(M):
        if compus[i][j] == 'I':
            x, y = i, j
            break

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


friends = 0

def dfs(x, y):
    # 방문한 곳을 벽으로 바꿈
    global friends
    compus[x][y] = 'X'
    # 상하좌우 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            # 벽이거나 이미 방문한 곳이면 continue
            if compus[nx][ny] == 'X':
                continue
            elif compus[nx][ny] == "O":
                dfs(nx, ny)
            elif compus [nx][ny] == "P":
                friends += 1
                dfs(nx, ny)

dfs(x, y)
if friends == 0:
    print("TT")
else:
    print(friends)