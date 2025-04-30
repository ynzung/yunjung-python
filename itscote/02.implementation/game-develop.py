n, m = map(int, input().split())
x, y, d = map(int, input().split())

game_map=[]
# 바다, 육지 값 입력받기
for _ in range(n):
    sea_or_shore = list(map(int, input().split()))
    game_map.append(sea_or_shore)

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문했던 좌표 목록을 저장하기 위해 set 선언
visited_list = set()
visited_list.add((x, y))

while True:
    # 사방 검사 후 움직였는지 안 움직였는지를 확인하려고 넣은 플래그
    moved = False
    for i in range(4):  # 북, 동, 남, 서 모든 방향 검사
        next_direction = (d - 1) % 4 
        d = next_direction  # 방향 업데이트
        next_x = x + dx[next_direction] # 위치 업데이트
        next_y = y + dy[next_direction] # 위치 업데이트
        
        #  게임 맵 안에 있고, 육지이고, 아직 방문하지 않은 곳에 방문
        if 0 <= next_x < n and 0 <= next_y < m:
            if game_map[next_x][next_y] == 0 and (next_x, next_y) not in visited_list:
                # 방문한 리스트에 추가하고
                visited_list.add((next_x, next_y))
                # 위치 이동시키기 !!
                x = next_x
                y = next_y
                # 움직였다는 플래그 값 넣어줌
                moved = True
                break
    # 만약에 움직이지 않은 경우, (위의 모든 방향을 방문한 경우)
    if not moved:
        # 현재 방향에서 뒤로 가기 
        back_direction = (d + 2) % 4
        # 뒤로 이동 
        back_x = x + dx[back_direction]
        back_y = y + dy[back_direction]
        
        # 게임 맵 안에 있고, 뒤로 이동한 위치가 모두 육지인 경우
        if 0 <= back_x < n and 0 <= back_y < m and game_map[back_x][back_y] == 0:
            # 뒤로 이동시키기
            x = back_x
            y = back_y
        else:
            break  # 뒤도 바다인 경우 종료
            
print(len(visited_list))