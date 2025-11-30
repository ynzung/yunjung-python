import sys
from itertools import permutations

input = sys.stdin.readline

N, M = map(int, input().split())
num_lst = list(map(int, input().split()))

# M개를 고르는 모든 순열 (중복되는 수열을 여러 번 출력하면 안됨)
result = list(set(permutations(num_lst, M)))
result.sort()

for r in result:
    print(*r)