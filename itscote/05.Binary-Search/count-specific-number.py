n, x = map(int, input().split())
array = list(map(int, input().split()))

def count_specific_number(array, x):
    # find_left: x가 처음 나오는 index를 찾아줌
    def find_left(array, target):
        start, end = 0, len(array)
        while start < end:
            mid = (start + end) // 2
             # mid 위치의 값이 target 이상인 경우 왼쪽에 target이 있을 수 있기 때문에 mid로 갱신해서 end 값을 낮추기
            if array[mid] >= target:
                end = mid
            else:
                 # mid 위치의 값이 target보다 작은 경우 target은 오른쪽에 있기 때문에 start 값을 올리기
                start = mid + 1
        return start 

    # find_right: x보다 큰 값이 처음 나오는 index를 찾아줌
    def find_right(array, target):
        start, end = 0, len(array)
        while start < end:
            mid = (start + end) // 2
            # mid 위치의 값이 target보다 큰 경우 정답은 왼쪽에 있을 수 있기 때문에 mid로 갱신해서 end 값을 낮추기
            if array[mid] > target:
                end = mid
            else:
                # mid 값이 target 이하인 경우 target의 마지막 index보다 오른쪽에 있기 떄문에 start 값을 올리기
                start = mid + 1
        # target보다 큰 값이 처음 나오는 index 반환
        return start

    
     # left: x가 처음 나오는 index
    left = find_left(array, x)
    # right: x보다 큰 값이 처음 나오는 index
    right = find_right(array, x)
    
     # x인 원소가 하나도 없는 경우 find_left, find_right가 같은 값을 return -> 둘의 차이가 0인 경우 -1 출력
    if right - left == 0:
        return -1
    else:
        return right - left

print(count_specific_number(array, x))