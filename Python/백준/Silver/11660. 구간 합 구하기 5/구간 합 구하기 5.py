# 11660
# 구간 합 구하기 5

import sys
input = sys.stdin.readline

# n: 배열의 크기, m: 구간 합을 구할 횟수
n, m = map(int, input().split())

# 원본 n x n 배열 입력
array = [list(map(int, input().split())) for _ in range(n)]

# 누적 합 배열 초기화
# dp[i][j]는 (1, 1)부터 (i, j)까지의 모든 원소 합을 의미
# 인덱스 계산을 편하게 하기 위해 (n+1) x (n+1) 크기로 생성
dp = [[0] * (n+1) for _ in range(n+1)]  

# 누적 합 배열 채우기
for i in range(1, n + 1):
    for j in range(1, n+1):
        # dp[i][j] = 왼쪽 영역 + 위쪽 영역 - 중복된 영역 + 현재 값
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + array[i-1][j-1]

# m개의 구간 합 계산
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    # 구간 합 계산:
    # (1,1)~(x2,y2) 전체에서
    # (1,1)~(x1-1,y2) 위쪽 영역과 (1,1)~(x2,y1-1) 왼쪽 영역을 빼고
    # 두 번 빠진 (1,1)~(x1-1,y1-1) 영역을 다시 더함
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(result)
