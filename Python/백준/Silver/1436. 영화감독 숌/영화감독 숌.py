# 계속 돌면서 666이 들어갈때까지 찾는거고 666이 들어갈 n개의 수를 찾으면 그만 둠

n = int(input())
count = 0
num = 666

while True:
    if "666" in str(num):
        count += 1
        if count == n:
            print(num)
            break
    num += 1