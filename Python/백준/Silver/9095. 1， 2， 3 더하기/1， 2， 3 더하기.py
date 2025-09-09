n = int(input())
nums=[int(input()) for _ in range(n)]
m = max(nums)  # 입력들 중 최대값까지만 DP 계산

dp = [0] * (m + 1)
dp[1] = 1        
dp[2] = 2       
dp[3] = 4       

for i in range(4, m + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for x in nums:
    print(dp[x])