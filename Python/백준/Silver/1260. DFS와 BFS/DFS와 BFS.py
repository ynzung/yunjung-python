import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 연결
    graph[a].append(b)
    graph[b].append(a)

def dfs(start, visited):
    visited[start] = True
    print(start, end=' ')
    # 오름차순으로 방문 탐색 (방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문)
    for i in sorted(graph[start]):
        # 방문하지 않은 노드라면 재귀적으로 방문
        if not visited[i]:
            dfs(i, visited)

def bfs(start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        # 큐에서 하나의 원소를 뽑아서 출력
        v = queue.popleft()
        print(v, end=' ')
        # 오름차순으로 방문 탐색 (방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문)
        for i in sorted(graph[v]):
            # 방문하지 않은 노드라면 큐에 삽입
            if not visited[i]:
                visited[i] = True
                queue.append(i)


visited = [False] * (n + 1)
dfs(v, visited)

print()

visited = [False] * (n + 1)   
bfs(v, visited)


