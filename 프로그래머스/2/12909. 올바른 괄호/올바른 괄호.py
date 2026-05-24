'''
첫 번째 시도: 여는 괄호와 닫는 괄호의 개수가 같으면 T, 다르면 F로 리턴
문제점: ((())))( -> 개수가 같아도 F여야 하는 경우 있음
'''
# def solution(s):
#     if s[0] == ")":
#         answer = False
#     else:
#         if s.count("(") == s.count(")"):
#             answer = True
#         else:
#             answer = False

#     return answer

def solution(s):
    cnt = 0
    for i in s:
        if i == '(':
            cnt += 1
        if i == ')':
            cnt -= 1
            if cnt < 0:
                return False
    return cnt == 0