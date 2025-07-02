n = int(input())

info = []

for i in range(n):
    info.append(input().split())

info.sort(key=lambda x:(-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for j in info:
    print(j[0])
