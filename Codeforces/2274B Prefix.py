def solve():
    t = int(input())
    answers = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        ans = a[0]
        max_sum = a[0]
        min_sum = a[0]
        for i in range(1, n):
            ai = a[i]
            best_abs_sum = max(abs(max_sum), abs(min_sum))
            ans = max(ans, ai + best_abs_sum)
            new_max = max(ai, max_sum + ai, 2 * max_sum + ai)
            new_min = min(ai, min_sum + ai, 2 * min_sum + ai)
            max_sum, min_sum = new_max, new_min
        answers.append(str(ans))
    print("\n".join(answers))

if __name__ == "__main__":
    solve()