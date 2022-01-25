# Calculates how many times a certain streak was completed when flipping coins, prints a complete table of the coin flips
import random
print("How many coin flips?")
try:
    numberFlips = int(input())
except ValueError:
    print("Try a number next time!")
print("What streak are you looking for?")
try:
    streakNum = int(input())
except ValueError:
    print("Try a number next time!")
flips = []
previousFlip = ''
currentStreak = 0
streakTotal = 0

for x in range(1,numberFlips):
    if random.randint(0,1) == 0:
        flip = 'H'
    else:
        flip = 'T'

    if flip == previousFlip:
        if currentStreak >= streakNum:
            streakTotal += 1
            currentStreak = 0
        currentStreak += 1
    else:
        if currentStreak >= streakNum:
            streakTotal += 1
        currentStreak = 0


    flips.append(flip)
    previousFlip = flip


print(flips)
print("We got "+str(streakNum)+" in a row "+str(streakTotal)+ " times!")
