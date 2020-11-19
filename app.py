import random

class Grid:
    def __init__(self, cols, rows, char1 = 1, char2 = 0):
        self.char1 = char1
        self.char2 = char2
        self.cols = cols
        self.rows = rows
        self.lst = []
        self.playerPositionY = random.randrange(0, self.rows)
        self.playerPositionX = random.randrange(0, self.cols)

    def printGrid(self):
        for row in range(self.rows):
            self.lst.append([])
        for row in self.lst:
            for _ in range(self.cols):
                row.append(self.char1)

    def spawnPlayer(self):
        self.lst[self.playerPositionY][self.playerPositionX] = self.char2

        # Print grid
        for row in self.lst:
            print(row)

def gameLoop(grid):
    # Get direction from user
    direction = input('Enter direction (u,d,l,r): ')

    if direction == 'u':

        # Check if player can move up
        if grid.playerPositionY <= 0:
            print("Can't move up, try another direction..")
        else:
            # Overwrite old position
            grid.lst[grid.playerPositionY][grid.playerPositionX] = grid.char1
            # Move player position up by 1
            grid.playerPositionY -= 1
            # update player position
            grid.lst[grid.playerPositionY][grid.playerPositionX] = grid.char2

        # Print grid
        for row in grid.lst:
            print(row)

    elif direction == 'd':

         # Check if player can move down
        if grid.playerPositionY >= grid.rows-1:
            print("Can't move down, try another direction..")
        else:
            # Overwrite old position
            grid.lst[grid.playerPositionY][grid.playerPositionX] = grid.char1
            # Move player position up by 1
            grid.playerPositionY += 1
            # update player position
            grid.lst[grid.playerPositionY][grid.playerPositionX] = grid.char2

        # Print grid
        for row in grid.lst:
            print(row)

    elif direction == 'l':

        # Check if player can move left
        if grid.playerPositionX <= 0:
            print("Can't move left, try another direction..")
        else:
            # Overwrite old position
            grid.lst[grid.playerPositionY][grid.playerPositionX] = grid.char1
            # Move player position up by 1
            grid.playerPositionX -= 1
            # update player position
            grid.lst[grid.playerPositionY][grid.playerPositionX] = grid.char2

        # Print grid
        for row in grid.lst:
            print(row)
    
    elif direction == 'r':

        # Check if player can move right
        if grid.playerPositionX >= grid.cols-1:
            print("Can't move right, try another direction..")
        else:
            # Overwrite old position
            grid.lst[grid.playerPositionY][grid.playerPositionX] = grid.char1
            # Move player position up by 1
            grid.playerPositionX += 1
            # update player position
            grid.lst[grid.playerPositionY][grid.playerPositionX] = grid.char2

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
            if grid.playerPositionY <= 0 or line >= lineLen:
                # Reset current line length
                line = 0
                # Change direction
                direction = random.choice(directions)
                print("Can't move up, try another direction..")
            else:
                # Increase current line length
                line += 1
                # Move player position up by 1
                grid.playerPositionY -= 1
                # update player position
                grid.lst[grid.playerPositionY][grid.playerPositionX] = grid.char2

            # Print grid
            print('\n')
            for row in grid.lst:
                print(row)

        elif direction == 'd':
            # Check if player can move down
            if grid.playerPositionY >= grid.rows-1 or line >= lineLen:
                # Reset current line length
                line = 0
                # Change direction
                direction = random.choice(directions)
                print("Can't move down, try another direction..")
            else:
                # Increase current line length
                line += 1
                # Move player position up by 1
                grid.playerPositionY += 1
                # update player position
                grid.lst[grid.playerPositionY][grid.playerPositionX] = grid.char2

            # Print grid
            print('\n')
            for row in grid.lst:
                print(row)

        elif direction == 'l':
            # Check if player can move left
            if grid.playerPositionX <= 0 or line >= lineLen:
                # Reset current line length
                line = 0
                # Change direction
                direction = random.choice(directions)
                print("Can't move left, try another direction..")
            else:
                # Increase current line length
                line += 1
                # Move player position up by 1
                grid.playerPositionX -= 1
                # update player position
                grid.lst[grid.playerPositionY][grid.playerPositionX] = grid.char2

            # Print grid
            print('\n')
            for row in grid.lst:
                print(row)

        else:
            # Check if player can move right
            if grid.playerPositionX >= grid.cols-1 or line >= lineLen:
                # Reset current line length
                line = 0
                # Change direction
                direction = random.choice(directions)
                print("Can't move right, try another direction..")
            else:
                # Increase current line length
                line += 1
                # Move player position up by 1
                grid.playerPositionX += 1
                # update player position
                grid.lst[grid.playerPositionY][grid.playerPositionX] = grid.char2

            # Print grid
            print('\n')
            for row in grid.lst:
                print(row)


grid = Grid(32, 32, '█', '░')
grid.printGrid()
grid.spawnPlayer()

dungeonCreator(grid)

while True:
    pass
    # gameLoop(grid)