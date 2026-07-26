def solution(n):
    if n == 1:
        return 1

    first = 1
    second = 2

    for _ in range(3, n + 1):
        first, second = second, first + second

    return second % 1234567