n = int(input())

members = [tuple(input().split()) for _ in range(n)]
members.sort(key=lambda X: (int(X[0]), members.index))

for member in members:
    print(member[0], member[1])