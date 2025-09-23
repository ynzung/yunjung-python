import sys

input = sys.stdin.readline
N = input().split()

result = list(map(int, input().split()))

# 중복 제거하고 오름차순 정렬
temp = sorted(set(result))

# # 값을 index로 바꾸기
# for i in range(len(result)):
#     result[i] = temp.index(result[i])   


# for i in range(len(result)):
#     print(result[i], end=' ')

# print()

dic = dict()

# 인덱스를 key로, 정렬하는 값들을 value으로
for i in range(len(temp)): 
    dic[temp[i]] = i


for i in result:
     print(dic[i], end=' ')
print()


