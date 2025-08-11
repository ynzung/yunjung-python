# 1차 시도
# s = [input() for _ in range(3)]

# if s[-1].isdigit():
#     result = int(s[-1]) + 1
#     if result % 3 == 0 and result % 5 == 0:
#         print("FizzBuzz")
#     elif result % 3 == 0:
#         print("Fizz")
#     elif result % 5 == 0:
#         print("Buzz")
#     else:
#         print(result)
# else:
#     print(int(s[1]) + 2)

s = [input().strip() for _ in range(3)]

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

if s[-1].isdigit():
    result = int(s[-1]) + 1
else:
    if s[-1] == "Fizz" or s[-1] == "Buzz" or s[-1] == "FizzBuzz":
        if s[1].isdigit():
            prev_num = int(s[1])
        else:
            prev_num = int(s[0]) + 1
        result = prev_num + 2

print(fizzbuzz(result))