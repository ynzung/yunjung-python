def solution(n):
    answer = 0
    bina = bin(n).count('1')    # n을 2진수로 변환했을 때 1의 개수 저장
    answer = n + 1  # n보다 큰 수부터 탐색 시작
    while True:
        # 현재 수의 1의 개수가 n과 같으면 종료
        if answer > n and bina == bin(answer).count('1'):
            break
        # 다음 수 확인
        answer += 1
    return answer