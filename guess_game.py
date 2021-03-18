# Guess random number games
import random

#game for the user to guess the computer's random number
def guess(num):

    random_number = random.randint(1, num)
    user_guess = 0

    while user_guess != random_number:
        user_guess = int(input(f'Guess a number between 1 and {num}: '))
        
        if user_guess < random_number:
            print("Your guess is too low. Guess again.")
        elif user_guess > random_number:
            print("Your guess is too high. Guess again.")
        else:
            print(f"Congratulations! You have guessed the right number: {random_number}.")


#game for the computer to guess the user's random number
def computer_guess(num):
    low = 1
    high = num
    feedback = ''

    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()
        
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"The computer guessed your number {guess} correctly!")

computer_guess(100)