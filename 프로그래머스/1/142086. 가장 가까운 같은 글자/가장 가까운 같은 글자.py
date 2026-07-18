def solution(s):
    answer = [-1] * len(s)    # 모든 문자 기본값 -1로 초기화
    
    for i in range(len(s)):
        for j in range(i):  # 현재 위치 이전 문자들 확인
            if (s[i] == s[j]):  # 같은 문자 찾으면 가까운 글자와 인덱스 차이
                answer[i] = i-j 
                
    return answer