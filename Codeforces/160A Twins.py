n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

total = sum(a)
s = 0
count = 0

for coin in a:
    s += coin
    count += 1

    if s > total - s:
        break

print(count)