from itertools import permutations

n = int(input())
numbers = list(map(int, input().split()))
operator_list = list(map(int, input().split()))

operators= []
operators += ['+'] * operator_list[0]
operators += ['-'] * operator_list[1]
operators += ['*'] * operator_list[2]
operators += ['/'] * operator_list[3]

operator_order = set(permutations(operators, n-1))

def calculate(operator):
    result = numbers[0]
    for i in range(1, n):
        if operator[i - 1] == '+':
            result += numbers[i]
        elif operator[i - 1] == '-':
            result -= numbers[i]
        elif operator[i - 1] == '*':
            result *= numbers[i]
        elif operator[i - 1] == '/':
            if result < 0:
                result = -(-result // numbers[i])
            else:
                result = result // numbers[i]
    return result

max_result = -float('inf')
min_result = float('inf')

for i in operator_order:
    total = calculate(i)
    max_result = max(max_result, total)
    min_result = min(min_result, total)

print(max_result)
print(min_result)
