import random

# List of words to choose from
word_list = ["python", "javascript", "hangman", "programming", "development"]

# Hangman stages
stages = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """
]

def choose_word():
    return random.choice(word_list)

def display_hangman(tries):
    return stages[tries]

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    tries = len(stages) - 1

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("\n")

    while len(word_letters) > 0 and tries > 0:
        print("You have", tries, "tries left.")
        print("Used letters: ", " ".join(used_letters))
        
        # Show the current guessed word with underscores
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", " ".join(word_list))
        
        user_letter = input("Guess a letter: ").lower()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("")
            else:
                tries -= 1
                print(f"\nYour letter, {user_letter}, is not in the word.")
        elif user_letter in used_letters:
            print("\nYou have already used that letter. Guess another letter.")
        else:
            print("\nInvalid character. Please enter a valid letter.")
        
        print(display_hangman(tries))
        print("\n")

    if tries == 0:
        print("You lost! The word was", word)
    else:
        print("Congratulations! You guessed the word", word, "!!")

if __name__ == "__main__":
    play_hangman()
