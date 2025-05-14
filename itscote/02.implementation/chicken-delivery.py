import itertools

# 입력 받기
n, m = map(int, input().split())

# 도시 정보 입력 받기
city = [list(map(int, input().split())) for _ in range(n)]

home = []     # 집 좌표 리스트
chicken = []  # 치킨집 좌표 리스트

# 집, 치킨집의 좌표 구별해서 저장
for row in range(n):
    for col in range(n):
        if city[row][col] == 1:
            home.append([row, col])
        elif city[row][col] == 2:
            chicken.append([row, col])

# 집, 각 치킨집 사이 거리 계산
chicken_dist = []
for c in chicken:
    dist = [abs(h[0] - c[0]) + abs(h[1] - c[1]) for h in home]
    chicken_dist.append(dist)

# 치킨집 중 m개 고르는 경우의 조합 
combinations = list(itertools.combinations(chicken_dist, m))

result = float('inf')  # 최소 거리 초기화 (무한대로 설정)

# 각 치킨집 m개 선택한 경우에 대해 도시의 치킨거리 계산
for case in combinations:
    city_distance = 0  # 각 경우의 치킨 거리 합 초기화

    # 각 집에 대해 최소 치킨 거리 계산
    for h in range(len(home)):
        # 해당 집과의 최소 거리 찾기
        min_dist = min(case[i][h] for i in range(m))
        city_distance += min_dist

    # 최소 도시 치킨 거리 찾기
    result = min(result, city_distance)

print(result)