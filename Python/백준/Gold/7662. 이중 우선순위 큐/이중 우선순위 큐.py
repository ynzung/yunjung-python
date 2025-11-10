import sys
import heapq

input = sys.stdin.readline
T = int(input())

# 틀림 - 원소 삭제 시 한 개의 힙에서만 삭제되고 다른 힙에서는 삭제되지 않음 (동기화 문제)
# for _ in range(T):
#     min_heapq = []
#     max_heapq = []
#     k = int(input())
#     for _ in range(k):
#         op, num = input().split()
#         num = int(num)
#         if op == 'I':
#             heapq.heappush(min_heapq, num)
#             heapq.heappush(max_heapq, -num)
#         elif op == 'D':
#             if min_heapq and max_heapq:
#                 if num == 1:
#                     heapq.heappop(max_heapq)
#                 else:
#                     heapq.heappop(min_heapq)

#     if not min_heapq or not max_heapq:
#         print("EMPTY")   
#     else:
#         print(-max_heapq[0], min_heapq[0])

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    valid = [False] * k  # 각 삽입 연산별로 유효 여부 체크하는 배열

    for i in range(k):
        op, num = input().split()
        num = int(num)

        if op == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            valid[i] = True  # 현재 값이 유효한 상태임을 표시
        else:
            if num == 1:  # 최댓값 삭제
                while max_heap and not valid[max_heap[0][1]]:   # 이미 삭제된 값이 max_heap에 있으면 제거
                    heapq.heappop(max_heap)
                if max_heap:    # 유효한 최댓값 삭제
                    valid[max_heap[0][1]] = False 
                    heapq.heappop(max_heap)
            if num == -1:  # 최솟값 삭제
                while min_heap and not valid[min_heap[0][1]]:  # 이미 삭제된 값이 min_heap에 있으면 제거
                    heapq.heappop(min_heap)
                if min_heap:    # 유효한 최솟값 삭제
                    valid[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    # 남은 값 중 유효하지 않은 값 제거
    while min_heap and not valid[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not valid[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])