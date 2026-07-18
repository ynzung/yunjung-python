def solution(s):
    answer = ""
    temp = ""
    dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    
    for word in s:
        if word.isdigit():
            answer += word
        else:
            temp += word
            if temp in dic:
                answer += dic[temp]
                temp = ""

    return int(answer)