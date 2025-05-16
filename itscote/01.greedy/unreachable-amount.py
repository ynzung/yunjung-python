import itertools

n = int(input())
coin = list(map(int, input().split()))
coin.sort()
# print(coin)

# 총합들 넣을 리스트
sumLst = []

# 모든 조합을 돌면서 합 구하기
for i in range(1, len(coin)+1):
    combinations = list(itertools.combinations(coin, i))
    for comb in combinations:
        sumLst.append(sum(comb))

sumLst.sort()

num = 1  

while True:
    if num not in sumLst:
        print(num)
        break
    num += 1  