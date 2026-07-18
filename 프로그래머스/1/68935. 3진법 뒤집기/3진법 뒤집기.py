def solution(n):
    answer = 0
    
    # 3진법 변환
    nums = []
    while n:
        n, remainder = divmod(n, 3)
        nums.append(remainder)
    
    # 뒤집고 다시 10진법으로 표현
    for i, v in enumerate(nums[::-1]):
        answer += v * (3 ** i)
    
    return answer