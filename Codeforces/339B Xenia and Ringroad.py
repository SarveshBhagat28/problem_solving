n, m = map(int, input().split())
a = list(map(int, input().split()))

current = 1
time = 0

for house in a:
    if house >= current:
        time += house - current
    else:
        time += n - current + house

    current = house

print(time)