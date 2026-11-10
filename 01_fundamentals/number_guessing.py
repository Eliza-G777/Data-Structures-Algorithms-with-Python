"""
Number Guessing Game

The computer picks a random number from 1 to 100.
The player keeps guessing until they get it right.

Reference solution I studied (not my original work).
"""

# Step 1: import the random module
import random

LOW = 1
HIGH = 100

# Step 2: pick a secret number between LOW and HIGH
secret = random.randint(LOW, HIGH)

# Step 3: set the guess counter to 0
guesses = 0

print(f"I'm thinking of a number between {LOW} and {HIGH}.")

# Step 4: repeat until the player guesses correctly
while True:
    # 4a. ask the player for a guess
    text = input("Your guess: ")

    # 4b. if it's not a number, tell them and ask again
    try:
        guess = int(text)
    except ValueError:
        print("Please enter a whole number.")
        continue  # go back to the top of the loop; this doesn't count as a guess

    if guess < LOW or guess > HIGH:
        print(f"Pick a number from {LOW} to {HIGH}.")
        continue

    # 4c. add 1 to the counter
    guesses += 1

    # 4d. compare the guess with the secret number
    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
        break  # leave the loop

# Step 5: print how many guesses it took
print(f"You got it in {guesses} guesses.")
