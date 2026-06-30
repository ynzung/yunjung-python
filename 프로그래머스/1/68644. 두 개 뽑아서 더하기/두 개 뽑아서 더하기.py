from itertools import permutations

def solution(numbers):
    answer = []
    comb = list(permutations(numbers, 2))
    for x, y in comb:
        answer.append(x + y)
    return sorted(set(answer))