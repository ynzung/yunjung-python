# 시간 초과 
# 중복된 같은 문자를 발견할 때마다 바로 제거하고 더 이상 제거할 쌍이 없을 때까지 반복

# def solution(s):
#     while True:
#         removed = False
#         for i in range(len(s) - 1):
#             if s[i] == s[i + 1]:
#                 s = s[:i] + s[i + 2:]
#                 removed = True
#                 break
#         if not removed:
#             break
#     return 1 if s == '' else 0

def solution(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return 1 if not stack else 0