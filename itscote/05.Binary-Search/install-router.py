# count_installable: 넘겨 받은 mid 거리로 설치 가능한 공유기 개수 카운트
def count_installable(array, distance):
    count = 1  # 첫 번째 공유기는 항상 설치
    last_installed = array[0]  # 첫 번째 공유기 위치

    # 두 번째 집부터 마지막 집까지 돌면서
    for i in range(1, len(array)):
         # 현재 집과 마지막 설치 위치 사이의 거리가 최소 거리 이상이면 설치 가능한 경우
        if array[i] - last_installed >= distance:
            # 공유기 하나 설치
            count += 1
            # 마지막 설치 위치 갱신
            last_installed = array[i]

    # 총 설치 가능한 공유기 개수 retrurn
    return count

# binary_search: 이진 탐색으로 인접한 두 공유기 가능한 최대 거리 탐색
def binary_search(array, start, end, c):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        # mid 거리를 기준으로 공유기 설치 가능한지 확인
        if count_installable(array, mid) >= c:  # c개 이상의 공유기 설치할 수 있는 경우
            result = mid  # 설치 가능한 거리 result에 저장하고
            start = mid + 1  # 더 큰 거리 탐색
        else:
            end = mid - 1  # 설치 불가능해서 거리 줄이기

    # 가장 인접한 두 공유기 사이의 최대 거리 return
    return result

n, c = map(int, input().split())
array = [int(input()) for _ in range(n)]
array.sort()  # 공유기 위치 오름차순 정렬
start = 1  # 최소 거리
end = array[-1] - array[0]  # 최대 거리
result = binary_search(array, start, end, c)
print(result)  