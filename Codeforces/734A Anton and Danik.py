
n = int(input())
s = input()

anton = s.count('A')
danik = s.count('D')

if anton > danik:
    print("Anton")
elif danik > anton:
    print("Danik")
else:
    print("Friendship")
