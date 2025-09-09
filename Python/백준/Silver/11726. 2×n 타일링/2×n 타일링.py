import sys
input = sys.stdin.readline

n = int(input())
# 런타임 에러
# dp = [0] * (n+1)
# dp[1] = 1
# dp[2] = 2
dp = [0] * (max(3, n+1))   # 최소 크기를 3으로 보장
dp[1], dp[2] = 1, 2

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % 10007)
