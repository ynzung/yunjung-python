def solution(k, tangerine):
    answer = 0
    cnt_dict = {}
    for t in tangerine:
        if t not in cnt_dict:
            cnt_dict[t] = 1
        else:
            cnt_dict[t] += 1
            
    cnt_arr = list(cnt_dict.values())
    cnt_arr.sort(reverse = True)
    for i in cnt_arr:
        if k > 0:
            k -= i
            answer += 1
    
    return answer