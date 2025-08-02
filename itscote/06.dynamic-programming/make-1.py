n = int(input())

# make_1: 1을 만들기 위한 최소 연산 횟수 계산
def make_1(n):  
    # dp[i]: i를 1로 만들기 위한 최소 연산 횟수
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1  # -1 연산
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 5 == 0:              
            dp[i] = min(dp[i], dp[i // 5] + 1)
    return dp[n]

result = make_1(n)
print(result)   