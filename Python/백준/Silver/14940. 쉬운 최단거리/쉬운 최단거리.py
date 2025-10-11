import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    visited = [[-1] * M for _ in range(N)]
    queue = deque([(x, y)])
    visited[x][y] = 0   # 시작 지점이 2이기 때문에 이걸 꼭 0으로 초기화해야 함!!!!!

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 안이고 벽이 아니고 아직 방문 안한 경우
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 0 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

    return visited

# 시작 지점 = 2에서 한 번만 bfs
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            result = bfs(i, j)

# 벽은 0, 그 외는 도달 거리 출력(도달 불가한 경우는 -1이 출력됨)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(0, end=' ')
        else:
            print(result[i][j], end=' ')
    print()