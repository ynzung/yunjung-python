def dfs(x, y):
    # 얼음 틀 공간 벗어나면 False
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 아직 방문하지 않은 노드인 경우
    if space[x][y] == 0:
        space[x][y] = 1  # 방문한 것으로 표현(1로 만들어 주기)
        # 상하좌우
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


n, m = map(int, input().split())
space = []
for _ in range(n):
    space.append(list(map(int, input())))

# 얼음 덩어리(=영역)의 개수를 저장하는 변수
result = 0
# 모든 좌표 (i, j)를 하나씩 돌면서 체크
for i in range(n):
    for j in range(m):
        if dfs(i, j):  # 새 영역 탐색이 성공했을 때
            result += 1

print(result)