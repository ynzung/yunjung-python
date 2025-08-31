
# 런타임 에러(NameError) 발생
# 첫번째 If문에서 else에 들어가지 않으면 level이 선언되지 않은 변수가 됨.
# import sys
# input = sys.stdin.readline

# n = int(input())
# if n == 0:
#     print(0)
# else: 
#     level = [int(input()) for _ in range(n)]
#     level.sort()

# cut = round(n * 0.15)
# final_level = level[cut : n-cut]
# print(round(sum(final_level) / len(final_level)))

# 파이썬의 round는 은행가 반올림을 사용, 0.5가 올림이 아닌 내림으로 됨
# import sys
# input = sys.stdin.readline

# n = int(input())
# if n == 0:
#     print(0)
# else:
#     level = [int(input()) for _ in range(n)]
#     level.sort()
#     cut = round(n * 0.15)
#     final_level = level[cut:n-cut]
#     print(round(sum(final_level) / len(final_level)))


import sys
import math
input = sys.stdin.readline

n = int(input())

def setRound(num):
    if (num - int(num)) >= 0.5:
        return math.ceil(num)
    else:
        return math.floor(num)
    
if n == 0:
    print(0)
else:
    level = [int(input()) for _ in range(n)]
    level.sort()
    cut = setRound(n * 0.15)
    final_level = level[cut:n-cut]
    average = setRound(sum(final_level) / len(final_level))
    print(average)