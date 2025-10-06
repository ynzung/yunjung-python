import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]


def dfs(start):
    visited = [False] * N
    queue = deque([start])

    while queue:
        node = queue.popleft()

        for next in range(N):
            if graph[node][next] == 1 and not visited[next]:    # 연결되어 있고 방문하지 않은 노드
                visited[next] = True
                queue.append(next)
    return visited  # 시작 노드에서 도달 가능한 노드 정보 반환

# 모든 i에서 j로 가는 경로 있는지 확인
for i in range(N):  
    result = dfs(i)  # i에서 방문 가능한 노드 리스트
    for j in range(N):
         # result[j]가 true면 i에서 j로 가는 경로 있는거
        if result[j]:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
    