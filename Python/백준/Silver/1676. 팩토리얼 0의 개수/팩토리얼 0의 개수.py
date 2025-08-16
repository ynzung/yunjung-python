import math

n = int(input())
result = str(math.factorial(n)) 

cnt = 0
for ch in reversed(result):
    if ch == '0':
        cnt += 1
    else:
        break

print(cnt)