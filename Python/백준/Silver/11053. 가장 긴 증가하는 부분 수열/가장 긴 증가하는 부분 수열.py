import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)   # dp[i]: A[i]를 마지막 원소로 가지는 가장 긴 증가하는 부분 수열의 길이

print(max(dp))