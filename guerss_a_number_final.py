import random

# config
low = 1
high = 100
import math

limit_calc = (math.log(high, 2)
limit = math.ceil(limit_calc)

# helper functions
def show_start_screen():
    print(" ██████╗ ██╗   ██╗███████╗███████╗███████╗     █████╗     ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ ")
    print("██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ██╔══██╗    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗")
    print("██║  ███╗██║   ██║█████╗  ███████╗███████╗    ███████║    ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝")
    print("██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║    ██╔══██║    ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗")
    print("╚██████╔╝╚██████╔╝███████╗███████║███████║    ██║  ██║    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║")
    print(" ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝    ╚═╝  ╚═╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")

def show_credits():
    print("~~~~~Plagiarized by: Wakasa Hitomi~~~~~")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")
    print(" ")
    print("You may have" + limit + " guesses.")
    print(" ")
    print("You may only insert numbers in a numeric symbolled value rather than written out in letters.")
    print(" ")
    print("GoodLuck")
    print(" ")

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
        print(" ")
        print(" ")
    elif guess > rand:
        print("You guessed too high.")
        print(" ")
        print(" ")

def show_result(guess, rand):
    if guess == rand:
        print("You win! It's about time you've done something right in your life.")
    else:
        print("You never fail to disappoint, do you? The number was " + str(rand) + ".")

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
