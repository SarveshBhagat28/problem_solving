def solve(k,n,w):
    total=0
    for i in range(w + 1):
        total+=k*i
    if total > n:
        print(total - n)
    else:
        print("0")

k,n,w=map(int,input().split())
solve(k,n,w)