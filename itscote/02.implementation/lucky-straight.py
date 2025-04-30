N = input()

half = len(N) // 2

left=0
right = 0

for i in range(int(half)):
    left += int(N[i])

for j in range(int(half), len(N)):
    right += int(N[j])

if left == right:
    print("LUCKY")
else: 
    print("READY")

