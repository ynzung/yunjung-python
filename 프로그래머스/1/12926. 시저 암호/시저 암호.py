def solution(s, n):
    answer = ''
    for i in s:
        # 공백 처리
        if i == ' ':
            answer += i
          
        # 대문자인 경우 Z보다 큰 경우와 아닌 경우 나눔
        elif i.isupper():
            if (ord(i) + n) > ord('Z'):
                temp = chr(ord(i) + n - 26)
            else:
                temp = chr(ord(i) + n)
            answer += temp
            
        # 소문자인 경우 z보다 큰 경우와 아닌 경우 나눔
        else:
            if (ord(i) + n) > ord('z'):
                temp = chr(ord(i) + n - 26)
            else:
                temp = chr(ord(i) + n)
            answer += temp
             
    return answer