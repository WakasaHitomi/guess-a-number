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
    pass

def pick_number():
    """
    Ask the player to think of a number between low and high.
    Then  wait until the player presses enter.
    """
    print("Choose a number between 1 and 100, and I will try to guess yout number")
    print(" ")
    print(" ")
    input("Press enter when you have choosen your number and you are ready to continue.")

def check_guess(guess):
    """
    Computer will ask if guess was too high, low, or correct.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    decision = input("How was my guess?      1= too high,   -1 = too low,   0 = I guessed it right.")
    if input(-1): print("I have guessed too low.")
            return def play(-1):
    if input(0): print("I have won!")
            return def play(0):
    if input(1): print("I have guessed too high.")
            return def play(1):
            
def show_result():
    """
    Says the result of the game. (The computer might always win.)
    """
    

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            guess = current_low
        
        elif check == 1:
           guess = current_high
        

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()


