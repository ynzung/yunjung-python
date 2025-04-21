n, m = map(int, input().split())
lst = []

for i in range(n):
    row = list(map(int, input().split()))
    minimum = min(row)
    lst.append(minimum)

print(max(lst))
    