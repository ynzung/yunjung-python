def solution(n):
    answer = []
    lst = list(str(n))
    lst.reverse()
    for i in lst:
        answer.append(int(i))
    return answer