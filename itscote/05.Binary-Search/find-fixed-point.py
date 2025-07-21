n = int(input())
array = [int(n) for n in input().split()]

def find_fiex_point(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 고정점 찾으면 바아로 mid return 
        if array[mid] == mid:
            return mid
         # 현재 값이 인덱스보다 크면 오른쪽 값들은 인덱스보다 더 큰 거 -> 왼쪽에 고정점이 존재할 것
        elif array[mid] > mid:
            return find_fiex_point(array, start, mid - 1)
        # 현재 값이 인덱스보다 작으면 왼쪽 값들은 인덱스보다 더 작은 거 -> 오른쪽에 고정점이 존재할 것
        else:
            return find_fiex_point(array, mid + 1, end)
    # 고정점 없는 경우 -1 return 
    return -1

print(find_fiex_point(array, 0, n - 1))