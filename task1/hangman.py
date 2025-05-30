import random

def hangman():
    
    word_list = ['python', 'hangman', 'developer', 'program', 'computer', 'science']
    secret_word = random.choice(word_list).lower()
    guessed_letters = set()
    correct_letters = set(secret_word)
    tries = 6  

    print("🎮 Welcome to Hangman!")
    print("_ " * len(secret_word))

    while tries > 0 and correct_letters:
        guess = input("\nGuess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in correct_letters:
            correct_letters.remove(guess)
            print("✅ Correct!")
        else:
            tries -= 1
            print(f"❌ Incorrect! Tries left: {tries}")

        display_word = [letter if letter in guessed_letters else "_" for letter in secret_word]
        print("Word: " + " ".join(display_word))

    if not correct_letters:
        print(f"\n🎉 Congratulations! You guessed the word: '{secret_word}'")
    else:
        print(f"\n💀 Game Over! The word was: '{secret_word}'")


if __name__ == "__main__":
    hangman()
