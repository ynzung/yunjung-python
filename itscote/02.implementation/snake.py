# 입력 받기
n = int(input())  # 정사각형 보드 크기
k = int(input())  # 사과 개수

# 사과 좌표 입력 받기
apple = {tuple(map(int, input().split())) for _ in range(k)}  # 사과는 좌표 튜플로 저장하기 (중복 방지)

# 방향 전환 횟수와 정보 입력 받기
d = int(input())
direction = {int(x): y for x, y in (input().split() for _ in range(d))}  # 방향 전환 정보 (초, 방향)

# 뱀 초기 상태
snake = [(1, 1)]  # 뱀의 초기 좌표
current_direction = 1  # 현재 뱀의 방향 (0: 북, 1: 동, 2: 남, 3: 서)

# 이동 방향 설정 (북, 동, 남, 서)
move_row = [-1, 0, 1, 0]
move_col = [0, 1, 0, -1]

# 게임 진행
count = 0  # 초
while True:
    # 뱀 머리의 새로운 위치 계산
    new_position = (snake[-1][0] + move_row[current_direction], snake[-1][1] + move_col[current_direction])
    count += 1  # 1초 경과

    # 벽에 부딪히거나 자기 몸에 부딪힌 경우 게임 종료
    if not (1 <= new_position[0] <= n and 1 <= new_position[1] <= n) or new_position in snake:
        break

    # 새로운 위치를 뱀 몸에 추가
    snake.append(new_position)

    # 사과가 없는 경우 꼬리 제거
    if new_position not in apple:
        snake.pop(0)
    else:
        apple.remove(new_position)  # 사과 먹었으니께 해당 사과는 제거

    # 방향 전환 확인
    if count in direction:
        if direction[count] == 'D':
            current_direction = (current_direction + 1) % 4  # 오른쪽으로 90도 회전
        else:
            current_direction = (current_direction - 1) % 4  # 왼쪽으로 90도 회전

print(count)