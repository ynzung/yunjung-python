while True:
    try:
        n, m = map(int, input().split())
        print(n + m)
    except EOFError:
        break