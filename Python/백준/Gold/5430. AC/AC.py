# 뒤집기를 매번 해서 시간 초과 발생

# import sys
# from collections import deque
# input = sys.stdin.readline

# T = int(input())
# result = []
# for _ in range(T):
#     p = input().rstrip()
#     n = int(input())
#     arr = input().rstrip()
#     no_bracket_str = arr[1:-1]  # 입력받은 문자열에서 대괄호 제거를 위해 슬라이싱
#     # dq = deque(no_bracket_str.split(",")) 빈 배열인 경우 error처리가 안되는 문제가 있는 코드
#     dq = deque() if no_bracket_str == "" else deque(no_bracket_str.split(","))  # 빈 배열 처리 필요!!

#     error = False
#     for i in range(len(p)):
#         if p[i] == "R":
#             dq.reverse()
#         elif p[i] == "D":
#             if not dq:
#                 result.append("error")
#                 error = True
#                 break
#             else: 
#                 dq.popleft()
#     if not error:
#         result.append("[" + ",".join(dq) + "]")


# print("\n".join(result))

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    arr = input().rstrip()
    no_bracket_str = arr[1:-1]  # 입력받은 문자열에서 대괄호 제거를 위해 슬라이싱
    dq = deque() if no_bracket_str == "" else deque(no_bracket_str.split(","))  # 빈 배열 처리 필요!!

    error = False
    rev = False  # 방향 플래그

    for i in range(len(p)):
        if p[i] == "R":
            rev = not rev  # 실제 reverse() 대신 플래그 토글
        elif p[i] == "D":
            if not dq:
                result.append("error")
                error = True
                break
            else:
                if rev:
                    dq.pop()       # 뒤에서 제거
                else:
                    dq.popleft()   # 앞에서 제거

    if not error:
        if rev:
            dq.reverse()  # 최종 한 번만 뒤집기 (또는 ",".join(reversed(dq)) 사용)
        result.append("[" + ",".join(dq) + "]")

print("\n".join(result))
