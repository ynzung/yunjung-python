# 세로 타일(2×1) 하나를 오른쪽에 놓는 경우, 오른쪽에 세로 1칸만 차지 → 남은 건 2×(i-1)
# 가로 타일(1×2) 두 개를 아래위로 쌓는 경우, 오른쪽에 2칸 차지 → 남은 건 2×(i-2)
# 정사각형 타일(2×2) 하나를 놓는 경우, 역시 오른쪽에 2칸 차지 → 남은 건 2×(i-2).

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * max(3, n+1)
dp[1] = 1
dp[2] = 3

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2] * 2

print(dp[n] % 10007)

