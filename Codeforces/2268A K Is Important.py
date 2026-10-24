
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0

    if 2 * k <= n:
        ans += sum(a[k - 1 : n - k + 1])

        for i in range(k - 1):
            ans += max(a[i], a[n - 1 - i])

    else:
       
        for i in range(n - k + 1):
            ans += max(a[i], a[n - 1 - i])

    print(ans)
