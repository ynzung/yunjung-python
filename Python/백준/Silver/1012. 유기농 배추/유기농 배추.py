import sys

# 런타임 에러 발생 방지
# 재귀 깊이 기본 제한이 1000이기 때문에, 이를 1,000,000으로 늘려줌
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1] 

    # 현재 위치 방문 처리
    visited[x][y] = True
    # 상하좌우 위치 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 공간을 벗어나지 않고, 방문하지 않았으면서 배추가 심어져 있는 경우
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and space[nx][ny] == 1:
            # 재귀적으로 방문
            dfs(nx, ny)
    
T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    space = [[0] * m for _ in range(n)]

    # 배추 심기
    for _ in range(k) :
        x, y = map(int, input().split())
        space[y][x] = 1

    visited = [[False] * m for _ in range(n)]
    count = 0

    # 모든 위치를 돌면서 dfs
    for i in range(n):
        for j in range(m):
            # 배추가 심어져 있고, 방문하지 않은 경우
            if space[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                count += 1
    print(count)

