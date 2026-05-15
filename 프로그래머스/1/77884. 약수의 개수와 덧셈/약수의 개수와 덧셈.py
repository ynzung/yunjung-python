def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1

        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
            
'''            
 i가 완전제곱수인지 확인하는 코드
 완전 제곱수는 약수의 개수가 홀수!!!!
 완전 제곱수가 아니면 약수의 개수가 짝수임
'''

# def solution(left, right):
#     answer = 0
#     for i in range(left,right+1):
#         if int(i**0.5)==i**0.5:
#             answer -= i
#         else:
#             answer += i
#     return answer