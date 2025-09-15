import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start, end = 0, max(tree)

while start <= end:
    mid = (start + end) // 2    # 톱날 높이
    total_length = 0   # 잘라서 만들 수 있는 나무 길이 총합
    for i in tree:
        if i > mid:
            total_length += (i - mid)
    
    if total_length >= m:  # m개보다 많으면 톱날을 올려 자를 수 있어서 +1
        start = mid + 1
    else:   # m개보다 적으면 톱날을 낮춰 잘라야 해서 -1
        end = mid - 1

print(end)