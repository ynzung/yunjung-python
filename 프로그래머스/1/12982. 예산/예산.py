def solution(d, budget):
    d.sort()

    total = 0
    answer = 0

    for x in d:
        total += x
        if total > budget:
            break
        answer += 1

    return answer