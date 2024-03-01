import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "coding", "computer", "encyclopedia"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    print("Welcome to Hangman!")
    
    while True:
        word_to_guess = choose_word().lower()
        guessed_letters = set()
        attempts_left = int(len(word_to_guess) * 1.5)

        while True:
            current_display = display_word(word_to_guess, guessed_letters)
            print(f"\nWord: {current_display}")
            print(f"Attempts left: {attempts_left}")
            
            if current_display == word_to_guess:
                print("Congratulations! You've guessed the word.")
                break
            
            if attempts_left == 0:
                print(f"Sorry, you've run out of attempts. The correct word was '{word_to_guess}'.")
                break

            guess = input("Enter a letter or the whole word: ").lower()

            if guess.isalpha() and len(guess) == 1:
                if guess in guessed_letters:
                    print("You've already guessed that letter. Try again.")
                    continue

                guessed_letters.add(guess)

                if guess not in word_to_guess:
                    print("Incorrect guess!\n")
                    attempts_left -= 1
            elif guess.isalpha() and len(guess) > 1:
                if guess == word_to_guess:
                    print("Congratulations! You've guessed the word.")
                    break
                else:
                    print("Incorrect guess!\n")
                    attempts_left -= 1
            else:
                print("Invalid input! Please enter a single letter or the whole word.")
                continue

        play_again = input("If you want to play again, type 'yes': ").lower()
        if play_again != 'yes':
            print("Thanks for playing Hangman. Goodbye!")
            break

hangman()