from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))

card_combi = list(combinations(card, 3))
max_sum = 0

for i in card_combi:
    if sum(i) <= m:
        max_sum = max(max_sum, sum(i))

print(max_sum)