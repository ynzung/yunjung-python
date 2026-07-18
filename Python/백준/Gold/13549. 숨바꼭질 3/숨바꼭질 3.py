# 백준 13549번: 숨바꼭질 3
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
MAX = 100000
visited = [False] * (MAX + 1)   

# BFS
dq = deque()
dq.append((n, 0))  # (수빈이 현재 위치, 현재 시간)
visited[n] = True  # 수빈이 현재 위치 방문 처리

while dq:
    position, time = dq.popleft()

    # 동생을 찾으면 시간 출력 후 종료
    if position == k:
        print(time)
        break

    # 순간 이동: 시간 0초
    next_pos = position * 2
    if 0 <= next_pos <= MAX and not visited[next_pos]:
        visited[next_pos] = True
        dq.appendleft((next_pos, time))  # 비용이 0이므로 앞에 추가

    # 걷기: 시간 1초
    for next_pos in (position - 1, position + 1):
        if 0 <= next_pos <= MAX and not visited[next_pos]:
            visited[next_pos] = True
            dq.append((next_pos, time + 1))  # 비용이 1이므로 뒤에 추가 

