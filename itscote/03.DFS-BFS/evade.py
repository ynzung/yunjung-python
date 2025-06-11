from itertools import combinations
import copy

n = int(input())
space = [input().split() for _ in range(n)]
X_space = []
T_space = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for r in range(n):
    for c in range(n):
        if space[r][c] == "X":
            X_space.append((r, c))
        if space[r][c] == "T":
            T_space.append((r, c))

result = False

for impediment in combinations(X_space, 3):
    copied_space = copy.deepcopy(space)
    for (r, c) in impediment:
        copied_space[r][c] = "O"

    success = True  

    for x, y in T_space:
        for d in range(4):
            nx, ny = x, y
            while 0 <= nx < n and 0 <= ny < n:
                if copied_space[nx][ny] == "O":
                    break
                if copied_space[nx][ny] == "S":
                    success = False  
                    break
                nx += dx[d]
                ny += dy[d]
            if not success:
                break
        if not success:
            break

    if success: 
        result = True
        break

if result:
    print("YES")
else:
    print("NO")