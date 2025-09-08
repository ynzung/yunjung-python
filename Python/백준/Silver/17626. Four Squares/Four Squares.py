import math

n = int(input())

sq = [0 if math.sqrt(i)%1 else 1 for i in range(n+1)]

minValue = 4
for i in range(int(math.sqrt(n)),0,-1) :
    if ( sq[n] ) : # 제곱수
        minValue = 1
        break
    elif sq[n-i**2] : # 나머지가 제곱수
        minValue = 2
        break
    else : # 그외
        for j in range( int(math.sqrt( n - i **2)),0,-1) :
            if sq[ (n- i**2) - j**2] :
                minValue = 3

print(minValue)