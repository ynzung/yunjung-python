import math

def solution(n, m):
    answer = []
    gcd, lcm = math.gcd(n, m), math.lcm(n, m)
    answer.append(gcd)
    answer.append(lcm)
    return answer
