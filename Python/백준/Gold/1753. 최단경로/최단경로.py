# 백준 1753: 최단경로
import sys
import heapq    

input = sys.stdin.readline
v, e = map(int, input().split())       # 정점 수, 간선 수
start = int(input())                   # 시작점
graph = [[] for _ in range(v + 1)]     # 인접 리스트 초기화

# 간선 정보 입력
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # 방향 그래프이기 때문에 a에서 b로 가는 간선만 추가: 거리 c

def dijkstra(start):
    # distances[i] : 시작점 start에서 i까지 최단 거리
    distances = [float('inf')] * (v + 1) 
    distances[start] = 0                   # 시작점 거리 0
    queue = [(0, start)]                   # (거리, 노드) 형태로 우선순위 큐에 삽입

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:  # 현재 노드에서 이미 더 짧은 경로 발견된 경우 무시
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:        # 더 짧은 경로 발견 시 갱신
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))  # 갱신된 거리와 노드를 우선순위 큐에 삽입
    return distances

# 시작점에서 모든 노드까지 최단 거리 계산
dist_from_start = dijkstra(start)

# 결과 출력: 무한대인 경우 INF 출력 / 무한대 아닌 경우 최단 거리 출력
for i in range(1, v + 1):
    if dist_from_start[i] != float('inf'):
        print(dist_from_start[i])
    else:
        print("INF")