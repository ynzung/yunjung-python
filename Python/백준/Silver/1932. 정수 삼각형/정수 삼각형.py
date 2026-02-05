import sys
input = sys.stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:  # 왼쪽 끝에서 오는 경우
            triangle[i][j] += triangle[i - 1][j]
        elif j == i:    # 오른쪽 끝에서 오는 경우
            triangle[i][j] += triangle[i - 1][j - 1]
        else:   # 중간에서 오는 경우
            triangle[i][j] += max(triangle[i - 1][j - 1], triangle[i - 1][j])
            
print(max(triangle[-1]))