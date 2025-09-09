computer = int(input())
linked_computer = int(input())
space = [[] for _ in range(computer + 1)]

for _ in range(linked_computer):
    a, b = map(int, input().split())
    space[a].append(b)
    space[b].append(a)

visited = [False] * (computer + 1)

def dfs(node):
    visited[node] = True
    count = 1 if node != 1 else 0   # 시작점 1에서는 count하지 않음
    for next_node in space[node]:
        if not visited[next_node]:  # 다음 지점 방문 안했을 경우
            count += dfs(next_node) # 다음 지점 방문, 새로 감염되는 모든 노드 수를 더함
    return count    

print(dfs(1))