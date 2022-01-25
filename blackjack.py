import random, sys

#Get the unicode characters for the suits
hearts = chr(9829)
diamonds = chr(9830)
spades = chr(9824)
clubs = chr(9827)
backside = 'backside'

def main():
    money = 5000
    while True: #Betting loop
        if money <= 0:
            print("You've gone backrupt buddy! Try again")
            sys.exit()

        print("Money: $", money)
        bet = getBet(money) #Asks the player to input bet amount

        deck = getDeck()    #Generates a random deck of 52 cards and then grabs two cards for each player
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        print("Bet:", bet)
        while True: #Playing loop
            displayHands(playerHand, dealerHand, False)
            if getHandValue(playerHand) > 21:
                break
            move = getMove(playerHand, money - bet)

            if move == 'D': #Player is doubling down
                additionalBet = getBet(min(bet, (money-bet)))
                bet += additionalBet
                print ("Bet has increased...")
                print("Bet: ", bet)

            if move in ('H', 'D'): #Retrieves a new card
                newCard = deck.pop()
                rank, suit = newCard
                print('You drew a {} of {}.'.format(rank,suit))
                playerHand.append(newCard)

                if getHandValue(playerHand) > 21:
                    continue

            if move in ('S', 'D'):
                break

        if getHandValue(playerHand) <= 21:
            while getHandValue(dealerHand) < 17:
                print("Dealer hits...")
                dealerHand.append(deck.pop())
                displayHands(playerHand, dealerHand, False)

                if getHandValue(dealerHand) > 21:
                    break
                input('Press Enter to continue...')
                print('\n\n')

        displayHands(playerHand,dealerHand,True)

        playerValue = getHandValue(playerHand)
        dealerValue = getHandValue(dealerHand)

        #Determines the end state of the game
        if dealerValue > 21:
            print("Dealer bust, house loses! You win ${}!".format(bet))
            money += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print("House wins! You lost ${}".format(bet))
            money -= bet
        elif playerValue > dealerValue:
            print("House loses! You win ${}!".format(bet))
            money += bet
        elif playerValue == dealerValue:
            print("A tie, take your bet back.")

        input('Press Enter to continue...')
        print('\n\n')

#Retrieves bet from player and determines if valid
def getBet(maxBet):
    while True:
        print("What's your bet sir? ($1-$"+str(maxBet)+", or QUIT)")
        bet = input('> ').upper().strip()
        if bet == 'QUIT':
            print("Come back anytime!")
            sys.exit()
        if not bet.isdecimal():
            continue
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet
        else:
            print("You can't bet that amount Sir! Try again")
            continue

def getDeck():
    #Generates all 52 cards
    deck = []
    for suit in (hearts, diamonds, spades, clubs):
        for rank in range(2,11):
            #Generates the numbered set
            deck.append((str(rank), suit))
        for rank in ('J','Q','K','A'):
            #Generates the face cards
            deck.append((rank,suit))
    random.shuffle(deck)
    return deck

def displayHands(playerHand, dealerHand, showDealerHand):
    print()
    if showDealerHand:
        print('Dealer: ', getHandValue(dealerHand))
        displayCards(dealerHand)
    else:
        print('Dealer: ???')
        displayCards([backside] + dealerHand[1:])

    print('Player: ', getHandValue(playerHand))
    displayCards(playerHand)


def getHandValue(cards):
    value = 0
    numberOfAces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            numberOfAces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += numberOfAces
    for i in range(numberOfAces):
        if value + 10 <= 21:
            value += 10
    return value

def displayCards(cards):
    rows = ['','','','','']
    for i, card in enumerate(cards):
        rows[0] += ' ___ '
        if card == backside:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card
            rows[1] += '|{} |'.format(rank.ljust(2))
            rows[2] += '| {} |'.format(suit)
            rows[3] += '|_{}|'.format(rank.rjust(2,'_'))

    for row in rows:
        print(row)

def getMove(playerHand, money):
    while True:
        moves = ['(H)it', '(S)tand']
        if len(playerHand) == 2 and money > 0:
            moves.append('(D)ouble down')
        movePrompt = ', '.join(moves) +'> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        elif move == 'D' and '(D)ouble down' in moves:
            return move
        else:
            print("Enter a valid move!")
main()
