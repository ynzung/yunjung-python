# 겹치는 IOI

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

count = 0   # 연속된 IOI 개수
result = 0  # Pn 완성 횟수
i = 0

while i < M - 1:
    if S[i:i+3] == "IOI":
        count += 1
        # Pn 완성한 경우
        if count == N:
            result += 1
            count -= 1  # IOI가 겹치기 때문에 하나 빼기
        i += 2          # IOI를 찾았으니 다음 I로 이동
    else:
        count = 0
        i += 1

print(result)

