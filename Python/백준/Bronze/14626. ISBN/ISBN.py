ISBN = input().strip()

total = 0
damage_idx = -1

for i in range(0, len(ISBN)):
    if ISBN[i] =="*":
        damage_idx = i
        continue
    if i % 2 == 0:
        total += int(ISBN[i])
    else: 
        total += int(ISBN[i]) * 3

for damage in range(10):
    real_total = total
    if damage_idx % 2 == 0:
        real_total += damage
    else:
        real_total += damage * 3
    if real_total % 10 == 0:
        print(damage)
        break