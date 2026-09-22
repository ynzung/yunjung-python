def solution(clothes):
    counter_dict = {}
    
    # 카테고리별로 의상 개수 넣기 
    for name, category in clothes:
        if category in counter_dict:
            counter_dict[category] += 1
        else:
            counter_dict[category] = 1

    
    answer = 1
    for count in counter_dict.values():
        # 의상 종류에서 하나 고르기 + 해당 의상 종류 안 입기
        answer *= count + 1
    
    # 아무 것도 안 입는 경우 제거
    return answer - 1