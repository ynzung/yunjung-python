import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[ ] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    # 현재 노드와 연결된, 방문 안햇던 다른 노드 재귀적 호출하면서 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)

# 연결된 요소의 개수
count = 0
visited = [False] * (N+1)

# 모든 노드를 다 돌면서 방문하지 않은 노드가 있으면 dfs 호출
for i in range(1, N+1):
    if not visited[i]:
        dfs(i, visited)
        count += 1  

print(count)    