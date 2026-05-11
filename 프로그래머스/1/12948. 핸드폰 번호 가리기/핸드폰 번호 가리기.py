def solution(phone_number):
    length = len(phone_number) - 4
    answer = '*' * length + phone_number[length:]
    # answer = "*" * (len(phone_number) - 4) + phone_number[-4:]
    return answer