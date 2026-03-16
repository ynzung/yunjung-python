# 백준 1967: 트리의 지름
import sys
sys.setrecursionlimit(10**6)
from collections import deque   

input = sys.stdin.readline
n = int(input())
tree = [[] for _ in range(n + 1)]  

for _ in range(n - 1):
    parent, child, weight = map(int, input().split())
    tree[parent].append((child, weight))
    tree[child].append((parent, weight))

def dfs(current):
    for nxt, dist in tree[current]: # 현재 노드에서 인접한 노드와 그 사이의 거리 확인
        if visited[nxt] == -1:  # 방문하지 않은 노드인 경우에만 탐색
            visited[nxt] = visited[current] + dist  # 현재 노드까지의 거리 + 현재 노드와 nxt 사이의 거리
            dfs(nxt) # nxt 노드에서 다시 DFS 수행하여 그 노드에서 가장 멀리 있는 노드까지의 거리 계산
 
# 1. 루트 노드(1)부터 시작해서 가장 멀리 있는 노드를 구함
visited = [-1] * (n + 1)
visited[1] = 0
dfs(1)
start_node = visited.index(max(visited))

# 2. 1번에서 구한 노드에서 시작해서 다시 가장 멀리 있는 노드를 구함
visited = [-1] * (n + 1)
visited[start_node] = 0
dfs(start_node)

# 트리의 지름 출력
print(max(visited))