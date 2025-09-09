import sys
import math
from collections import Counter
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()

def setRound(x):
   return int(x + 0.5) if x >= 0 else -int(-x + 0.5)
        
def getMode(arr):
    # arr의 각 원소별 등장 횟수를 세어 딕셔너리 형태로 반환
    cnt = Counter(arr)

    # 가장 큰 등장 횟수(최빈도) 구하는 코드
    max_freq = max(cnt.values())

    # 최빈도와 같은 횟수를 가진 원소들만 모아서 리스트로 만들기
    modes = [x for x, f in cnt.items() if f == max_freq]

    # 값이 여러 개일 수 있기 때문에 오름차순으로 정렬
    modes.sort()

    # 최빈값이 하나이면 그대로 반환
    # 여러 개면 두 번째로 작은 값 반환
    return modes[0] if len(modes) == 1 else modes[1]

first = setRound(sum(num) / n)
second = num[n // 2]
third = getMode(num)
fourth = num[-1] - num[0]

print(first)
print(second)
print(third)
print(fourth)