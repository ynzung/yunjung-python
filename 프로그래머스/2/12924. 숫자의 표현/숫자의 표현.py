def solution(n):
    answer = 0  # 연속된 수의 합으로 n을 만들 수 있는 경우의 수
    sum = 0     # 현재 구간의 합

    # 시작 숫자 i
    for i in range(1, n + 1):
        sum = 0  # 새로운 시작점마다 합 초기화

        # i부터 차례대로 더해가며 연속된 수의 합 계산
        for j in range(i, n + 1):
            sum += j

            # 합이 n과 같으면 경우의 수 증가
            if sum == n:
                answer += 1
                break

            # n을 초과하면 더 볼 필요 없으므로 종료
            elif sum > n:
                break

    return answer