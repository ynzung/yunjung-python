def total_cut_length(array, cut_height):
    total = 0
    for x in array:
        if x > cut_height:
            total += x - cut_height
    return total

n, m = map(int, input().split())
height = list(map(int, input().split()))

# 이진 탐색할 시작점, 끝점
start = 0
end = max(height)
result = 0

while start <= end:
    mid = (start + end) // 2  # 절단기 높이
    total = total_cut_length(height, mid)

    if total < m:
        # 덜 잘렸다면 높이를 낮추기
        end = mid - 1
    else:
        # 충분히 잘렸으면 높이 올리기
        result = mid  # 일단 저장 먼저하고
        start = mid + 1

print(result)