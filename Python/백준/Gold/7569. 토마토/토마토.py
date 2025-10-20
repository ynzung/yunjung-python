import sys
from collections import deque
input = sys.stdin.readline

# m 열(가로), n 행(세로), h 높이(층)
m, n, h = map(int, input().split())

farm = []   # 3차원 리스트로 농장(토마토 상자) 상태 저장

# 층(h) 단위로 입력받기
for _ in range(h):
    floor = [list(map(int, input().split())) for _ in range(n)]
    farm.append(floor)

# 이동 방향 (위, 아래, 앞, 뒤, 왼쪽, 오른쪽)
dz = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, -1, 1]

# 익은 토마토(값이 1인 칸)들의 좌표를 전부 큐에 추가 (다중 시작점)
q = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if farm[z][x][y] == 1:
                q.append((z, x, y))

# bfs
while q:
    z, x, y = q.popleft()
    for i in range(6):
        nz = z + dz[i]
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m: # 범위 안에 있고
            if farm[nz][nx][ny] == 0:   # 아직 익지 않은 토마토라면
                farm[nz][nx][ny] = farm[z][x][y] + 1    # 현재 토마토의 날짜 + 1로 갱신 (며칠째에 익었는지 기록)
                q.append((nz, nx, ny))  # 새로 익은 토마토의 좌표를 큐에 추가

day = 0  # 며칠 걸렸는지 저장
for z in range(h):
    for x in range(n):
        for y in range(m):
            if farm[z][x][y] == 0:   # 안 익은 토마토(0)가 하나라도 남아있다면 -1 출력 후 종료
                print(-1)
                sys.exit(0)
            day = max(day, farm[z][x][y])    # 전체 중 가장 큰 값(마지막으로 익은 날)을 갱신

print(day - 1)  # 처음 익은 토마토가 1로 시작했기 때문에 실제 걸린 일수는 (최대값 - 1)