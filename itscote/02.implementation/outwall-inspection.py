from itertools import permutations

def solution(n, weak, dist):
    weak_len = len(weak)
    
    for i in range(weak_len):
        weak.append(weak[i] + n)

    min_friends = len(dist) + 1 

    for start_index in range(weak_len):
        for friend_order in permutations(dist):
            friend_used = 1  
            space_limit = weak[start_index] + friend_order[friend_used - 1] 

            for i in range(start_index, start_index + weak_len):
                if weak[i] > space_limit:
                    friend_used += 1 
                    if friend_used > len(dist): 
                        break
                    space_limit = weak[i] + friend_order[friend_used - 1]

            min_friends = min(min_friends, friend_used)

    if min_friends <= len(dist):
        return min_friends
    else:
        return -1


n = 12 
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]

print(solution(n, weak, dist))