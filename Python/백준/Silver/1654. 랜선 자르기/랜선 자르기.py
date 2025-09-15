import sys
input = sys.stdin.readline

k, n = map(int, input().split())
each_length = [int(input()) for _ in range(k)]

start, end = 1, max(each_length)
result = 0

while start <= end:
    mid = (start + end) // 2
    count = 0   # 잘라서 만들 수 있는 랜선의 개수
    for i in each_length:
        count += i // mid
    
    if count >= n:  # n개보다 많으면 더 길게 자를 수 있어서 +1
        start = mid + 1
    else:   # n개보다 적으면 짧게 잘라야 해서 -1
        end = mid - 1

print(end)