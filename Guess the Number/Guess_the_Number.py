import random
x = random.randint(1, 10)
attempts = 0
while True:
    Guess = int(input("Guess the number between 1 and 100: "))
    attempts += 1
    if Guess == x:
        print(f"Congratulations! You guessed the number correctly in {attempts} attempts .")
        break
    elif Guess < x:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.") 



