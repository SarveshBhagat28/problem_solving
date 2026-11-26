t = int(input())

for _ in range(t):
    s = input().strip()
    n = len(s)

    has_long_block = False
    has_internal_single = False

    i = 0
    while i < n:
        j = i

        while j < n and s[j] == s[i]:
            j += 1

        length = j - i

        if length >= 3:
            has_long_block = True
        if length == 1 and i > 0 and j < n:
            has_internal_single = True

        i = j

    answer = 1
    if has_long_block:
        answer += 1
    if has_internal_single:
        answer += 1

    print(answer)