import sys
input = sys.stdin.readline

n = int(input())
lst = set()

for _ in range(n):
    line = input().split()
    op = line[0]

    if op == "add":
        lst.add(int(line[1]))
    elif op == "remove":
        lst.discard(int(line[1]))
    elif op == "check":
        print(1 if int(line[1]) in lst else 0)
    elif op == "toggle":
        if int(line[1]) in lst:
            lst.discard(int(line[1]))
        else:
            lst.add(int(line[1]))
    elif op == "all":
        lst = set(range(1, 21))
    elif op == "empty":
        lst.clear()