n = int(input())

info = []

for i in range(n):
    info.append(tuple(map(str, input().split())))

info.sort(key=lambda x:int(x[1]))


print(" ".join(result_name[0] for result_name in info))