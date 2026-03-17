# 2448: 별 찍기 - 11
import sys
input = sys.stdin.readline

n = int(input())
arr = [[' ']*(2*n-1) for i in range(n)] # n행 2n-1열의 2차원 리스트 생성, 공백으로 초기화

# n: 별의 크기, x: 현재 행 위치, y: 현재 열 위치
def star(n, x, y):
  if(n == 3):
    arr[x][y] = '*'

    arr[x+1][y-1] = '*'
    arr[x+1][y+1] = '*'

    arr[x+2][y-2] = '*'
    arr[x+2][y-1] = '*'
    arr[x+2][y] = '*'
    arr[x+2][y+1] = '*'
    arr[x+2][y+2] = '*'
    return
  else:
    star(n//2, x, y)    # 가운데 부분 별 찍기
    star(n//2, x+n//2, y- n//2)   # 왼쪽 아래 부분 별 찍기
    star(n//2, x+n//2, y + n//2)    # 오른쪽 아래 부분 별 찍기

star(n, 0, n-1) # 초기 호출 n은 입력받은 값, x는 0(첫 번째 행), y는 n-1(가운데 열)로 설정

for i in arr:
    print(''.join(i))