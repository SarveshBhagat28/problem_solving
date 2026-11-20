n = int(input())
cards = list(map(int, input().split()))

left = 0
right = n - 1
sereja = 0
dima = 0
sereja_turn = True

while left <= right:
    if cards[left] > cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1

    if sereja_turn:
        sereja += chosen
    else:
        dima += chosen

    sereja_turn = not sereja_turn

print(sereja, dima)