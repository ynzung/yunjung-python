import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

Pn = "IO" * N + "I"
count = 0

for i in range(M):
  if S[i] == 'I':
    if S[i:i+(N * 2 + 1)] == Pn and i <= M:
      count += 1

print(count)