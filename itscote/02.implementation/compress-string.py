def solution(s):
    answer = len(s)  # 문자열 길이로 초기화

    # i는 압축 단위를 의미
    for i in range(1, len(s) // 2 + 1):
        compressed = ""  # 압축된 문자열을 저장할 변수
        prev = s[:i]  # 이전에 비교한 문자열 초기화
        count = 1  # 문자열 반복 횟수 초기화

        # 단위 당 압축된 문자열 만들기
        for j in range(i, len(s), i):
            current = s[j:j + i]  # 현재 단위의 문자열을 가져오기

            # 이전 문자열과 동일한 경우 반복 횟수를 증가
            if prev == current:
                count += 1
            else:
                # 이전 문자열과 다른 경우, 압축된 문자열에 추가
                compressed += str(count) + prev if count > 1 else prev
                prev = current  # 다음 문자열로 이동
                count = 1  # 반복 횟수 초기화

        # 남은 문자열을 압축된 문자열에 추가
        compressed += str(count) + prev if count > 1 else prev

        # 압축된 문자열의 길이가 최소값보다 작은 경우 업데이트
        answer = min(answer, len(compressed))

    return answer

s = "aabbaccc"
print(solution(s)) 
