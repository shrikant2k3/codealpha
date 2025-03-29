import random

# List of words to choose from
word_list = ["python", "programming", "hangman", "developer", "challenge"]

# Function to choose a random word
def get_random_word():
    return random.choice(word_list).lower()

# Function to display the current state of the word
def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Main game function
def hangman():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6  # Number of incorrect guesses allowed

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord: ", display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {attempts}")
        guess = input("Guess a letter: ").lower()

        # Check if input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        # If the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print("Good job! You guessed a correct letter.")
        else:
            print("Oops! That letter is not in the word.")
            attempts -= 1

        # Check if the player has guessed the whole word
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print("\nGame Over! The word was:", word)

# Run the game
if __name__ == "__main__":
    hangman()
