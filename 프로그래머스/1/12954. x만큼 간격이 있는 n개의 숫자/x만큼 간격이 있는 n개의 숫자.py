# def solution(x, n):
#     answer = []
#     end = 0
#     if x > 0:
#         end = (x*n) + 1
#     else: 
#         end = (x*n) - 1
#     for i in range(x, end, x):
#         answer.append(i)
#     return answer

def solution(x, n):
    answer = []
    for i in range(1, n+1):
        answer.append(x*i)
        
    return answer