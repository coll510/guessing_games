import random

# Rock Paper Scissors game
def play():
    user = input("What is your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie."

    if is_win(user, computer):
        return "You won!"

    # if computer wins if is_win(computer, user)
    return "You lost!"

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())

#Hangman Game
from words import words
import string

def get_valid_word(words):
    #choose random word from words list in words.py
    word = random.choice(words) 

    #get a word that doesn't have a space or dash in it
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():

    word = get_valid_word(words)

    #this variable saves all the letters in the word 
    #keep track of what's already been guessed in the word
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #keep track of what user has guessed

    lives = 7

    #get user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        print("You have ", lives, " lives left and you have used these letters: ", " ".join(used_letters))

        # what current word is without characters that they haven't guessed
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else: 
                # remove a life if the letter isn't in the word
                lives -= 1 
                print("The letter", user_letter, " is not in the word.")

        elif user_letter in user_letters:
            print("You already guessed that letter. Try again.")

        else:
            print("Invalid character. Try again.")


    # exit while loop when length words == 0 or when lives == 0
    if lives == 0:
        print("Sorry! You died. The word was ", word, ".")
    else:
        print("You guessed the word ", word, "! Congratulation!")

hangman()














