
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ones = a.count(1)

    if 2 * ones >= n:
        print("Bessie")
    else:
        print("Elsie")
