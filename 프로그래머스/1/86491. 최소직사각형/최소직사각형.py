def solution(sizes):
    long = 0    # 긴 변 중 최댓값 넣는 변수
    short = 0   # 짧은 변 중 최댓값 넣는 변수
    
    for a, b in sizes:
         # a: 긴 변 / b: 짧은 변
        if a < b:
            a, b = b, a
        
        long = max(long, a)
        short = max(short, b)
        
    return long * short
