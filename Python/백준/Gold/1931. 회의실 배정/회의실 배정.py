import sys
input = sys.stdin.readline

n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]

# 끝나는 시간 기준으로 정렬, 끝나는 시간이 같으면 시작 시간 기준으로 정렬   
times.sort(key=lambda x: (x[1], x[0]))

result = [] # 선택된 회의 목록(겹치지 않는 회의들만 담음)
for s, e in times:
    # 비어 있거나 마지막에 선택한 회의가 끝난 시간 <= 현재 회의 시작시간인 경우
    if not result or result[-1][1] <= s:
        result.append((s, e))

print(len(result))
