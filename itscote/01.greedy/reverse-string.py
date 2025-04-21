s = input()

lst = []
count = 0


for i in str(s):
    lst.append(i)

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j]:
            count += 1

print(count)