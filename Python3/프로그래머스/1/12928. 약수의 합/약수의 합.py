import math

# 초기 답안 (시간 복잡도: O(n))
# def solution(n):
#     answer = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             answer += i
#     return answer

# 시간 복잡도: O(√n)
def solution(n):
    answer = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            answer += i
            if i != n // i:     # 같은 약수를 두 번 더하는 걸 막기 위한 조건
                answer += n // i
    return answer