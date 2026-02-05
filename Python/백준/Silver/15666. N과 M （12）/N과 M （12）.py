import sys
from itertools import combinations_with_replacement # 중복 조합

input = sys.stdin.readline

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))
num_lst.sort() 

# M개를 고르는 중복 조합
result = list(set(combinations_with_replacement(num_lst, M)))
result.sort()

for r in result:
    print(*r)