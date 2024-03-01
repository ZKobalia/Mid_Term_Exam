import random

def guess_number_game():
    while True:
        max_attempts = 7
        print("Welcome to the Number Guessing Game!")
        print(f"I have selected a number between 1 and 100. Can you guess it in {max_attempts} attempts? \n")

        secret_number = random.randint(1, 100)

        attempts = 0
        guessed_correctly = False

        while attempts < max_attempts:
            try:
                guess = int(input(f"Attempt {attempts+1}. Enter your guess: "))
                if guess < 1 or guess > 100:
                    print("Invalid input! Please enter a number between 1 and 100.")
                    continue
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
                guessed_correctly = True
                break
            elif guess < secret_number:
                print("Too low! Try again. \n")
            else:
                print("Too high! Try again. \n")

        if not guessed_correctly:
            print(f"Sorry, you've reached the maximum number of attempts. The correct number was {secret_number}.")

        play_again = input("If you want to play again, type 'yes': ").lower()
        if play_again != 'yes':
            print("Thanks for playing. Goodbye!")
            break

guess_number_game()
