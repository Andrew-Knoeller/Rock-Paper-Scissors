from random import randint

# Array for computer to choose from
CHOICES = ["rock", "paper", "scissors"]

# Function for one round game
def oneRound():
    computer = CHOICES[randint(0,2)]                                    # Computer picks a random choice from the array
    playerTotal = 0                                                     # Set player and computer totals to 0 to start
    computerTotal = 0                                    
    while playerTotal <= 1 or computerTotal <= 1:                       # For some reason this while loop doesn't work right. Line 53 makes up for it. Wish I knew why
                                                                        # It continues to go through the loop even when the expression returns false

        player = input("Rock, Paper, Scissors? \n")
        if player.lower() == computer.lower():                          # If statement for a tie game. uses lowers function to correct capitilization errors
            print("Tie! \n")
            print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")          # Print current score

        elif player.lower() == "rock":                                                              # Series of elif statements to decide winner
            if computer.lower() == "paper":
                print("You lose!", computer, "covers", player, "\n")
                computerTotal = computerTotal + 1                                                   # Add 1 to win total
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")
            else:
                print("You win!", player, "smashes", computer, "\n")
                playerTotal = playerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")

        elif player.lower() == "paper":
            if computer.lower() == "scissors":
                print("You lose!", computer, "cut", player, "\n")
                computerTotal = computerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")
            else:
                print("You win!", player, "covers", computer, "\n")
                playerTotal = playerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")

        elif player.lower() == "scissors":
            if computer.lower() == "rock":
                print("You lose...", computer, "smashes", player, "\n")
                computerTotal = computerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")
            else:
                print("You win!", player, "cut", computer, "\n")
                playerTotal = playerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")
        else:
            print("Not a valid selection, Please try again")

        computer = CHOICES[randint(0,2)]

        if playerTotal >=1 or computerTotal >= 1:                                           # Fix for line 14
            print("You Won! \n")
            break
        else:
            continue 





# Function for a three round game 
def threeRound():
    computer = CHOICES[randint(0,2)]                                    # Computer picks a random choice from the array
    playerTotal = 0                                                     # Set player and computer totals to 0 to start
    computerTotal = 0                                    
    while playerTotal <= 3 or computerTotal <= 3:                       # For some reason this while loop doesn't work right. Line 109 makes up for it. Wish I knew why

        player = input("Rock, Paper, Scissors? \n")
        if player.lower() == computer.lower():                          # If statement for a tie game
            print("Tie! \n")
            print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")          # Print current score

        elif player.lower() == "rock":                                  # Series of elif statements to decide winner
            if computer.lower() == "paper":
                print("You lose!", computer, "covers", player, "\n")
                computerTotal = computerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")
            else:
                print("You win!", player, "smashes", computer, "\n")
                playerTotal = playerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")

        elif player.lower() == "paper":
            if computer.lower() == "scissors":
                print("You lose!", computer, "cut", player, "\n")
                computerTotal = computerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")
            else:
                print("You win!", player, "covers", computer, "\n")
                playerTotal = playerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")

        elif player.lower() == "scissors":
            if computer.lower() == "rock":
                print("You lose...", computer, "smashes", player, "\n")
                computerTotal = computerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")
            else:
                print("You win!", player, "cut", computer, "\n")
                playerTotal = playerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")
        else:
            print("Not a valid selection, Please try again")

        computer = CHOICES[randint(0,2)]                                                    # computer picks again for next iteration

        if playerTotal >=3 or computerTotal >= 3:                                           # Fix for the while loop
            print("You Won! \n")
            break
        else:
            continue


