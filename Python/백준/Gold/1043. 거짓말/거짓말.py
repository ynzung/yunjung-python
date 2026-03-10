import sys

input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
truth_input = list(map(int, input().split()))
truth = set(truth_input[1:])  # 첫 숫자는 진실 아는 사람 수라 제외

parties = [set(map(int, input().split()[1:])) for _ in range(m)]  # 각 파티 참석자

# 진실 전파
changed = True  # 진실이 새로 전파되는 동안 반복(True: 진실이 새로 전파됨, False: 더 이상 전파되지 않음)
while changed:
    changed = False # 초기값은 False로 설정하고 진실이 새로 전파되는 경우에만 True로 변경
    for party in parties: 
        if truth & party:  # 파티에 진실 아는 사람이 있으면: 진실이 전파될 수 있는 파티(교집합)
            if not party <= truth:  # 파티 참석자가 모두 진실 그룹에 포함되는지 확인
                # party <= truth : True : 이미 모두 진실을 알고 있음 → 전파할 필요 없음
                # party <= truth : False : 아직 진실을 모르는 사람이 있음 → 전파 필요
                truth |= party  # 그 사람들도 진실 알게 됨: 파티에 있는 사람들을 모두 진실 그룹에 포함(합집합)
                changed = True # 새로운 사람이 진실을 알게 되었으므로 True로 바꾸고 다시 반복

# 거짓말 가능한 파티 수
count = sum(1 for party in parties if not (truth & party))  # 진실 아는 사람과 겹치는 사람이 없는 파티만 카운트
print(count)