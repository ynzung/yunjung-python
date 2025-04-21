n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
nums.sort(reverse=True)

while m > 0:
    for i in range(k):
        result += nums[0]
        m -= 1
    result += nums[1]
    m -= 1

print(result)