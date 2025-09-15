# +로 더할 애들은 모두 더해놓고 마지막에 다 빼면 가장 작은 수가 되지 않을까

import sys
input = sys.stdin.readline

exp = input().strip()
result = []

# -를 기준으로 분리
chunk_base_sub = exp.split("-")

for i in chunk_base_sub:
    if "+" in i:
        chunk_base_add = i.split("+")
        result.append(sum(map(int, chunk_base_add)))
    else:
        result.append(int(i))

print(result[0] - sum(result[1:]))



# 틀린 코드: 첫 덩어리인지 판별을 result == 0으로 해서
# 중간 계산 결과가 우연히 0이 되는 순간, 그 다음 덩어리를 “첫 덩어리”로 착각해서 더할 수도 있음

# chunk_base_sub = exp.split("-")

# for i in chunk_base_sub:
#     if "+" in i:    # -를 기준으로 분리된 애들 중 +가 있는 덩어리면
#         chunk_base_add = i.split("+")  # +를 기준으로 다시 나눔
#         num = sum(map(int, chunk_base_add)) # +를 기준으로 나눈 애들의 합을 구해서 num에 넣기
#         # result 안에 값이 없으면 더하고 나머지는 뺌
#         if result == 0: 
#             result += num
#         else:
#             result -= num
#     else: 
#         # +없는 덩어리인 경우에도 result 안에 값이 없으면 더하고 나머지는 뺌
#         if result == 0:
#             result += int(i)
#         else:
#             result -= int(i)

# print(result)