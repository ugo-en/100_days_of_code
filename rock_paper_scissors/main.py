# module for random-related functions
import random

# Set all possible moves
possible_moves = ["rock","paper","scissors"]

# contains the user's nmame
username = ""

# set both scores
user_score = 0
comp_score = 0

# Define function whose job is to determine the winner
def decide_winner(user_move,comp_move):
    global user_score, comp_score
    """
    The way this function works is as follows:

    1. There is a list of winning combinations, each containing two
       moves, the first being the winner, and the second being the loser,
       e.g. ("rock","scissors"), signifying that rock beats scissors.
    2. Both moves are put in a tuple. The user's move first, then the
       computer's move next, like so; (user_move,comp_move).
    3. If this tuple can be found in the list of winning combinations,
       the user wins. 
    4. Else, swap the members of that tuple, like so; (comp_move,user_move)
    5. If that tuple can be found in the list of winning combos, 
       computer wins
    6. Else, it is a tie 
    7. This method is more professional than too many 'if statements'
    """
    # winning combos
    winning_combos = [("rock","scissors"),("scissors","paper"),("paper","rock")]

    # testing the first tuple to see if user wins
    if (user_move,comp_move) in winning_combos:
        # add the user's score'
        user_score += 1
        return "WIN"
    # testing the secong tuple to see if computer wins
    elif (comp_move,user_move) in winning_combos:
        # add to the computer's score
        comp_score += 1
        return "LOSE"
    else:
        return "TIE"

# define function to print out the score
def show_scores():
    global user_score, comp_score, username
    print(f"\n\nSCORE:\n\n{username}: {user_score}\nComputer: {comp_score}\n\n")


# Main program begins

# welcome user
print("\n\n\t---------- WELCOME TO UGO'S ROCK-PAPER_SCISSORS ---------- \t\n\n")

# collect user's name
username = input("What is your name? ")

# make this run over and over again
while True:
    user_move = ""
    
    # keep asking user for a move until they enter a valid move
    while user_move not in possible_moves:
        user_move = input("Enter a move; 'rock', 'paper', 'scissors': ")
    
    # randomly generate a move for the computer
    comp_move = random.choice(possible_moves)

    # show both moves
    print(f"{username} played: {user_move}\nComputer played: {comp_move}\n")

    # get the result
    result = decide_winner(user_move,comp_move)
    
    # show result
    if result == "WIN":
        print(f"{username} scored!")
    elif result == "LOSE":
        print(f"Computer scored!")
    else:
        print("TIE!!!")

    # show scores
    show_scores()

    # ask the user if they want to play again or quit
    play_again = input("Do you want to play again? (Y/N)").lower()

    if play_again != "y":
        break

# end game
print("GAME OVER\n\nFinal Scores:\n")

show_scores()
