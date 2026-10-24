s = input()
target = "hello"
j = 0

for ch in s:
    if j < len(target) and ch == target[j]:
        j += 1

if j == len(target):
    print("YES")
else:
    print("NO")