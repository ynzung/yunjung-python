def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for r in range(1, total + 1):
        if total % r == 0:
            c = total // r
            
            if r >= c and (r - 2) * (c - 2) == yellow:
                return [r, c]