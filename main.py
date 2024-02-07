import random
import sys
from termcolor import colored
import nltk
from nltk.corpus import words

def print_menu():   
    print("Type a 5 letter Word and hit enter!\n")

def read_random_word():
    return random.choice(words.words())

# Ensure NLTK data is downloaded
nltk.download('words')

# Load NLTK words corpus
word_list = words.words()
words_five = [word for word in word_list if len(word) == 5]

print_menu()

play_again = ""
while play_again != "q":
    word = read_random_word()

    for attempt in range(1, 7):
        guess = input("Your guess: ").lower()

        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')

        for i in range(min(len(guess), 5)):
            if guess[i] == word[i]:
                print(colored(guess[i], "green"), end="")
            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end="")
            else:
                print(guess[i], end="")
        
        print()

        if guess == word:
            print(colored(f"Congrats! You got the wordle in {attempt} attempts!", 'red'))
            break
        elif attempt == 6:
            print(f"Sorry, the word was: {word}")

    play_again = input("Want to play again? Type 'q' to exit: ")
