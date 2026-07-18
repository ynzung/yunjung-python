def solution(a, b, n):
    answer = 0
    while n >= a:
        exchange = n // a       # 교환 가능 횟수 = 가진 빈 병 // 교환에 필요한 빈 병
        answer += exchange * b      # 교환으로 받은 콜라 병 누적
        n = (n % a) + (exchange * b) # 남은 빈 병 + 교환하고 생긴 빈 병
        
    return answer