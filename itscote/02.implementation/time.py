N = int(input())

count = 0

for h in range(N+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h) or '3' in str(m) or '3' in str(s):
                count += 1

print(count)