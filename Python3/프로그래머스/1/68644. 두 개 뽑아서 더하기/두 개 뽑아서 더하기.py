from itertools import combinations

def solution(numbers):
    answer = []
    comb = list(combinations(numbers, 2))
    for x, y in comb:
        answer.append(x + y)
    return sorted(set(answer))