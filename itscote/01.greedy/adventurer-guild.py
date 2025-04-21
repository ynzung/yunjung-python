n = int(input())
data = list(map(int,input().split()))
count = 0

data.sort(reverse=True)
print(data)

while data:
    maximum = data.pop()
    if maximum > len(data):
        break
    for i in range(maximum - 1):
        del data[i]
    count += 1


print(count)
