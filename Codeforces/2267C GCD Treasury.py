def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def tokens():
    while True:
        try:
            line = input()
        except EOFError:
            return

        for value in line.split():
            yield int(value)

it = tokens()
t = next(it)
answers = []

for _ in range(t):
    n = next(it)
    x = next(it)
    sums = {}
    for _ in range(n):
        a = next(it)
        g = gcd(a, x)
        sums[g] = sums.get(g, 0) + a

    if x == 1:
        answers.append("0")
        continue

    reachable = [x]
    used = {x}

    for b in sums:
        if b == 1:
            continue

        size = len(reachable)

        for i in range(size):
            g = gcd(reachable[i], b)

            if g > 1 and g not in used:
                used.add(g)
                reachable.append(g)

    answer = 0

    for d in reachable:
        current = 0

        for b, total in sums.items():
            if b > 1 and b % d == 0:
                current += total

        answer = max(answer, current)

    answers.append(str(answer))

print("\n".join(answers))