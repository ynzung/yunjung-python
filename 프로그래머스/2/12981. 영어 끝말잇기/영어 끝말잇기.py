def solution(n, words):
    answer = []
    words_set = set()

    for idx, word in enumerate(words):
        # 첫 번째 단어가 아니라면 끝말잇기 규칙 검사
        if idx > 0:
            if words[idx - 1][-1] != word[0]:
                person = idx % n + 1
                turn = idx // n + 1
                return [person, turn]

        # 이미 나온 단어인지 검사
        if word in words_set:
            person = idx % n + 1
            turn = idx // n + 1
            return [person, turn]

        # 정상적으로 말한 단어를 저장
        words_set.add(word)

    return [0, 0]