import math

def solution(number, limit, power):
    answer = 0

    # 1부터 number까지 확인하면서
    for num in range(1, number + 1):
        count = 0

        # 약수 개수 구하기
        for i in range(1, math.isqrt(num) + 1):
            if num % i == 0:
                if i == num // i:
                    count += 1
                else:
                    count += 2
        # limit 넘으면 power, 안 넘으면 약수의 개수
        if count > limit:
            answer += power
        else:
            answer += count

    return answer