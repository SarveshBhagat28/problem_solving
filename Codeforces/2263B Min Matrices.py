t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if k < n or k > 2 * n - 1:
        print(-1)
        continue

    s = 2 * n - k

    a = [[0] * n for _ in range(n)]

    used = set()

    # Place row minimums
    for i in range(n):
        if i < s:
            a[i][i] = i + 1
        else:
            a[i][0] = i + 1

        used.add(i + 1)

    # Place additional column minimums
    for j in range(s, n):
        a[0][j] = n + j + 1
        used.add(n + j + 1)

    # Fill remaining cells
    num = 1

    for i in range(n):
        for j in range(n):
            if a[i][j] == 0:
                while num in used:
                    num += 1

                a[i][j] = num
                used.add(num)

    # Print matrix
    for row in a:
        print(*row)