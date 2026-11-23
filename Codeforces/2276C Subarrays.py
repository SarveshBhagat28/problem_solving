t = int(input())
answers = []

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    pref = [0] * (n + 1)
    cur = 0

    for i in range(1, n + 1):
        cur = (cur + a[i - 1]) % k
        pref[i] = cur

    count = [0] * k
    ans = 0

    for j in range(n + 1):
        idx = j - k - 1
        if idx >= 0:
            count[pref[idx]] += 1

        ans += count[pref[j]]

    answers.append(str(ans))

print("\n".join(answers))