import sys
input = sys.stdin.readline

n, m = map(int, input().split())
never_seen = {input().strip() for _ in range(n)}
never_heard = {input().strip() for _ in range(m)}

result = sorted(never_seen & never_heard)
print(len(result))
print("\n".join(result))