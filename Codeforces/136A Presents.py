n = int(input())
p = list(map(int, input().split()))

ans = [0] * n

for i, receiver in enumerate(p, start=1):
    ans[receiver - 1] = i

print(*ans)