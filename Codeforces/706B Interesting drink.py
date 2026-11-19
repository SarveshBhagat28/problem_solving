n = int(input())
prices = list(map(int, input().split()))
prices.sort()

q = int(input())
answers = []

for _ in range(q):
    money = int(input())

    left = 0
    right = n

    while left < right:
        mid = (left + right) // 2
        if prices[mid] <= money:
            left = mid + 1
        else:
            right = mid

    answers.append(str(left))

print("\n".join(answers))