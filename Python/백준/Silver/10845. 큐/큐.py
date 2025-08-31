
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()

for _ in range(n):
    line = input().split()
    command = line[0]

    if command == "push":
        queue.append(line[1])
    elif command == "pop": 
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif command == "size":
        print(len(queue))
    elif command == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif command == "front":
        if queue:
            print(queue[0])  
        else:
            print(-1)
    elif command == "back":
        if queue:
            print(queue[-1])  
        else:
            print(-1)



