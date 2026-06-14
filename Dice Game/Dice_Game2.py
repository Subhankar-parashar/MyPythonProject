import random

dice_art = {

1: ("┌──────────────┐",
    "│              │",
    "│              │",
    "│      ●       │",
    "│              │", 
    "│              │", 
    "└──────────────┘"),

2: ("┌──────────────┐",
    "│              │",
    "│   ●          │",
    "│              │",
    "│          ●   │",
    "│              │",
    "└──────────────┘"),

3: ("┌──────────────┐",
    "│              │", 
    "│    ●         │",
    "│      ●       │",
    "│        ●     │", 
    "│              │",
    "└──────────────┘"),

4: ("┌──────────────┐",
    "│              │", 
    "│   ●      ●   │",
    "│              │",
    "│   ●      ●   │", 
    "│              │", 
    "└──────────────┘"),

5: ("┌──────────────┐",
    "│              │",
    "│   ●      ●   │",
    "│       ●      │",
    "│   ●      ●   │",
    "│              │",
    "└──────────────┘"),

6: ("┌──────────────┐",
    "│  ●       ●   │",
    "│              │",
    "│  ●       ●   │",
    "│              │",
    "│  ●       ●   │",
    "└──────────────┘")}


while True:

    total = int(input("Enter the total: "))
    dice_num = int(input("Enter the no. of dice: "))
    min_value = dice_num
    max_value = dice_num * 6

    if min_value <= total <= max_value:
        break
    else:
        print("Invalid Input")

dice = [1] * dice_num
remaining = total - sum(dice) 
while remaining > 0:
    index = random.randint(0, dice_num - 1)
    if dice[index] == 6:
        continue
    max_add = min(6 - dice[index], remaining)
    add = random.randint(1, max_add)

    dice[index] += add
    remaining -= add 

print("Dice values:", dice)
print("Total:", sum(dice))
print()
for _ in range(dice_num):
    for die in dice_art.get(dice[num]):
        print(die)
