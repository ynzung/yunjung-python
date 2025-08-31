n = int(input())   # 테스트 케이스 개수

for _ in range(n):
    documents, current = map(int, input().split())   # 문서 개수, 궁금한 문서 위치
    data = list(map(int, input().split()))           # 각 문서 중요도
    
    result = 1                                       # 인쇄 순서 (1번부터 시작)
    while data:                                      # 문서가 남아 있는 동안 반복
        if data[0] < max(data):
            # 맨 앞 문서보다 뒤에 더 중요한 문서가 있으면
            # 맨 앞 문서를 큐 뒤로 보냄
            data.append(data.pop(0))
        else:
            # 맨 앞 문서가 가장 중요해서 인쇄하는 경우
            if current == 0:      # 찾던 문서가 맨 앞이었다면
                break             # 현재 result가 인쇄 순서라서 종료
            data.pop(0)           # 인쇄하고 큐에서 제거
            result += 1           # 인쇄된 문서 수 증가

        # current 위치 업데이트
        #   맨 앞 문서가 빠져서 인덱스를 하나 줄임
        #   만약 current가 0이었다면 큐 뒤로 간 문서를 가리켜야 함 -> len(data)-1
        current = current - 1 if current > 0 else len(data) - 1

    print(result)