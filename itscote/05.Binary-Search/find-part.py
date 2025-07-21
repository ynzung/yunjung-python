
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
    
n = int(input())
all_part = list(map(int, input().split()))
all_part.sort()

m = int(input())
ordered_part = list(map(int, input().split()))

for i in ordered_part:
    result = binary_search(all_part, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')



