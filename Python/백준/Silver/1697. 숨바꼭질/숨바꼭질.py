import sys
from collections import deque

input = sys.stdin.readline
subin, sister = map(int, input().split())

def bfs():
    visited = [False] * 100001
    q = deque([(subin, 0)])  # (현재 위치, 시간)
    visited[subin] = True   # 시작 위치 방문 처리

    while q:
        # pos: 현재 위치, t: 현재까지 걸린 시간
        pos, time = q.popleft()
        if pos == sister:
            return time # 동생 찾았을 때 걸린 시간 리턴

        # 수빈이가 이동할 수 있는 세 가지 방법을 튜플로 모두 시도
        for next in (pos - 1, pos + 1, pos * 2):
            # 다음 위치가 유효하고 방문하지 않은 곳이라면 큐에 추가
            if 0 <= next <= 100000 and not visited[next]:
                visited[next] = True
                # 다음 위치와 시간(1초 증가)을 큐에 추가
                q.append((next, time + 1))

print(bfs())