from collections import deque

n, l, r = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(r_start, c_start): # r, c와 겹치지 않게 매개변수 이름 변경
    queue = deque()
    union = []
    queue.append((r_start, c_start))
    union.append((r_start, c_start))
    visited[r_start][c_start] = 1

    # print(f"  BFS started at ({r_start}, {c_start})") # 디버깅용
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(A[nx][ny] - A[x][y]) <= r:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    # print(f"    Added ({nx}, {ny}) to union. Diff: {abs(A[nx][ny] - A[x][y])}") # 디버깅용
    return union               

result = 0
while True:
    visited = [[0 for _ in range(n)] for _ in range(n)]
    flag = 0
    # print(f"\n--- Day {result + 1} ---") # 디버깅용
    for r_idx in range(n): # r과 겹치지 않게 매개변수 이름 변경
        for c_idx in range(n): # c와 겹치지 않게 매개변수 이름 변경
            if visited[r_idx][c_idx] == 0:
                country = bfs(r_idx, c_idx)
                
                if len(country) > 1:
                    flag = 1
                    people = sum(A[x][y] for x, y in country) // len(country)
                    # print(f"  Union found: {country}, Avg People: {people}") # 디버깅용
                    for x, y in country:
                        A[x][y] = people
    
    if flag == 0:
        break

    result += 1
    # print(f"  Current A after movement: {A}") # 디버깅용

print(result)