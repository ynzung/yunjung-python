import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())

num_lst = list(map(int, input().split()))

# M개를 고르는 모든 순열
result = list(permutations(num_lst, M))
result.sort()

for r in result:
    print(' '.join(map(str, r)))