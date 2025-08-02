n, m = map(int, input().split())

array =[]
for i in range(n):
    array.append(int(input()))

d= [10001] * (m + 1)
d[0] = 0  # 0원을 만드는 데 필요한 동전의 개수는 0개
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:  # 이전 금액이 만들 수 있는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)
if d[m] == 10001:
    print(-1)  # 만들 수 없는 경우
else:
    print(d[m])