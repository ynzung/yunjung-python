# 항상 작은 것끼리 먼저 합치면서 전체 비용 누적 합산 -> 시간복잡도 문제 ? 자꾸 틀림; ;; 
# n = int(input())
# cards = list(map(int, input().split()))

# total = 0

# while len(cards) > 1:
#     min1 = min(cards)
#     cards.remove(min1)

#     min2 = min(cards)
#     cards.remove(min2)

#     local_sum = min1 + min2
#     total += local_sum
#     cards.append(local_sum)

# print(total)

import heapq

n = int(input())  # 카드 묶음 개수
card_bundle = [int(input()) for _ in range(n)]  # 각 카드 묶음의 크기 입력
heapq.heapify(card_bundle)

total = 0

while len(card_bundle) > 1:
    first = heapq.heappop(card_bundle)     # 가장 작은 카드
    second = heapq.heappop(card_bundle)    # 그 다음으로 작은 카드
    local_sum = first + second             # 그것들 합치는 비교 횟수 
    total += local_sum                     # 총 비교 횟수 누적 계산
    heapq.heappush(card_bundle, local_sum) # 카드 묶음 heap에 비교 횟수 넣기

print(total)