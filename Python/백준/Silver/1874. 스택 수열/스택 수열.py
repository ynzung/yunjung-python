n = int(input())

# is_possible: 불가능한 수열인지 체크하는 상태값
# current: 스택에 아직 넣지 않은 다음 수 (1부터 시작: 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓기 때문)
stack, result, is_possible  = [], [], True

current = 1

for _ in range(n):
    num = int(input())  # 만들어야 할 수열의 다음 숫자
    while current <= num:   # 목표 num까지 자연수 push -> result에 '+' 추가
        stack.append(current)   
        result.append("+")
        current += 1
    if stack[-1] == num:    # 목표값이랑 top 일치하면 ("-")를 추가하고,
        stack.pop()
        result.append("-")
    else:
        is_possible = False # top이 원하는 값이 아니면 불가능으로

if not is_possible: # 수열 불가능한 경우 NO 출력
    print("NO")
else:
    for i in result:  
        print(i)