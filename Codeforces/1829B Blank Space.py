
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = 0
    max_count = 0

    for x in a:
        if x == 0:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    print(max_count)
