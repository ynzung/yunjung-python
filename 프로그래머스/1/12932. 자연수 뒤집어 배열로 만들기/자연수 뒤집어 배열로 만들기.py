def solution(n):
    answer = []
    # lst = list(str(n))
    # lst.reverse()
    lst = str(n)[::-1]     # 문자열 슬라이싱으로 reverse 가능
    for i in lst:
        answer.append(int(i))
    return answer
