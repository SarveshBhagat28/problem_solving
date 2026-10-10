
n = int(input())
s = list(map(int, input().split()))

count = [0] * 5
for x in s:
    count[x] += 1

taxis = count[4]

# Groups of 3 take a taxi, preferably with one group of 1
taxis += count[3]
count[1] = max(0, count[1] - count[3])

# Groups of 2: two groups per taxi
taxis += count[2] // 2
count[2] %= 2

# One remaining group of 2 can fit with up to two groups of 1
if count[2]:
    taxis += 1
    count[1] = max(0, count[1] - 2)

# Remaining groups of 1: four per taxi
taxis += (count[1] + 3) // 4

print(taxis)
