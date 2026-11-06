n = int(input())
users = {}

for _ in range(n):
    name = input()

    if name not in users:
        print("OK")
        users[name] = 1
    else:
        new_name = name + str(users[name])

        while new_name in users:
            users[name] += 1
            new_name = name + str(users[name])

        print(new_name)
        users[new_name] = 1