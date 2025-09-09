T = int(input())
sequences = [int(input()) for _ in range(T)]

m = max(sequences)
dp = [0] * (m + 1)
dp[1], dp[2], dp[3] = 1, 1, 1

for i in range(4, m + 1):
    dp[i] = dp[i - 3] + dp[i - 2]

for x in sequences:
    print(dp[x])