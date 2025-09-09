n = int(input())
scores = [int(input()) for _ in range(n)]

if n < 3:
    print(sum(scores))
else:
    dp = [0] * n
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]
    dp[2] = max(scores[0] + scores[2], scores[1] + scores[2])
    for i in range(3, n):
        dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])
    print(dp[-1])