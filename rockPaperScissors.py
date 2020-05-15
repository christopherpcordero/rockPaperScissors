# Rock Paper Scissors
# Christopher "Wuayna" Cordero 
# 01 APR 2020
# 
# 
# GOAL: Create a program that plays Rock, Paper, Scissors with you. 
# FLOW:
#   Prompt the user for either rock paper or scissors 
#   Genereate rock paper scissors as the opponent
#   Compare the two to see who wins
# FUNCS:
#   play_game
# 
# 
# EXTRAS:
#   keep score 
#   add username
# 
import random

#Variables
turn_is_Valid = False
is_Winner = False
possible_choices = ['r','s','p']
choice = ''
opponent_choice = ''



#Starting Prompt
def display_game():
    print("\n")
    print("Welcome to Rock, Paper, Scissors!\n")
    print("\n")
    print("r - Rock")
    print("p - Paper")
    print("s - Scissors")
    return

#Get choice from User
def play_game():
    global choice
    choice = input("\nEnter your choice:\n")
    while choice not in possible_choices:
        choice = input("Enter your choice:\n")
    return
    
#Play as computer
def opponent_Generator():
    global opponent_choice
    opponent_number = random.randrange(1,4)
    if opponent_number == 1:
        opponent_choice = 'r'
    elif opponent_number == 2:
        opponent_choice = 'p'
    elif opponent_number == 3:
        opponent_choice = 's'

#Compare to find a winner
def check_Winner():
    global choice
    global opponent_choice
    if choice == 'r':
        if opponent_choice == 's':
            print("YOU WIN! The computer picked SCISSORS\n")
        elif opponent_choice == 'p':
            print("You lost. The computer picked PAPER\n")
        else:
            print("Its a tie. You both picked ROCK\n")
    elif choice == 'p':
        if opponent_choice == 'r':
            print("YOU WIN! The computer picked ROCK.\n")
        elif opponent_choice == 's':
            print("You lost. The computer picked SCISSORS\n")
        else:
            print("Its a tie. You both picked PAPER\n")
    elif choice == 's':
        if opponent_choice == 'p':
            print("YOU WIN! The computer picked PAPER\n")
        elif opponent_choice == 'r':
            print("You lost. The computer picked ROCK\n")
        else:
            print("Its a tie. You both picked SCISSORS\n")

    return



#RUN THE GAME !
display_game()
play_game()
opponent_Generator()
check_Winner()