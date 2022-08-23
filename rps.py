import random

while True:
    ch = ["rock","paper","scissors"]
    rand = random.choice(ch)
    player = None
    while player not in ch:
        player = input("Choose: Rock or Paper or Scissors:").lower()

    if rand == player:
        print("computer: ", rand)
        print("Player: ", player)
        print("Its a draw!")
    elif player == "rock":
        if rand == "paper":
            print("computer: ", rand)
            print("Player: ", player)
            print("You lose!")
        else:
            print("computer: ", rand)
            print("Player: ", player)
            print("You win!")
    elif player == "paper":
        if rand == "rock":
            print("computer: ", rand)
            print("Player: ", player)
            print("You win!")
        else:
            print("computer: ", rand)
            print("Player: ", player)
            print("You lose!")
    else:
        if rand == "rock":
            print("computer: ", rand)
            print("Player: ", player)
            print("you lose!")
        else:
            print("computer: ", rand)
            print("Player: ", player)
            print("You win")

    play_once_more = input("Do you like to play again(Yes/No): ").lower()

    if play_once_more != "yes":
        break

print("Nice play!!!!")