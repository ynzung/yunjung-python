r = 31
m = 1234567891

length = int(input())
s = input()
result = 0 
for i in range(length):
    result += (ord(s[i]) - ord('a') + 1)  * (r ** i)
result %= m
print(result)