# ceil(): 올림 함수 -> math에서 불러와야 함
# size_arr: 티셔츠 사이즈 배열
# t: 한 세트에 들어가는 티셔츠 개수
# p: 한 세트의 펜 개수
# shirts_set_count: 티셔츠 세트 개수

import math

n = int(input())
size_arr = list(map(int, input().split()))
t, p = map(int, input().split())

shirts_set_count = 0

for size in size_arr:
    shirts_set_count += math.ceil(size / t)

print(shirts_set_count)
print(n // p, n % p)
