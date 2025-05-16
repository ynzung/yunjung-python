from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

# 이동 방향 - 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 미로 공간 벗어나면 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽이면 무시
            if maze[nx][ny] == 0:
                continue
            # 처음 방문한 곳이면 거리 + 1
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    # 도착지 값 = 최단 거리
    return maze[n - 1][m - 1]

print(bfs(0, 0))