k = int(input())
money_list = []
zero_count = 0

for i in range(k):
    money = int(input())
    if money == 0:  # 0을 외치면 가장 최근에 쓴 돈 취소
        money_list.pop()
    else:   # 제대로 외치면 리스트에 추가
        money_list.append(money)

print(sum(money_list))
