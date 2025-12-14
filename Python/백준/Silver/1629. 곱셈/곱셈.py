import sys
input = sys.stdin.readline

a, b, c  = map(int, input().split())

# 시간초과
# result = (a ** b) % c

# 파이썬 내장 함수: pow (밑, 지수, 나머지)
result = pow(a, b, c)

print(result)