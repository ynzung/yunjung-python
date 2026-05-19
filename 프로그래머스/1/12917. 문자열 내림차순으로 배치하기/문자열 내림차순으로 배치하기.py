def solution(s):
    answer = ''
    lst = [int(ord(i)) for i in s]
    lst.reverse()
    lst = [chr(i) for i in lst]
    answer = ''.join(lst)
    return answer