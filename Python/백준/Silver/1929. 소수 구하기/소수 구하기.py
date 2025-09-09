import math

# m과 n 사이의 수 중에 소수 출력하기
m, n = map(int, input().split())
result = []

for i in range(m, n+1):
    if i < 2:
        continue
    is_prime = True
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        result.append(i)

print("\n".join(str(i) for i in result))