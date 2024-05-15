from random import randint #generate random number. e.g beg,end=1,8 for i in range(8): print(random.randint(beg,end))

"""
X = x-axis
Y = y-axis
Gameboard will be 6 * 6 in size
"~" = water, space available to guess
“S" = players ship
"X" = Ship that was hit with bullet
“O" = Water that was shot with bullet, a miss because it hit no ship

"""

letter_to_number = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8} 
"""
convert column letters to numbers for grid/board. 
I started "A" at 1 because letter unlike numbers start at 1
Will need to chabge letters to numbers for column and user .upper() so if the player types lowercase it will be changed to upper 
"""

BOARD_SIZE_X = 6
BOARD_SIZE_Y = 6

#Cconstants to represent elements on the grid/board
NOT_GUESSED = "~" #guess board marks before shot in this position
SHIP = "S" # players ship
MISS_MARK = "O" # player misses, shown on computer board
HIT_MARK = "X" # if correct guess, Board updates with hit


print("Welcome to Battleships\n")


menu_request = ''
while menu_request == '':
    print("""
What would you like to do?
1. Read Instructions
2. Play Game
          """)
    user_in = input('What would you like: ').lower().strip()
    possible_answers = ['1', '2']
    if user_in in possible_answers:
        print(f'Thanks, you have chosen {user_in}!')
        menu_request = user_in
    else:
        print('No, you just need to input 1 or 2 - there are no other options')

if menu_request == "1":
    print("Battleships is a classic two-player game played on a grid.\nYou'll play against the computer, each having 5 ships. \nThe first to hit all 5 ships is the winner. \nYou will see 2 grids, first is your grid with ship placement and the second is the computers grid. \nThe computers grid won’t display their ship positions.\nHowever it will be mark with an “X” if you get a hit or “O” if it’s a miss.\nTake a shot by entering coordinates (e.g., A1, B5) on the grid. \nThe goal is to sink all of the opponent's ships before they sink yours.\n")
else:
    pass
    
user_name = input("What is your name: ")
print(f"Hello {user_name}, are you ready to play?\n")


def create_grid():
    """
    returns a grid that is 9x9 in size. using for loops to make 9 columns cells in 9 row lists
    """
    grid = [] #make a grid list
    for row in range(9):
        new_row = [] # make row of 9
        for col in range(9):# Loop through columns
            new_row.append(' ') # Add an empty space to each cell of the row
        grid.append(new_row) #.append/add the row to the grid
    return grid


def print_board(grid):
    """
    Takes the parameter of grid returned from create_grid()
    prints a header with letters, a frame top and bottom.
    prints rows numbered 0-8 and columns, seperated with a '|'. the '|' is a viual que of the cells

    """
    print("  A B C D E F G H I")
    print(" +-----------------+")
    for i in range(9): #loop though 9 times
        row = '' # sting that stores the content of each row
        for j in range(9): # nested loop for columns
            row += grid[i][j] # this appends/add the value of the cell eg A0
            if j < 8: # add '|' to inside columns only
                row += '|'
        print(i, row)
    print(" +-----------------+")

def place_ships(grid):
    """
    ship variable is = 2 lists. a tuple of size(3) or (2) and type. Each list is given a quantity *2 *3.
    in the for loop, a random direction is used with the function random.choice(), calling 'horizontal' or 'vertical'
    ships are placed in the grid area and only on empty spaces
    """
    ships = [(3, 'large')] * 2 + [(2, 'medium')] * 3
    for size, ship_type in ships:
        for s in range(100):  # Try up to 100 times to place the ship, without overlapping or going off grid
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                row = random.randint(0, 8)
                col = random.randint(0, 8 - size)
                if all(grid[row][col+j] == ' ' for j in range(size)): #checks if grid row and column coordinates are ' ' empty
                    for j in range(size):
                        grid[row][col+j] = ship_type[0].upper() 
                    break # breaks when the random ships are places
            else: #if direction vertical at random.choice(). do the same thing as 'horizontal' if statement and loop
                row = random.randint(0, 8 - size)
                col = random.randint(0, 8)
                if all(grid[row+i][col] == ' ' for i in range(size)):
                    for i in range(size):
                        grid[row+i][col] = ship_type[0].upper() #ship_type[0].upper() takes the first letter of the ship type and makes the letter uppercase
                    break





def see_hits(board):
    count = 0
    for row in board:
        for column in row:
            if column =="S":
                count += 1
    return count

