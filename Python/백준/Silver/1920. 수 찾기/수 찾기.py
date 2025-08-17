n = int(input())
A = set(map(int, input().split())) 
m = int(input())
B = list(map(int, input().split()))

for number in B:
    if number in A:
        print(1)
    else:
        print(0)
