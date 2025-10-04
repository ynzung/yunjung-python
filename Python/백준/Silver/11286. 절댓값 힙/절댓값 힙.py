import sys
import heapq
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (abs(num), num))
