# 런타임 에러 (KeyError)
# quiz가 string이라서 int로 숫자로 변경해주기
# input할 때 줄바꿈도 같이 들어가서 없애려면 strip() 필요

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pocketmon_index = dict()
pocketmon_name = dict()

for pkm in range(1, n+1):
    name = input().strip() 
    pocketmon_index[pkm] = name
    pocketmon_name[name] = pkm

for _ in range(m):
    quiz = input().strip()
    if quiz.isdigit():
        print(pocketmon_index[int(quiz)])
    else: 
        print(pocketmon_name[quiz])