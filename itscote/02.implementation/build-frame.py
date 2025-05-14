def check(answer, x, y, a):
    if a == 0:  # 기둥
        if y == 0:  # 바닥에 설치 
            return True
        elif (x - 1, y, 1) in answer:  # 왼쪽에 보가 있을 때
            return True
        elif (x, y, 1) in answer:  # 오른쪽에 보가 있을 때
            return True
        elif (x, y - 1, 0) in answer:  # 아래에 기둥이 있을 때
            return True
    elif a == 1:  # 보
        if (x, y - 1, 0) in answer:  # 왼쪽 기둥이 있을 때
            return True
        elif (x + 1, y - 1, 0) in answer:  # 오른쪽 기둥이 있을 때
            return True
        elif (x - 1, y, 1) in answer and (x + 1, y, 1) in answer:  # 양쪽에 보가 있을 때
            return True
    return False


def solution(n, build_frame):
    answer = set()  # 설치된 기둥과 보 저장하는 집합
    for value in build_frame:
        x, y, a, b = value  # x: x좌표, y: y좌표, a: 기둥, 보, b: 설치, 삭제

        if b == 1:  # 설치
            if check(answer, x, y, a):
                answer.add((x, y, a))
        elif b == 0:  # 삭제
            answer.discard((x, y, a)) 
            # 삭제 먼저 갈기고 모든 기둥과 보가 유효한지 확인
            is_valid = True
            for item in answer:
                x1, y1, a1 = item
                if not check(answer, x1, y1, a1):  # 유효하지 않으면 false
                    is_valid = False
                    break
            if not is_valid:  # 유효하지 않으면 다시 복구
                answer.add((x, y, a))

    return sorted([list(i) for i in answer], key=lambda x: (x[0], x[1], x[2]))


n = 5
build_frame = [
    [1, 0, 1, 1],  # 기둥 (1, 0) 설치
    [1, 1, 1, 1],  # 보 (1, 1) 설치
    [2, 1, 1, 1],  # 보 (2, 1) 설치
    [2, 2, 0, 1],  # 기둥 (2, 2) 설치
    [5, 0, 1, 1],  # 보 (5, 0) 설치
    [4, 2, 1, 1],  # 보 (4, 2) 설치
    [3, 2, 0, 1],  # 기둥 (3, 2) 설치
    [3, 3, 1, 1],  # 보 (3, 3) 설치
    [2, 3, 0, 1],  # 기둥 (2, 3) 설치
    [4, 3, 0, 1],  # 기둥 (4, 3) 설치
    [3, 4, 1, 1],  # 보 (3, 4) 설치
    [5, 2, 1, 1],  # 보 (5, 2) 설치
    [4, 4, 0, 1],  # 기둥 (4, 4) 설치
    [3, 5, 1, 1],  # 보 (3, 5) 설치
    [2, 4, 0, 1],  # 기둥 (2, 4) 설치
]


print(solution(n, build_frame))