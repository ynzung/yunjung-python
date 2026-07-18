# 백준 17070번: 파이프 옮기기 1

import sys
input = sys.stdin.readline
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j][k]: (i, j) 위치에서 k 방향으로 파이프를 놓는 경우의 수
# k = 0: 가로, 1: 세로, 2: 대각선
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][1][0] = 1  # 초기 상태: (0, 1) 위치에 가로 방향으로 파이프가 놓여 있음    

for i in range(n):
    for j in range(2, n):
        if house[i][j] == 0:  # 현재 위치가 빈 칸인 경우
            # 가로 방향으로 파이프를 놓는 경우: 가로 방향에서 오는 경우 + 대각선 방향에서 오는 경우
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            
            # 세로 방향으로 파이프를 놓는 경우: 세로 방향에서 오는 경우 + 대각선 방향에서 오는 경우
            if i > 0:
                dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
            
            # 대각선 방향으로 파이프를 놓는 경우: 가로, 세로, 대각선 방향에서 오는 경우 모두 고려
            if i > 0 and house[i-1][j] == 0 and house[i][j-1] == 0:
                dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
                
# 최종적으로 (n-1, n-1) 위치에서 가로, 세로, 대각선 방향으로 파이프를 놓는 경우의 수를 합산
result = sum(dp[n-1][n-1])
print(result)