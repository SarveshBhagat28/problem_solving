n = int(input())
a = list(map(int, input().split()))

even = []
odd = []

for i in range(n):
    if a[i] % 2 == 0:
        even.append(i + 1)
    else:
        odd.append(i + 1)

if len(even) == 1:
    print(even[0])
else:
    print(odd[0])