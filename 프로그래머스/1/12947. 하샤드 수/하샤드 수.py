def solution(x):
    answer = True
    lst = list(map(int, str(x)))
    s = sum(lst)
    
    if x % s == 0:
        answer = True
    else:
        answer = False
    return answer