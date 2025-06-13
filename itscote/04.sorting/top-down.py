n = int(input())

lst =[]

for i in range(n):
    lst.append(input())

lst.sort(reverse=True)

print(lst)