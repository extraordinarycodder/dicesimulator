import random

# Define the dice
dice = [1, 2, 3, 4, 5, 6]

# Start the game
print("Welcome to the Dice Rolling Simulator!")
while True:
    input("Press Enter to roll the dice (or q to quit): ")
    if input == "q":
        break
    else:
        roll = random.choice(dice)
        print("You rolled a", roll)

print("Thanks for playing!")
