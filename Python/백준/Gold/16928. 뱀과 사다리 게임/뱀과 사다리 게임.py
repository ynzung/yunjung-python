import sys
from collections import deque
input = sys.stdin.readline

N, M  = map(int, input().split())
ladder = [tuple(map(int, input().split())) for _ in range(N)]
snake =  [tuple(map(int, input().split())) for _ in range(M)]

def bfs():
    visited = [False] * 101
    q = deque()
    q.append((1, 0))  # (position, dice_count)
    visited[1] = True   # 시작 위치 방문 처리

    while q:
        position, dice_count = q.popleft()
        if position == 100: # 100에 도착하면 주사위 던진 횟수 반환
            return dice_count
        
        for dice in range(1, 7):  
            next = position + dice  # 주사위로 이동한 위치
            if next > 100:  # 다음 위치가 100보다 크면 무시
                continue
            for x, y in ladder: # 사다리가 있는지 확인
                if next == x: 
                    next = y
                    break
            for u, v in snake:  # 뱀이 있는지 확인
                if next == u:
                    next = v
                    break
            if not visited[next]:
                visited[next] = True
                q.append((next, dice_count + 1))

print(bfs())