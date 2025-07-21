from collections import deque


def solution(N, stages):
    stages = deque(sorted(stages))
    total = len(stages) # 현재 스테이지에 도달한 플레이어 수
    failure_rate = []
    for i in range(1, N+1): # 1부터 n까지 for 문 돌면서 
        count = 0   # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어 수를 세기 위한 count 변수
        while stages and stages[0] == i:    # 현재 스테이지에 머무른? 플레이어 수 확인
            stages.popleft()
            count += 1
        if total == 0:  # 전체 플레이어의 유저가 0인 경우 0 반환
            result = 0 
        else:   # 아닌 경우 실패율 계산 후 result에 누적 계산
            result = count / total
        failure_rate.append((i, result))    # 실패율을 스테이지 번호와 같이 리스트에 저장
        total -= count  # 이전 스테이지에서 탈락한 플레이어 빼주기

    failure_rate.sort(key=lambda x: (-x[1], x[0]))  # 실패율 내림차순, 실패율 같은 경우 스테이지 번호 오름차순 정렬
    answer = [stage for stage, _ in failure_rate]   # 스테이지 번호만 뽑아서 answer에 넣기 
    return answer

n = 5
stages_lst=[2,1,2,6,2,4,3,3]
print(solution(n, stages_lst))