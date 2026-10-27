t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    values = [a[i] + a[i + 2] - a[i + 4] for i in range(n - 4)]

    freq = {}
    ans = 0

    for i, v in enumerate(values):
        ans += freq.get(v, 0)
        if i >= 2 and values[i - 2] == v:
            ans -= 1
        if i >= 4 and values[i - 4] == v:
            ans -= 1
        freq[v] = freq.get(v, 0) + 1

    print(ans)
