from collections import deque

n, k = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())
virus_space = []

for r in range(n):
    for c in range(n):
        if (space[r][c]) != 0:
            virus_space.append((space[r][c], 0, r, c)) 

def infection(space, virus_space, s):
    n = len(space)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    virus_space.sort()
    queue = deque(virus_space)  

    while queue:
        virus, time, x, y = queue.popleft()

        if time == s:
            break

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if space[nx][ny] == 0:
                    space[nx][ny] = virus
                    queue.append((virus, time + 1, nx, ny))
    
infection(space, virus_space, s)

print(space[x-1][y-1])