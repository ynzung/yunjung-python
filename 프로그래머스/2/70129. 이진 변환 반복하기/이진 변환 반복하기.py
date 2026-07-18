def solution(s):
    answer = []
    cnt = 0  
    zero_cnt = 0
    
    while True:
        if s == "1":
            break
        
        zero_cnt += s.count("0")  # 문자열에서 0의 개수
        s = s.replace("0",'')     # 0을 공백으로 변환
        s = bin(len(s))[2:]       # 이진수로 변환
        
        cnt +=1
        
    answer = [cnt, zero_cnt]    
    return answer