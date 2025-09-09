import sys
input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    line = input().split()
    command = line[0]

    if command == "push":
        stack.append(line[1])
    elif command == "pop": 
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif command == "top":
        if stack:
            print(stack[-1])  
        else:
            print(-1)

