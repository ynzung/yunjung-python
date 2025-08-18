# 최대한 5kg 봉지로 배달하는게 이득
# 일단 기본적으로 3kg로 나누되, 5로 나눠 떨어지는 경우에는 5kg 봉지로만

n = int(input())

count = 0
while n >= 0:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    n -= 3
    count += 1
else:
    print(-1)