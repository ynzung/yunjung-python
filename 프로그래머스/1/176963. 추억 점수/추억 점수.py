def solution(name, yearning, photo):
    dictionary = dict(zip(name, yearning))
    answer = []

    for line in photo:
        score = 0

        for each in line:
            if each in dictionary:
                score += dictionary[each]

        answer.append(score)

    return answer