import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
parent = [-1] * (N + 1)  # 부모 노드 저장할 리스트

def bfs(start):
    queue = deque([start])
    parent[start] = 0  # 루트 노드 1의 부모는 0으로 설정

    while queue:
        node = queue.popleft()
        for next in tree[node]:
            if parent[next] == -1:  # 부모가 아직 없는 경우
                parent[next] = node
                queue.append(next)

bfs(1)
for i in range(2, N + 1):
    print(parent[i])