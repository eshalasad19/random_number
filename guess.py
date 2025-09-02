import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5
    print("\n🎯 Guess the number from 1 to 100!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter a number to guess the real number! "))
            attempts += 1

            if guess == number:
                print(f"🎉 You won this game in {attempts} attempts!")
                break
            elif guess < number:
                print("Too Low!")
            else:
                print("Too High!")

        except ValueError:
            print("❌ Invalid Number, please enter a valid integer.")
    if attempts == max_attempts and guess != number:
        print(f"😢 You have reached maximum attempts! The number was {number}")

# ==== Game Loop ====
while True:
    play_game()
    choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if choice not in ("yes", "y"):
        print("👋 Thanks for playing! Goodbye.")
        break
