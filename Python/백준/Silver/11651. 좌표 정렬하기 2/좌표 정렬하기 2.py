n = int(input())

coordinates = [tuple(input().split()) for _ in range(n)]
coordinates.sort(key=lambda X: (int(X[1]), int(X[0])))

for coordinate in coordinates:
    print(coordinate[0], coordinate[1])