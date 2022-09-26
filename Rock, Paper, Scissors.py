import random

while True:
    choices = ["rock", "paper", "scissors"] #enters the choices in an array

    computer = random.choice(choices) #randomizes the choices in the above list that could be picked from the computer  
    player = None

    while player not in choices:
        player = input("rock, player, or scissors?: ").lower()

    if player ==computer:
        print("Computer chose: ", computer)
        print("Player chose: ", player)
        print("Tie!")

    elif player == "rock":
        if computer == "scissor":
            print("Computer chose: ", computer)
            print("Player chose: ", player)
            print("Player Wins!")
        if computer == "paper":
            print("Computer chose: ", computer)
            print("Player chose: ", player)
            print("Computer Wins!")

    elif player == "scissor": 
        if computer == "rock":
            print("Computer chose: ", computer)
            print("Player chose: ", player)
            print("Computer Wins!")
        if computer == "paper":
            print("Computer chose: ", computer)
            print("Player chose: ", player)
            print("Player Wins!")

    play_again = input("Up for another round? yes or no : ").lower()

    if play_again != "yes":
        break

    print("Bye!")

