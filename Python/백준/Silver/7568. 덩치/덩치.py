# 모든 사람 다 비교해서 나보다 덩치 큰 사람 수 찾아서 +1

n = int(input())
people = [tuple(map(int, input().split())) for _ in range(n)]

ranks = []

for i in range(n):
    cnt = 0
    for j in range(n):
         if i != j and people[j][0] > people[i][0] and people[j][1] > people[i][1]:
                cnt += 1
    ranks.append(cnt + 1)

print(*ranks)

    