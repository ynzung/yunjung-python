# 백준 12865번: 평범한 배낭

import sys
input = sys.stdin.readline
n, k = map(int, input().split())

# dp[w] : "현재까지 고려한 물건들"로 배낭 무게 한도가 w일 때 얻을 수 있는 "최대 가치"
dp = [0] * (k + 1)      

for _ in range(n):
    weight, value = map(int, input().split())

    # 0/1 배낭에서 1차원 dp를 쓸 때는 반드시 "역순"으로 돈다.
    #
    # 이유:
    # - 작은 w -> 큰 w(정방향)으로 돌면
    #   현재 물건을 고려하기 전 상태가 아니라 이미 현재 물건이 반영된 상태를 참조하게 된다.
    #   그러면 해당 물건을 여러 번 넣는 효과가 생겨 "완전 배낭(무한 선택)"이 되어버림.
    #
    # - 그래서 큰 w -> 작은 w(역방향)으로 돌면,
    #   dp[w - weight]는 "이번 물건을 반영하기 전 상태"를 보장하게 되고
    #   물건을 딱 1번만 사용하는 0/1 조건을 지킬 수 있다.
    for w in range(k, weight - 1, -1):
        # 1) 현재 물건을 안 넣는 경우: dp[w]
        # 2) 현재 물건을 넣는 경우:
        #    - w에서 weight만큼 무게를 쓰므로 남는 한도는 (w - weight)
        #    - 그때의 최대 가치 dp[w - weight]에 현재 물건 가치 value를 더함
        dp[w] = max(dp[w], dp[w - weight] + value)

# 배낭 무게 한도가 k일 때의 최대 가치 출력
print(dp[k])