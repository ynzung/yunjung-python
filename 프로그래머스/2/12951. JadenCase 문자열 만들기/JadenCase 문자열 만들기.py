# # 런타임 에러
# def solution(s):
#     answer = ''
#     lst = list(map(str, s.split(" "))) # 공백 기준으로 잘라서 lst에 넣기
#     result = [] # JadenCase로 변환된 문자열 넣을 리스트
#     for word in lst:
#         temp = ''
#         if word[0].isdigit():   # 문자열의 첫 문자가 숫자인 경우
#             result.append(word) # 변환 필요 X -> word 그냥 result에 넣기
#         else:   # 문자열 첫 문자가 숫자 아닌 경우 (문자인 경우)
#             temp = word[0].upper()  # 첫 문자를 대문자로 변경
#             temp += word[1:].lower()    # 첫 문자 이후의 문자를 소문자로 변경
#             result.append(temp)    # JadenCase로 변환된 temp를 result에 넣기
#     answer = " ".join(result)
#     return answer

def solution(s):
    lst = list(map(str, s.split(" ")))
    answer = " ".join([word.capitalize() for word in lst])
    return answer