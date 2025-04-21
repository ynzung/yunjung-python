n, m = map(int, input().split())
ball = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(i + 1, n):
        if ball[i] != ball[j]:
            count += 1

print(count)
