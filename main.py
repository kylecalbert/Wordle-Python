import random
import sys
from termcolor import colored
def print_menu():   
    print("Type a 5 letter Word and hit enter!\n")

def read_random_word():
    with open ("words.text") as f:
        words = f.read().splitlines() #create a seperate value in array for each line in file which is individual word
        return random.choice(words)
    

print_menu()
word = read_random_word() #going to put random word into this vvariable

play_again = ""
while(play_again!="q"):
    
    for attempt in range(1,7):
        guess = input().lower() #this converts users input to lowercase
        sys.stdout.write('\x1b[1A')
        sys.stdout.write('\x1b[2K')


        for i in range(min(len(guess),5)) :
            if guess[i] == word[i]:   #if guess index is same as word index, it is in correct spot
                print(colored(guess[i], "green"), end="")

            elif guess[i] in word:
                print(colored(guess[i], 'yellow'), end= "")

            else:
                print(guess[i], end="")
        print()

        if guess == word:
         print(colored( f"Congrats! you got the wordle in {attempt} attempts, 'red"))
         break

        





