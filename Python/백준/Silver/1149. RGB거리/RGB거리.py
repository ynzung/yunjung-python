import sys
input = sys.stdin.readline

n = int(input())    # 집의 수
costs = [list(map(int, input().split())) for _ in range(n)] # 각 집을 R(0), G(1), B(2)로 칠하는 비용

for i in range(1, n):
    costs[i][0] += min(costs[i-1][1], costs[i-1][2])    # i번째 집을 빨강으로 칠할 때의 최소 비용
    costs[i][1] += min(costs[i-1][0], costs[i-1][2])    # i번째 집을 초록으로 칠할 때의 최소 비용
    costs[i][2] += min(costs[i-1][0], costs[i-1][1])    # i번째 집을 파랑으로 칠할 때의 최소 비용
print(min(costs[n-1]))  # 마지막 집까지 칠하는 데 드는 최소 비용
  
