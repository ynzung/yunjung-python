# 시간 초과
import sys
input = sys.stdin.readline

n = int(input())
n_card = input().split()
m = int(input())
m_card = input().split()
result = []

# for i in m_card:
#     if i in n_card:
#         count = n_card.count(i)
#         result.append(count)
#     else:
#         result.append(0)

# print(" ".join(str(r) for r in result))


from collections import Counter

count = Counter(n_card)           
# n_card 리스트에 들어있는 원소들의 등장 횟수를 세어서
# {원소: 빈도수} 형태의 딕셔너리처럼 저장해줌
# 예: n_card = ['10', '10', '3'] → Counter({'10': 2, '3': 1})

result = [str(count.get(x, 0)) for x in m_card] 
# m_card 안의 각 원소 x에 대해:
#   count.get(x, 0) → Counter에 x가 있으면 그 개수, 없으면 0 반환
#   str(...)       → 문자열로 변환 (join 출력 위해)
# 리스트 컴프리헨션으로 한 번에 결과 리스트 생성
# 예: m_card = ['10','5'] → ['2','0']
print(' '.join(result))