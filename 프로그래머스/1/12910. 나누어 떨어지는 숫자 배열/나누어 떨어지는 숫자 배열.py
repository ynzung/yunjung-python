def solution(arr, divisor):
    # answer = []
    # for i in arr:
    #     if i % divisor == 0:
    #         answer.append(i)
    # if len(answer) == 0:
    #     answer = [-1]
    # else: 
    #     answer.sort()
    return sorted([n for n in arr if n%divisor == 0]) or [-1]