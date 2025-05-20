from collections import deque

n, m, k, x = map(int, input().split())
city = [[] for _ in range(n + 1)]
distance = [0] * (n + 1)
visited = [False] * (n + 1)


for _ in range(m):
    start, end = list(map(int, input().split()))
    city[start].append(end)


def bfs(start, k):
    queue = deque()
    queue.append(start)
    visited[start]= True

    result = []

    while queue:
        now = queue.popleft()
        for i in city[now]:
            if not visited[i]:
                visited[i] = True
                distance[i] = distance[now] + 1
                queue.append(i)
                if distance[i] == k:
                    result.append(i)
    return result

    
result = bfs(x, k)

if result:
    result.sort()
    for city_number in result:
        print(city_number)
else:
    print(-1)
    