#Guess a Number ai game
#Dammorah J.


import random

# config
low = 1
high = 100


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    pass
    
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
    print("Choose a number between " + str(low) + " and " + str(high) + ", and I will try to guess yout number")
    print(" ")
    print(" ")
    print("After I have guessed tell me if it was: too high, too low, or correct")
    input("Press enter when you have choosen your number and you are ready to continue.")

def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    print(" ")
    print(" ")
    print(" ")
    decision = input("Is the number you are thinking of " + str(guess) + "? Is it correct? Too high? Too low?")
    print(" ")
    print(" ")
    print(" ")
    decision = decision.lower()
    
    if decision == "too low":
        check = -1
        return check
    if decision == "yes":
        print("I've guessed your number!")
        check = 0
        return check
    if decision == "too high":
        check = 1
        return check
    
def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    #fix show results
    print("The number you were thinking or was  !")
    

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'yes' or 'no'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            current_low = int(guess)
        
        elif check == 1:
           current_high = int(guess)
        

    show_result()


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()


