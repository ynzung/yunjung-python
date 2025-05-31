from itertools import combinations
from collections import deque
import copy

n, m = map(int, input().split())
laboratory = [list(map(int, input().split())) for _ in range(n)]
zero_space=[]
virus_space = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for r in range(n):
    for c in range(m):
        if (laboratory[r][c]==0):
            zero_space.append((r, c))
        elif laboratory[r][c] == 2:
            virus_space.append((r, c))


wall_combination = combinations(zero_space, 3)

max_safe_area = 0

for walls in wall_combination:
    new_wall = copy.deepcopy(laboratory)
    for r, c in walls:
        new_wall[r][c] = 1
    
    queue = deque(virus_space)
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if new_wall[nx][ny] == 0:
                    new_wall[nx][ny] = 2
                    queue.append((nx, ny))

    safe_area = sum(row.count(0) for row in new_wall)
    max_safe_area = max(max_safe_area, safe_area)



print(max_safe_area)