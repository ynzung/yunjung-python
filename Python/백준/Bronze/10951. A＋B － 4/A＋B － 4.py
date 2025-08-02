# 런타임 에러 발생, 입력 함수 호출 시 적절한 입력 제공되는지 확인하고 
# 파일의 끝을 예외처리 해야함 
# 참고 블로그: https://machinelog.tistory.com/entry/Python-%EB%9F%B0%ED%83%80%EC%9E%84-%EC%97%90%EB%9F%AC

while True:
    try:
        n, m = map(int, input().split())
        print(n + m)
    except EOFError:

        break
