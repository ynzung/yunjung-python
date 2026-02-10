import sys
input = sys.stdin.readline

n = int(input())

a, b, c = map(int, input().split())
max_dp = [a, b, c]
min_dp = [a, b, c]

for _ in range(n - 1):
    a, b, c = map(int, input().split())


    # 이전 최대 최소 값들 복사 
    prev_max0, prev_max1, prev_max2 = max_dp
    prev_min0, prev_min1, prev_min2 = min_dp


    # 현재 행의 최대 값 계산
    max_dp = [
        a + max(prev_max0, prev_max1),
        b + max(prev_max0, prev_max1, prev_max2),
        c + max(prev_max1, prev_max2),
    ]

    # 현재 행의 최소 값 계산
    min_dp = [
        a + min(prev_min0, prev_min1),
        b + min(prev_min0, prev_min1, prev_min2),
        c + min(prev_min1, prev_min2),
    ]

print(max(max_dp), min(min_dp))