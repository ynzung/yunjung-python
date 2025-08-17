min_result = float('inf')
n, m = map(int, input().split())
board = [list(map(str, input())) for _ in range(n)]

for i in range(n-7):
    for j in range(m-7):
        count_white = 0  # 왼쪽 위가 W일 때 다시 칠해야 하는 수 
        count_black = 0  # 왼쪽 위가 B일 때 다시 칠해야 하는 수
        
        for x in range(i, i+8): 
            for y in range(j, j+8): 
                if (x + y) % 2 == 0:
                    # 짝수 위치: 왼쪽 위와 같은 색이어야 함
                    if board[x][y] != 'W': 
                        count_white += 1  
                    if board[x][y] != 'B': 
                        count_black += 1
                else:
                    # 홀수 위치: 왼쪽 위와 반대 색이어야 함
                    if board[x][y] != 'B': 
                        count_white += 1
                    if board[x][y] != 'W': 
                        count_black += 1    

        min_result = min(min_result, count_white, count_black) 

print(min_result)