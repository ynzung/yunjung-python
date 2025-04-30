s = input()
string = []
number = 0
result=""

for i in range(len(s)):
    if(s[i].isdigit()):
        number += int(s[i])
    else:
        string.append(s[i])

string.sort()

for j in range(len(string)):
    result += string[j]

print(result + str(number))