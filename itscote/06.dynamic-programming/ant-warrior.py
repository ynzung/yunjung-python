n = int(input())
array = list(map(int, input().split()))

d=[0] * 100

d[0] = array[0]  # 첫 번째 칸은 첫 번째 계단의 점수로 초기화
d[1] = max(array[0], array[1])  # 두 번째 칸은 첫 번째와 두 번째 계단 중 큰 점수로 초기화
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])  # 현재 칸의 점수 계산
print(d[n - 1])  # 마지막 칸의 점수 출력