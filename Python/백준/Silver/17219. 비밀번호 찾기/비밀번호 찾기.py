import sys
input = sys.stdin.readline

n, m = map(int, input().split())
email_key_dict = dict()
result = []

for _ in range(n):
    input_value = input().split()
    email_key_dict[input_value[0]] = input_value[1]

for _ in range(m):
    find_password = input().strip()
    result.append(email_key_dict[find_password])

print("\n".join(result))