def solution(t, p):
    answer = 0
    # t_length = len(t)
    # p_length = len(p)
    
    for i in range((len(t)-len(p))+1):
        print('t[i:i+len(p)]', t[i:i+len(p)])
        if t[i:i+len(p)] <= p:
            answer += 1
            
    return answer