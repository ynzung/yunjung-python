from collections import Counter

def solution(want, number, discount):
    answer = 0

    # 1. want + number를 딕셔너리로 만들기
    want_dict = {}

    for i in range(len(want)):
        want_dict[want[i]] = number[i]

    # 2. discount를 10일씩 확인
    for i in range(len(discount) - 9):

        # 3. 현재 10일의 상품 개수 세기
        current = Counter(discount[i:i+10])

        # 4. want_dict와 current가 정확히 같은지 확인
        if want_dict == current:
            answer += 1

    return answer