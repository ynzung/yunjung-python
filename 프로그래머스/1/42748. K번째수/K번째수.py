def solution(array, commands):
    answer = []
    temp = []
    for com in commands:
        i, j, k = com[0], com[1], com[2]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k - 1])
        
    return answer