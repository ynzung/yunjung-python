import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())

num_lst = []

# 1부터 N까지의 수 리스트
for i in range(1, N + 1):
    num_lst.append(i)

# M개를 고르는 모든 조합
result = combinations(num_lst, M)

for r in result:
    print(' '.join(map(str, r)))