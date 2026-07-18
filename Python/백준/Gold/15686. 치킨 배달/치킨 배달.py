# 백준 15686번: 치킨 배달

import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

houses = []  # 집 위치
chickens = []  # 치킨집 위치

# 집, 치킨집 위치 저장
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j)) 

result = float('inf')

# 치킨집 조합을 구해서 각 집과의 거리를 계산하여 최소값을 찾음
for comb in combinations(chickens, m):
    total = 0
    for hr, hc in houses:
        dist = min(abs(hr - cr) + abs(hc - cc) for cr, cc in comb)
        total += dist
    result = min(result, total)

print(result)