import sys
import heapq
input = sys.stdin.readline

N = int(input())
x = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if x:  
            print(heapq.heappop(x))
        else:  
            print(0)
    elif num > 0:
        heapq.heappush(x, num)

