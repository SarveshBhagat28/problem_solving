
n = int(input())

current = 0
capacity = 0

for i in range(n):
    a, b = map(int, input().split())
    current = current - a + b
    capacity = max(capacity, current)

print(capacity)
