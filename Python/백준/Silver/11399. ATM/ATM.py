import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
times.sort()

sum_time = 0
result = 0

for t in times:
    sum_time += t
    result += sum_time

print(result)