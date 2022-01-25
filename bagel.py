
import random, sys, os
answer = str(random.randint(100,999))
guessing = True
print("This is a number guessing game! If a number is in the correct position I will return 'Hit' and if a number is in the sequence but not in the correct position I will return 'Nearly!'. Your guess must be 3 numbers")

def checkGuess(guess):
    if guess == answer:
        print("Correct!")
        guessing = False
        exit()

    hint = []
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            hint.append('Hit')
        elif guess[i] in answer:
            hint.append('Nearly')
    if len(hint) == 0:
        return 'Nada!'
    else:
        hint.sort()
        return ' '.join(hint)

def randomNum():
    print('in here')
    answer = str(random.randint(100,999))

while guessing:
    playerGuess = input('>')
    if len(playerGuess) != 3:
        print("You must guess a three digit number like 123!")
    response = checkGuess(playerGuess)
    print(response)

