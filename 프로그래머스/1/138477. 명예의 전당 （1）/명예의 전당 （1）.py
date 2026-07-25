def solution(k, score):
    answer = []
    temp = []
    for s in score:
        temp.append(s)      # 오늘 점수 추가
        temp.sort()         # 오름차순 정렬

        if len(temp) > k:   # k명 초과하면
            temp.pop(0)     # 가장 낮은 점수 제거

        answer.append(temp[0])  # 현재 명예의 전당 최저 점수 저장
    return answer