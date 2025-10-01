import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    dist = [-1] * (N + 1)   # -1: 방문하지 않음 
    dist[start] = 0         # 시작 노드
    q = deque([start]) 
    while q:
        v = q.popleft()
        # v에 연결된 모든 노드 탐색
        for next in graph[v]:
            if dist[next] == -1: # 방문하지 않은 노드
                dist[next] = dist[v] + 1 # 거리 갱신
                q.append(next)   
     # 모든 정점까지의 거리 합 반환
    total = 0
    # 0번 노드는 제외하고 계산
    for d in dist[1:]:
        if d != -1:
            total += d
    return total

result = 1    # 최소 케빈 베이컨 수를 가진 노드 번호
min_sum = float('inf') 

# 모든 노드에 대해 bfs 수행
for s in range(1, N + 1):
    # s에서 시작하는 bfs 수행 후, 모든 노드까지의 거리 합 계산
    total = bfs(s)
    if total < min_sum:
        min_sum = total
        result = s

print(result)