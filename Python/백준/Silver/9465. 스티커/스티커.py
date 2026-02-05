import sys
input = sys.stdin.readline  
T = int(input())

for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    
    # dp[i][j]: j열에서 i행 스티커를 선택했을 때 얻을 수 있는 최대 점수
    dp = [[0] * n for _ in range(2)]
    
    # 첫 번째 열에서는 제약이 없음: 각 행 스티커 값이 그대로 최대 점수
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    
    # 스티커 크기가 2인 경우: 두 번째 열의 값 계산 - 첫 번째 열과 겹치지 않는 행의 값 더하기
    if n > 1:
        dp[0][1] = dp[1][0] + sticker[0][1]
        dp[1][1] = dp[0][0] + sticker[1][1]
    
    # 세 번째 열부터 마지막 열까지 계산
    # 현재 위치와 인접하지 않은 이전 열의 반대 행 값만 고려
    # dp[1][i-1]: 바로 이전 열의 아래쪽
    # dp[1][i-2]: 두 칸 전 열의 아래쪽
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + sticker[1][i]
    
    print(max(dp[0][n-1], dp[1][n-1]))