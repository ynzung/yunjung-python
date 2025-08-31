import sys
input = sys.stdin.readline

n, k= map(int, input().split())
result = 0

coins = [int(input().strip()) for _ in range(n)]

for coin in reversed(coins):
    if k >= coin: 
        count = k // coin
        result += count
        k -= count * coin
print(result)
