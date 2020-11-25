import random

class Grid:
    def __init__(self, cols, rows, char1 = 1, char2 = 0):
        self.char1 = char1
        self.char2 = char2
        self.cols = cols
        self.rows = rows
        self.lst = []
        self.randomPositionY = random.randrange(0, self.rows)
        self.randomPositionX = random.randrange(0, self.cols)
        self.takenCoords = []

    def mineLevelGen(self):
        for row in range(self.rows):
            self.lst.append([])
        for row in self.lst:
            for _ in range(self.cols):
                if self.lst.index(row) == 0:
                    row.append(self.char2)
                else:
                    row.append(self.char1)

    def createGrid(self):
        for row in range(self.rows):
            self.lst.append([])
        for row in self.lst:
            for _ in range(self.cols):
                row.append(self.char1)
    
    def printGrid(self):
        # Print grid
        for row in self.lst:
            print(row)

    def spawnPlayer(self):
        self.lst[self.randomPositionY][self.randomPositionX] = self.char2

        # Print grid
        self.printGrid()

    def placeOre(self, symbol, items):
        # Do for number of items to spawn
        for _ in range(items):
            # Get a random spawn position
            spawnPosition = (random.randrange(0, self.cols), random.randrange(0, self.rows))

            # Prevent spawning on top row
            if spawnPosition[0] == 0:
                # Add coords to do not spawn list
                self.takenCoords.append(spawnPosition)

            # Check that coords are not in the do not spawn list
            if spawnPosition not in self.takenCoords:
                # Spawn character in grid
                self.lst[spawnPosition[0]][spawnPosition[1]] = symbol
                # Add coords to do not spawn list
                self.takenCoords.append(spawnPosition)

            # Check if coords are in the do not spawn list
            else:

                # Keep spawning new coords until they meet the requirements
                while spawnPosition in self.takenCoords or spawnPosition[0] == 0:
                    # Get random coords
                    spawnPosition = (random.randrange(0, self.cols), random.randrange(0, self.rows))

                # Spawn character in grid
                self.lst[spawnPosition[0]][spawnPosition[1]] = symbol
                # Add coords to do not spawn list
                self.takenCoords.append(spawnPosition)
        

def gameLoop(grid):
    # Get direction from user
    direction = input('Enter direction (u,d,l,r): ')

    if direction == 'u':

        # Check if player can move up
        if grid.randomPositionY <= 0:
            print("Can't move up, try another direction..")
        else:
            # Overwrite old position
            grid.lst[grid.randomPositionY][grid.randomPositionX] = grid.char1
            # Move player position up by 1
            grid.randomPositionY -= 1
            # update player position
            grid.lst[grid.randomPositionY][grid.randomPositionX] = grid.char2

        # Print grid
        for row in grid.lst:
            print(row)

    elif direction == 'd':

         # Check if player can move down
        if grid.randomPositionY >= grid.rows-1:
            print("Can't move down, try another direction..")
        else:
            # Overwrite old position
            grid.lst[grid.randomPositionY][grid.randomPositionX] = grid.char1
            # Move player position up by 1
            grid.randomPositionY += 1
            # update player position
            grid.lst[grid.randomPositionY][grid.randomPositionX] = grid.char2

        # Print grid
        for row in grid.lst:
            print(row)

    elif direction == 'l':

        # Check if player can move left
        if grid.randomPositionX <= 0:
            print("Can't move left, try another direction..")
        else:
            # Overwrite old position
            grid.lst[grid.randomPositionY][grid.randomPositionX] = grid.char1
            # Move player position up by 1
            grid.randomPositionX -= 1
            # update player position
            grid.lst[grid.randomPositionY][grid.randomPositionX] = grid.char2

        # Print grid
        for row in grid.lst:
            print(row)
    
    elif direction == 'r':

        # Check if player can move right
        if grid.randomPositionX >= grid.cols-1:
            print("Can't move right, try another direction..")
        else:
            # Overwrite old position
            grid.lst[grid.randomPositionY][grid.randomPositionX] = grid.char1
            # Move player position up by 1
            grid.randomPositionX += 1
            # update player position
            grid.lst[grid.randomPositionY][grid.randomPositionX] = grid.char2

        # Print grid
        for row in grid.lst:
            print(row)

    else:
        print('Wrong character entered. Please try again')

def dungeonCreator(grid):
    # Find lowest value (cols or rows)
    if grid.cols > grid.rows:
        maxLen = grid.rows
    else:
        maxLen = grid.cols

    directions = ['u','d','l','r']
    direction = random.choice(directions)
    
    # Define current line len
    line = 0
    while True:
        lineLen = random.randrange(0, maxLen)
        if direction == 'u':
            # Check if player can move up
            if grid.randomPositionY <= 0 or line >= lineLen:
                # Reset current line length
                line = 0
                # Change direction
                direction = random.choice(directions)
                print("Can't move up, try another direction..")
            else:
                # Increase current line length
                line += 1
                # Move player position up by 1
                grid.randomPositionY -= 1
                # update player position
                grid.lst[grid.randomPositionY][grid.randomPositionX] = grid.char2

            # Print grid
            print('\n')
            for row in grid.lst:
                print(row)

        elif direction == 'd':
            # Check if player can move down
            if grid.randomPositionY >= grid.rows-1 or line >= lineLen:
                # Reset current line length
                line = 0
                # Change direction
                direction = random.choice(directions)
                print("Can't move down, try another direction..")
            else:
                # Increase current line length
                line += 1
                # Move player position up by 1
                grid.randomPositionY += 1
                # update player position
                grid.lst[grid.randomPositionY][grid.randomPositionX] = grid.char2

            # Print grid
            print('\n')
            for row in grid.lst:
                print(row)

        elif direction == 'l':
            # Check if player can move left
            if grid.randomPositionX <= 0 or line >= lineLen:
                # Reset current line length
                line = 0
                # Change direction
                direction = random.choice(directions)
                print("Can't move left, try another direction..")
            else:
                # Increase current line length
                line += 1
                # Move player position up by 1
                grid.randomPositionX -= 1
                # update player position
                grid.lst[grid.randomPositionY][grid.randomPositionX] = grid.char2

            # Print grid
            print('\n')
            for row in grid.lst:
                print(row)

        else:
            # Check if player can move right
            if grid.randomPositionX >= grid.cols-1 or line >= lineLen:
                # Reset current line length
                line = 0
                # Change direction
                direction = random.choice(directions)
                print("Can't move right, try another direction..")
            else:
                # Increase current line length
                line += 1
                # Move player position up by 1
                grid.randomPositionX += 1
                # update player position
                grid.lst[grid.randomPositionY][grid.randomPositionX] = grid.char2

            # Print grid
            print('\n')
            for row in grid.lst:
                print(row)


grid = Grid(32, 32, '█', '░')
grid.mineLevelGen()
grid.placeOre('#', 22)
# grid.placeOre('*', 12)
# grid.placeOre('^', 12)
# grid.placeOre('$', 12)
grid.printGrid()
# grid.spawnPlayer()
print(grid.takenCoords)
# dungeonCreator(grid)

# while True:
#     pass
    # gameLoop(grid)