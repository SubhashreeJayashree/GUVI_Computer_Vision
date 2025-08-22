import random

def guess_number_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 7 chances to guess it. Good luck!")

    # Generate random number
    secret_number = random.randint(1, 100)
    chances = 10

    for attempt in range(1, chances + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{chances} - Enter your guess: "))

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempt} attempts.")
                break
        except ValueError:
            print(" Invalid input! Please enter a number.")
    else:
        print(f" Sorry, you're out of chances. The number was {secret_number}.")

# Run the game
guess_number_game()
