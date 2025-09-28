import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            # 최대값을 출력하기 위해 음수로 저장한 값을 다시 양수로 바꿔서 출력
            print(-heapq.heappop(heap))
    else:
        # 음수로 저장해서 최소 힙을 최대 힙처럼 사용
        heapq.heappush(heap, -x)
        