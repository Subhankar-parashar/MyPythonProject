import random

choices = ["Gun", "Snake", "Water"]

player_score = 0
computer_score = 0

for chance in range(5):
    computer = random.choice(choices)
    player = input("Enter your choice (Gun/Snake/Water): ")

    print("Computer chose:", computer)

    if computer == player:
        print("It's a tie!")
    elif (computer == "Gun" and player == "Water") or \
        (computer == "Snake" and player == "Gun"):
        (computer == "Water" and player == "Snake") or \
        print("You won this round!")
        player_score += 1
    else:
        print("Computer won this round!")
        computer_score += 1

    print()

print("Final Score")
print("You:", player_score)
print("Computer:", computer_score)

if player_score > computer_score:
    print("You won the game!")
elif player_score < computer_score:
    print("Computer won the game!")
else:
    print("The game is a tie!")