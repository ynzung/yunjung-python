# 첫번째 시도 (시간초과이슈)

# n = int(input())
# result = float('inf')

# homes = list(map(int, input().split()))  # 집의 위치
# homes.sort()


# for i in range(homes[0], homes[-1]+1, 1):
#     min_dist = 0
#     for home in homes:
#         min_dist += abs(home - i)
#     if min_dist < result:
#         result = min_dist
#         antenna = i

    

# print(antenna)

n = int(input())
homes = list(map(int, input().split()))
homes.sort()

print(homes[(n - 1) // 2])