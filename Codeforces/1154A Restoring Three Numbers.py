x = list(map(int, input().split()))

s = max(x)
x.remove(s)

result = []

for num in x:
    result.append(s - num)

result.reverse()

print(*result)