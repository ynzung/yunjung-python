def solution(s):
    words = s.split(" ")
    result = []

    for word in words:
        make_word = ""

        for idx, ch in enumerate(word):
            if idx % 2 == 0:
                make_word += ch.upper()
            else:
                make_word += ch.lower()

        result.append(make_word)
        
    answer = " ".join(result)

    return answer