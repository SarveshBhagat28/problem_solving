def solve(l):
    l.sort()
    print(l[1])
t=int(input())
for i in range(t):
    l=list(map(int,input().split()))
    solve(l)