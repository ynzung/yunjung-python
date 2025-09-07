import sys
input = sys.stdin.readline

N, M = map(int, (input().split()))
nums = list(map(int, input().split()))

# 시간 초과
# for _ in range(M):
#     x, y = map(int, input().split())
#     print(sum(nums[x-1:y]))   sum(nums[x-1:y])는 매번 O(N) → 시간초과


# 누적합 배열 만들기
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    prefix[i] = prefix[i-1] + nums[i-1]

# 쿼리 처리
for _ in range(M):
    x, y = map(int, input().split())
    print(prefix[y] - prefix[x-1])