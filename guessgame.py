# import random

# #guessgame(computer)
# def guess(x):
#     random_number = random.randint(1, x)  # Corrected the typo in random_number
#     guess = 0
#     while guess != random_number:
#         guess = int(input(f"Guess a number between 1 and {x}: "))
#         if guess < random_number:
#             print("Sorry, guess again. Too low.")
#         elif guess > random_number:
#             print("Sorry, guess again. Too high.")

#     print(f"Yay, Congrats! You have guessed the number {random_number} correctly!")

#guessgame(user)

import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""  # Start with an empty string for feedback
    
    while feedback != "c":
        if low != high:  # If there's more than one option to guess
            guess = random.randint(low, high)
        else:  # When low equals high, the computer has narrowed down to one number
            guess = low
        
        feedback = input(f"Is {guess} too high(h), too low(l), or correct(c)? ").lower()
        
        if feedback == 'h':  # If the guess was too high
            high = guess - 1 
        elif feedback == 'l':  # If the guess was too low
            low = guess + 1
    
    print(f"Yay! The computer guessed your number, {guess}, correctly!")  # Outside the loop

# Call the function with a number range
computer_guess(10)
