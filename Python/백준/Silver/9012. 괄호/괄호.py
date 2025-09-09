sentences = []
n = int(input())
sentences =[input() for _ in range(n)]

for sentence in sentences:
    parentheses = []  
    balance = True
    for char in sentence:
        if char == "(":   # 여는 괄호: push
            parentheses.append(char)
        elif char == ")":                # 닫는 소괄호: pop
            if not parentheses:   # 괄호 균형이 안 맞는 경우 (열린 괄호가 없거나 마지막 열린 괄호가 소괄호가 아닌 경우)
                balance = False
                break
            parentheses.pop()

    # 검사 끝난 뒤 결과 출력
    if balance and not parentheses: # 모든 괄호의 균형이 맞는 경우
        print("YES")
    else:
        print("NO")