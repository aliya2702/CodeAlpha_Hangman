import random

def hangman():
    words = ["apple", "banana", "grapes", "orange", "mango"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman Game!")
    print("_ " * len(word))

    while attempts > 0:
        try:
            guess = input("Guess a letter: ").strip().lower()
        except EOFError:
            print("\nGame ended unexpectedly.")
            print(f"The word was: {word}")
            break

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_word)

        if "_" not in display_word:
            print("Congratulations! You guessed the word!")
            break

    if attempts == 0:
        print(f"game Over! The word was '{word}'.")

hangman()