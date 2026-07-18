# 백준 1504: 특정한 최단 경로
import sys
import heapq

input = sys.stdin.readline
n, e = map(int, input().split())   # 정점 수, 간선 수     
graph = [[] for _ in range(n + 1)]  # 인접 리스트로 그래프 표현

# 간선 정보 입력
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # a에서 b로 가는 간선 추가: 거리 c
    graph[b].append((a, c)) # b에서 a로 가는 간선 추가: 거리 c

v1, v2 = map(int, input().split())  # 반드시 거쳐야 하는 정점 v1, v2

def dijkstra(start):    
    # distances[i] : 시작점 start에서 i까지 최단 거리
    distances = [float('inf')] * (n + 1)
    distances[start] = 0    # 시작점 거리는 0: 시작점 -> 시작점이기 때문
    queue = [(0, start)]    # (거리, 노드) 형태로 우선순위 큐에 삽입

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        if current_distance > distances[current_node]:  # 현재 노드에서 이미 더 짧은 경로가 발견된 경우 무시
            continue
        for neighbor, weight in graph[current_node]:    # 모든 이웃 노드를 확인하고
            distance = current_distance + weight
            if distance < distances[neighbor]:  # 더 짧은 경로 발견 시 갱신
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor)) # 갱신된 거리와 노드를 우선순위 큐에 삽입
    return distances    # 최단 거리 리스트 반환

dist_from_1 = dijkstra(1)   # 1에서 모든 노드까지의 최단 거리 계산
dist_from_v1 = dijkstra(v1) # v1에서 모든 노드까지의 최단 거리 계산
dist_from_v2 = dijkstra(v2) # v2에서 모든 노드까지의 최단 거리 계산

# v1, v2를 반드시 거쳐야 하는데, 어떤 순서로 거쳐도 상관 없기 때문에 두 가지 경우를 모두 계산해서 최솟값 선택
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]  # 1 -> v1 -> v2 -> n (v1먼저 가는 경우)
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]  # 1 -> v2 -> v1 -> n (v2먼저 가는 경우)       
result = min(path1, path2)

# 최단 경로가 존재하지 않는 경우는 무한대인 경우: 결과가 무한대보다 작은 경우에만 출력하고 그렇지 않으면 -1 출력
print(result if result < float('inf') else -1)