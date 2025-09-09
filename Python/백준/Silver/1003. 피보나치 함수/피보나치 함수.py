# result =[]

# def fibonacci(inputNum, num):
#     if (num == 0):
#         countTest(inputNum, num)
#         return 0
#     elif (num == 1):
#         countTest(inputNum, num)
#         return 1
#     else:
#         return (fibonacci(inputNum, num-1) + fibonacci(inputNum, num-2))
    
# # order: 입력 값으로 받앗던 숫자
# # testNum: 피보나치에서 하나씩 깎여가는 숫자
# def countTest(order, testNum):
#     result.append((order, testNum))
    
    
# n = int(input())

# for i in range(n):
#     fibonacci(i, int(input()))

# counts = {}  # order, val: [0개수, 1개수]

# for order, val in result:
#     if order not in counts:
#         counts[order] = [0, 0]  
#     if val == 0:
#         counts[order][0] += 1
#     else:
#         counts[order][1] += 1

# for order in sorted(counts.keys()):
#     print(counts[order][0], counts[order][1])


n = int(input())
for _ in range(n):
    inputNum = int(input())
    zero, one = 1, 0 # fib(0) = (1,0)
    for i in range(inputNum):
        # fib(n) = fib(n-1) + fib(n-2)
        # 0은 1이 호출된 횟수만큼, 1은 0과 1이 호출된 합만큼 출력됨
        zero, one = one, zero + one    # 0일때의 (0,1) 값을 계속 갱신 시키는 것!!

    print(zero, one)    
