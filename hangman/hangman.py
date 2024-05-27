import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)

    # puts the characters into singular quotes in the set
    word_letters = set(word)

    alphabet = set(string.ascii_uppercase)

    # what the user has guessed
    used_letters = set()

    print(f"The word is: {word}")

    while len(word_letters) > 0:

        print("-------------------------")
        print("You have used these letters: ", ", ".join(used_letters))

        word_list = [
            letter if letter in used_letters else "-" for letter in word]

        print('Current word: ', ' '.join(word_list))

        # getting user input
        user_letter = input('Guess a letter: ').upper()

        # creates a new set that contains all elements from alphabet that are not in used_letters and checks if user_letter is in there
        if user_letter in (alphabet - used_letters):
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You've already used that character, please try again")

        else:
            print("Invalid Character")

    print("Game completed")


hangman()
