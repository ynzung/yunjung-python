# def solution(n, arr1, arr2):
#     answer = []
    
#     for word1, word2 in zip(arr1, arr2):
#         word1_binary = format(word1, f'0{n}b')
#         word2_binary = format(word2, f'0{n}b')
#         result = ''

#         for a, b in zip(word1_binary, word2_binary):
#             if a == '1' or b == '1':
#                 result += '#'
#             else:
#                 result += ' '

#         answer.append(result)

#     return answer

def solution(n, arr1, arr2):
    answer = []

    for num1, num2 in zip(arr1, arr2):

        # 비트 OR 연산: 둘 중 하나라도 1이면 1
        # OR 연산 결과를 길이 n의 이진수 문자열로 변환
        binary = format(num1 | num2, f'0{n}b')

        # 1은 벽('#'), 0은 공백으로 변환
        result = binary.replace('1', '#').replace('0', ' ')
        answer.append(result)

    return answer