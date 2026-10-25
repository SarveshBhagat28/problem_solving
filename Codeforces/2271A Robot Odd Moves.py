t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    if x == 0 and y == 0:
        print(0)
    elif x == 0:
        print(1 if abs(y) == 1 else -1)
    elif x < abs(y) - 1:
        print(-1)
    elif (x - y) % 2 == 0:
        print(x)
    else:
        print(x + 1)