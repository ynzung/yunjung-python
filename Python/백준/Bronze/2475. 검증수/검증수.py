num = list(map(int, input().split()))
result = sum([x ** 2 for x in num])
print(result % 10)