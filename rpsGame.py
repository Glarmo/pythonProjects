import random, sys
print("Rock Paper Scissors")
print("Enter move: (R)ock, (P)aper, (S)cissors or (Q)uit")
wins = 0
loses = 0
ties = 0

while True: #game loop
    print ("Wins: "+str(wins)+" Loses: "+str(loses)+" Ties: "+str(ties))
    while True:
        playerMove = input().upper()
        if playerMove == 'Q':
            sys.exit()
        elif playerMove == 'R' or playerMove == 'P' or playerMove == 'S':
            break
        print ("Please choose either R, P, S or Q")

    if playerMove == 'R':
        print("Rock versus....")
    elif playerMove == 'P':
        print ("Paper versus....")
    else:
        print ("Scissors versus...")

    randomNumber = random.randint(1,3)
    #Determine computers move
    if randomNumber == 1:
        computerMove = 'R'
        print ("Rock!")
    elif randomNumber == 2:
        computerMove = 'P'
        print ("Paper!")
    else:
        computerMove = 'S'
        print("Scissors!")

    #Determine winner
    if playerMove == computerMove:
        print("Tie!")
        ties = ties +1
    elif playerMove == 'R' and computerMove == 'S':
        print("You Win!")
        wins = wins +1
    elif playerMove == 'P' and computerMove == 'R':
        print("You Win!")
        wins = wins +1
    elif playerMove == 'S' and computerMove == 'P':
        print("You Win!")
        wins = wins +1
    else:
        print ("You lose...")
        loses = loses +1
