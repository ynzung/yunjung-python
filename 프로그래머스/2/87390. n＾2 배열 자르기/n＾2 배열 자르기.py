def solution(n, left, right):
    answer = []
    for k in range(left, right + 1):
        i = k // n + 1
        j = k % n + 1
        answer.append(max(i, j))
        
    return answer