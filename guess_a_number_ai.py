#Guess a Number ai game
#Dammorah J.


import random

# config
low = 1
high = 100
import math

limit_calc = (math.log(high, 2))

limit = math.ceil(limit_calc)


# helper functions
def show_start_screen():
    print("   ______                        ___       _   __                __                 ___      ____")
    print("  / ____/_  _____  __________   /   |     / | / /_  ______ ___  / /_  ___  _____   /   |    /  _/")
    print(" / / __/ / / / _ \/ ___/ ___/  / /| |    /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/  / /| |    / /  ")
    print("/ /_/ / /_/ /  __(__  |__  )  / ___ |   / /|  / /_/ / / / / / / /_/ /  __/ /     / ___ |_ _/ /_  ")
    print("\____/\__,_/\___/____/____/  /_/  |_|  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     /_/  |_(_)___(_) ")
    print("                                                                                                 ")

def show_credits():
    print(" _____    _ _ _           _   _              ______                                          _      ")
    print("|  ___|  | (_) |         | | | |          _  |  _  \                                        | |     ")
    print("| |__  __| |_| |_ ___  __| | | |__  _   _(_) | | | |__ _ _ __ ___  _ __ ___   ___  _ __ __ _| |__   ")
    print("|  __|/ _` | | __/ _ \/ _` | | '_ \| | | |   | | | / _` | '_ ` _ \| '_ ` _ \ / _ \| '__/ _` | '_ \  ")
    print("| |__| (_| | | ||  __/ (_| | | |_) | |_| |_  | |/ / (_| | | | | | | | | | | | (_) | | | (_| | | | | ")
    print("\____/\__,_|_|\__\___|\__,_| |_.__/ \__, (_) |___/ \__,_|_| |_| |_|_| |_| |_|\___/|_|  \__,_|_| |_| ")
    print("                                     __/ |                                                          ")
    print("                                    |___/         Final configuration date: 10/6/17                 ")

def get_guess(current_low, current_high):
    """
    Return a truncated average of current low and high.
    """
    guess = (current_high + current_low) // 2
    return guess

def pick_number():
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    print("Choose a number between " + str(low) + " and " + str(high) + ", and I will try to guess your number")
    print(" ")
    print(" ")
    print("After I have guessed tell me if it was: too high, too low, or correct.")

def get_name():
    print("Before we begin, what is your name?")
    name = input()
    input("Press enter when you have choosen your number and you are ready to continue " + str(name) + ". I will try to guess it in 7 tries.")
    return name

def check_guess(guess, name, tries, limit):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    while True:
        print()
        print()
        decision = input("Is the number you are thinking of " + str(guess) + ", " + str(name) + "? Is it correct? Too high? Too low?")
        print(" Guess " + str(tries) + " of " + str(limit) + " is " + str(guess) + ".")
        print()
        decision = decision.lower()
        
        if decision in ["too low", "l", "lower"]:
            check = -1
            return check
        elif decision in ["yes", "y", "yeah", "correct"]:
            print("I've guessed your number!")
            check = 0
            return check
        elif decision in ["too high", "h", "higher"]:
            check = 1
            return check
        else:
            print( str(name) + ",you have entered an invalid staterment I cannot understand.")
def show_result(guess, check, name,tries):
    """
    Says the result of the game. (The computer might always win.)
    """

    if check == 0:
        print("The number you were thinking of was " + str(guess) + "!")
        print("I have guessed your number in " + str(tries) + " tries!")
    else:
        print("Looks like I lost... Sorry " + str(name) + ". Would you let me try again?")
        

def play_again(name):
    while True:
        decision = input("Would you like to play again, " + str(name) + " ? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'yes' or 'no'.")

def play(name):
    current_low = low
    current_high = high
    check = -1

    tries = 0
    
    pick_number()

    
    while check != 0 and tries < limit:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess, name, tries, limit)

        if check == -1:
            current_low = int(guess)
        
        elif check == 1:
           current_high = int(guess)
           
        tries += 1

    show_result(guess, check, name, tries)


# Game starts running here
show_start_screen()
name = get_name()

playing = True

while playing:
    play(name)
    playing = play_again(name)

show_credits()


