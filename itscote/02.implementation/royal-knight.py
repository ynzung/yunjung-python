current_knight = input()
row = int(current_knight[1])
col = ord(current_knight[0]) - ord('a') + 1 

move = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0

for m in move:
    next_row = row + m[0]
    next_col = col + m[1]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        result += 1

print(result)