# 실행한 결괏값 null이 기댓값 [4,3,2]과 다릅니다.
# remove()가 삭제된 리스트를 반환하는 게 아니라 None을 반환 (원본 수정)

# def solution(arr):
#     answer = []
#     if len(arr) == 1:
#         answer = [-1]
#     answer = arr.remove(min(arr))
#     return answer

def solution(arr):
    if len(arr) == 1:
        arr = [-1]
    else:
        arr.remove(min(arr))
    return arr