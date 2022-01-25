# simple game of life simulation that is depicted in the terminal
import random, time, copy
width = 40
height = 10
nextCells = []
for x in range(width):
    collumn = []
    for y in range(height):
        if random.randint(0,1) == 0:
            collumn.append(' ') #Dead Cell
        else:
            collumn.append('O') #Alive Cell
    nextCells.append(collumn)
while True:
    print ('\n\n\n\n\n\n\n\n\n\n')
    print('----------------------------------------')
    currentCells = copy.deepcopy(nextCells)
    for y in range(height):
        for x in range(width):
            print(currentCells[x][y], end = '')
        print()
    for x in range(width):
        for y in range(height):
            leftCord = (x-1) % width #Doing this ensures it stays within bounds of the board
            rightCord = (x+1) % width
            aboveCord = (y-1) % height
            belowCord = (y+1) % height
            numNeighbours = 0
            #Check each neighbour cell if alive
            if currentCells[leftCord][aboveCord] == 'O':
                numNeighbours += 1
            if currentCells[x][aboveCord] == 'O':
                numNeighbours += 1
            if currentCells[rightCord][aboveCord] == 'O':
                numNeighbours += 1
            if currentCells[leftCord][y] == 'O':
                numNeighbours += 1
            if currentCells[rightCord][y] == 'O':
                numNeighbours += 1
            if currentCells[leftCord][belowCord] == 'O':
                numNeighbours += 1
            if currentCells[x][belowCord] == 'O':
                numNeighbours += 1
            if currentCells[rightCord][belowCord] == 'O':
                numNeighbours += 1
            if currentCells[x][y] == 'O' and (numNeighbours == 2 or numNeighbours == 3):
                nextCells[x][y] = 'O'
            elif currentCells[x][y] == ' ' and numNeighbours == 3:
                nextCells[x][y] = 'O'
            else:
                nextCells[x][y] = ' '
    time.sleep(0.2)
