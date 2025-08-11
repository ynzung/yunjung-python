num = []

for _ in range(9):
    a = input()
    num.append(int(a))
    max_num = max(num)

print(max_num)
print(num.index(max_num) + 1)
