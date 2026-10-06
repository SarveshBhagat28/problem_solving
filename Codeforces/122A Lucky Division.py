n = int(input())

for i in range(1, 1001):
    if all(c in "47" for c in str(i)):
        if n % i == 0:
            print("YES")
            break
else:
    print("NO")