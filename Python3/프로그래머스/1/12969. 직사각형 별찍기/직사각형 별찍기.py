a, b = map(int, input().strip().split(' '))

# answer = [a * '*' for i in range(b)]
# print('\n'.join(answer))

answer = ('*'*a +'\n')*b
print(answer)