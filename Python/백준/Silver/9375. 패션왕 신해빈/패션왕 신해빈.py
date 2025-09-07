# strip(): 문자열 양쪽 공백제거
# lstrip(): 문자열 왼쪽 공백제거
# rstrip: 문자열 오른쪽 공백제거

import sys

T = int(input())

for _ in range(T):
    cloth = {}  # 옷 종류별 개수 저장
    result = 1 
    n = int(input())
    for _ in range(n):
        name, type = sys.stdin.readline().rstrip().split() 

        if not type in cloth: # 옷 종류가 처음 등장한 경우
            cloth[type] = 1 # 옷 종류별 개수 1로 초기화
        else:
            cloth[type] += 1

    for i in cloth: # 옷 종류별 개수 + 1(안 입는 경우) 곱하기
        result *= (cloth[i] + 1)    # 모든 경우의 수

    print(result - 1)   # 아무것도 안 입는 경우 제외