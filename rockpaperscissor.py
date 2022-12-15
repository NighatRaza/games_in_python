from random import randint

t = ["Rock", "Paper", "Scissors"]

#a random play to the computer
computer = t[randint(0,2)]

#player flag
player = False

while player == False:

    player = input("Rock, Paper, Scissors?\n")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's not a valid play. Check your spelling!")

    # play again
    ask = input('Do you want to play again? Press Y for yes\n')
    
    if ask == 'Y' or ask == 'y':
        player = False
        computer = t[randint(0,2)]
    else:
        player = True