# Function for five round game
def fiveRound():
    computer = CHOICES[randint(0,2)]                                    # Computer picks a random choice from the array
    playerTotal = 0                                                     # Set player and computer totals to 0 to start
    computerTotal = 0                                    
    while playerTotal <= 5 or computerTotal <= 5:                       # For some reason this while loop doesn't work right. Line 163 makes up for it. Wish I knew why
                                                                        # It continues to go through the loop even when the expression returns false

        player = input("Rock, Paper, Scissors? \n")
        if player.lower() == computer.lower():                          # If statement for a tie game. uses lowers function to correct capitilization errors
            print("Tie! \n")
            print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")          # Print current score

        elif player.lower() == "rock":                                                              # Series of elif statements to decide winner
            if computer.lower() == "paper":
                print("You lose!", computer, "covers", player, "\n")
                computerTotal = computerTotal + 1                                                   # Add 1 to win total
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")
            else:
                print("You win!", player, "smashes", computer, "\n")
                playerTotal = playerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")

        elif player.lower() == "paper":
            if computer.lower() == "scissors":
                print("You lose!", computer, "cut", player, "\n")
                computerTotal = computerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")
            else:
                print("You win!", player, "covers", computer, "\n")
                playerTotal = playerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")

        elif player.lower() == "scissors":
            if computer.lower() == "rock":
                print("You lose...", computer, "smashes", player, "\n")
                computerTotal = computerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")
            else:
                print("You win!", player, "cut", computer, "\n")
                playerTotal = playerTotal + 1
                print("Score is: player - ", playerTotal, " computer - ", computerTotal, "\n")
        else:
            print("Not a valid selection, Please try again")

        computer = CHOICES[randint(0,2)]

        if playerTotal >= 5:                                           # Fix for line the while loop
            print("You Won! \n")
            break
        elif computerTotal >= 5:
            print("You Lost! \n")
            break
        else:
            continue 



# Main logic for game:

# Menu to select game mode, help or exit
menuSelection = input("Welcome to Rock, Paper, Scissors \n Please select from the options: \n \n1 - Play Game \n2 - Instructions \n3 - Exit \n \n")

# While loop for the menu. If you select to start, it asks what game mode and starts the chosen mode.
# Instructions shows the game rules and then returns to selection menu
# choosing exit leaves the program and game 
while menuSelection != "3":
    if menuSelection == "1":
        gameMode = input("\n Select game mode: \n \n 1--One round game \n 2--Best of three \n 3--Best of five \n")
        if gameMode == "1":
            oneRound()
            menuSelection = input("Welcome to Rock, Paper, Scissors \n Please select from the options: \n \n1 - Play Game \n2 - Help/Instructions \n3 - Exit \n \n")
        else:
            if gameMode == "2":
                threeRound()
                menuSelection = input("Welcome to Rock, Paper, Scissors \n Please select from the options: \n \n1 - Play Game \n2 - Help/Instructions \n3 - Exit \n \n")
            else:
                if gameMode == "3":
                    fiveRound()
                    menuSelection = input("Welcome to Rock, Paper, Scissors \n Please select from the options: \n \n1 - Play Game \n2 - Help/Instructions \n3 - Exit \n \n")
    else:
        if menuSelection == "2":
            print("\n Each player will pick between rock, paper, or scissors \n")
            print("Rock wins over scissors (because rock smashes scissors)")
            print("Scissors wins over paper (because scissors cut paper)")
            print("Paper wins over rock (because paper covers rock) \n")
            menuSelection = input("Welcome to Rock, Paper, Scissors \n Please select from the options: \n \n1 - Play Game \n2 - Help/Instructions \n3 - Exit \n \n")
        else:
            if menuSelection == "3":
                input(" \n Thanks for playing! Press any key to exit")
            else:
                if menuSelection != 1 or menuSelection != 2 or menuSelection != 3:
                    print("Invalid selection, Please try again \n")
                    menuSelection = input("Welcome to Rock, Paper, Scissors \n Please select from the options: \n \n1 - Play Game \n2 - Help/Instructions \n3 - Exit \n \n")

input(" \n Thanks for playing! Press any key to exit")

# Hello Professor, I don't quite understand why the while loop will not stop iterating when the expression returns false. If you know what the error is
# in my code, please leave me a comment on this when you grade it if possible. I know you are probably really busy, but I would love to understand what's
# going wrong. I made a fix for it as you will see with a final if statement in each function. I honestly hated doing that but It was the only way I could
# get it to work correctly

# Anyways hope you enjoy my game and I really enjoyed your class this semester. I learned alot and really appreciate your teaching. The course was awesome!
# Thanks and happy holidays!


