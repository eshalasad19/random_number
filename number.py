# === Number Guessing Game ===

# importing the random module 
import random

# code to generate random number  
number = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("Guess the number from 1 to 100!")

while attempts < max_attempts:
    try:
        guess = int(input(f"Attempt: {attempts + 1} Enter your guess: "))
        attempts += 1
        if guess == number:
            print("Correct You guessed it!")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too High!")
    except ValueError:
        print("Please Enter a valid number!")

if attempts == max_attempts and guess != number:
    print(f"Out of attempts! the number was {number}.")
