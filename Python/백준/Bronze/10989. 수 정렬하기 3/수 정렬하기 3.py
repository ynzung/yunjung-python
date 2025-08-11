# 메모리 초과 오류
'''
n = int(input())
nums = [input() for _ in range(n)]
nums.sort()
for num in nums:
    print(num)
'''

# 구글링 참고한 코드
import sys
input = sys.stdin.readline

# 수의 개수를 입력 받음
n = int(input())

# 각 수의 등장 횟수를 저장하기 위한 리스트 생성
lst = [0] * 10001

# n개의 수를 입력 받아 등장 횟수를 증가시킴
for _ in range(n):
    num = int(input())
    lst[num] += 1

# 리스트 순회하면서 등장 횟수가 0이 아닌 수 출력
for i in range(10001):
    if lst[i]:
        for j in range(lst[i]):
            print(i)