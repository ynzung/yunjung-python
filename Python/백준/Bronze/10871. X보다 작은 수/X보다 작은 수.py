n, x = map(int, input().split())
A = list(map(int, input().split()))
    

for num in A:
    if num < x:
        print(num, end=' ')