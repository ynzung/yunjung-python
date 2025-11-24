import sys
from itertools import combinations_with_replacement # 중복 조합

input = sys.stdin.readline

N, M = map(int, input().split())

num_lst = []

# 1부터 N까지의 수 리스트
for i in range(1, N + 1):
    num_lst.append(i)

# M개를 고르는 중복 조합
result = combinations_with_replacement(num_lst, M)

for r in result:
    print(' '.join(map(str, r)))