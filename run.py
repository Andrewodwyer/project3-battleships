from random import randint #generate random ship orientation and placement

"""
X = x-axis
Y = y-axis
Gameboard will be 6 * 6 in size
"~" = water, space available to guess
“S" = players ship
"X" = Ship that was hit with bullet
“O" = Water that was shot with bullet, a miss because it hit no ship


letter_to_number = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8} 

convert column letters to numbers for grid/board. 
I started "A" at 1 because letter unlike numbers start at 1
Will need to chabge letters to numbers for column and user .upper() so if the player types lowercase it will be changed to upper 
"""

#Constants to represent elements on the grid/board
BOARD_SIZE_X = 9
BOARD_SIZE_Y = 9

MISS_MARK = "O" # player misses, shown on computer board
HIT_MARK = "X" # if correct guess, Board updates with hit
SHIPS = {"aircraft_carrier":5, "battleship":4, "destroyer":3, "submarine":2, "cruiser":2}
TOTAL_AREA_OF_ALL_SHIPS = sum(SHIPS[item] for item in SHIPS) 
"""
SHIPS[item] retrieves the length of each ship (the value).
for item in SHIPS iterates over each ship type in the SHIPS dictionary.
sum() checks the total space the ships add up to
"""



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
    for row in range(BOARD_SIZE_X):
        new_row = [] # make row of 9
        for col in range(BOARD_SIZE_Y):# Loop through columns
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
    for i in range(): #loop though 9 times
        row = '' # sting that stores the content of each row
        for j in range(BOARD_SIZE_X): # nested loop for columns
            row += grid[i][j] # this appends/add the value of the cell eg A0
            if j < (BOARD_SIZE_X -1): # add '|' to inside columns only. only the first 8 cells
                row += '|'
        print(i, row,)
    print(" +-----------------+")

def place_ships(grid):
    """
    places ships on the grid. To be called later for player_board and computer_board
    SHIPS constant is =  a dictionary with ship types and their sizes. .items() gets the key.value and assigns them to ship_type (key), size(value)
    in the for loop, a random direction is used with the function random.choice(), calling 'horizontal' or 'vertical'
    ships are placed in the grid area and only on empty spaces
    """
    for ship_type, size in SHIPS.items():
        for s in range(100):  # Try up to 100 times to place the ship, without overlapping or going off grid
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                row = random.randint(0, (BOARD_SIZE_X -1)) #BOARD_SIZE_X is 9 so I've -1 as the boards starts at 0 not 1
                col = random.randint(0, (BOARD_SIZE_X -1) - size)
                if all(grid[row][col+j] == ' ' for j in range(size)): #checks if grid row and column coordinates are ' ' empty
                    for j in range(size):
                        grid[row][col+j] = ship_type[0].upper() 
                    break # breaks when the random ships are places
            else: #if direction vertical at random.choice(). do the same thing as 'horizontal' if statement and loop
                row = random.randint(0, (BOARD_SIZE_Y -1) - size) 
                col = random.randint(0, (BOARD_SIZE_Y -1))
                if all(grid[row+i][col] == ' ' for i in range(size)):
                    for i in range(size):
                        grid[row+i][col] = ship_type[0].upper() #ship_type[0].upper() takes the first letter of the ship type and makes the letter uppercase
                    break

def player_turn(computer_board, player_tracking_board):
    """
    players chooses a row and column e.g A4
    Check to see if length is 2, first (0) is a letter, second(1) is a number
    from the constants LETTERS, NUMBERS
    letter has to be converted to a number for the position using ord()
    we - ord('A') as A is one on the grid but numbers start at 0
    we return the col letter and row number to the terminal and say if it hit or miss
    inner else the cell is marked with X or O, you've fired at this position already
    outer else input not in ==2 or not number or not letter.
    we only break (stop loop) when it's a hit of miss.
    """
    player_turn = True
    while player_turn:
        print("Your turn:")
        target = input("Enter target (e.g., A4): ").upper()
        if len(target) == 2 and target[0] in LETTERS and target[1] in NUMBERS:
            row = int(target[1])
            col = ord(target[0]) - ord('A') #ord() converts letters to numbers
            if player_tracking_board[row][col] != 'X' and player_tracking_board[row][col] != 'O':
                if computer_board[row][col] != ' ':
                    print("Hit!")
                    player_tracking_board[row][col] = 'X'
                    computer_board[row][col] = 'X'
                else:
                    print("Miss!")
                    player_tracking_board[row][col] = 'O'
                break #loop only breaks when it's a hit or miss (conditions for X or O)
            else:
                print("You've already fired at this location.")
        else:
            print("Invalid input. Please enter a valid target.")

def computer_turn(player_board, computer_tracking_board):
    """
    computer chooses a random number for row and random letter for column.
    like players_turn, the letter has to be converted to a number for the position using ord()
    we return the col letter and row number to the terminal and say if it hit or miss
    """
    computer_turn = True
    while computer_turn:
        row = random.randint(0, (BOARD_SIZE_X -1)) #BOARD_SIZE_X constant is 9, we -1 as the row starts at 0
        random_col = LETTERS[random.randint(0, BOARD_SIZE_X -1)] #random choice of the letters in constant LETTERS
        col = ord(random_col) - ord('A') #ord() converts letters to numbers
        if computer_tracking_board[row][col] != 'X' and computer_tracking_board[row][col] != 'O': #checks if the cell is marked with an X for hit or O for miss
            print("Computer hit at", str(random_col) + str(row)) # strings e.g "A""2"
            computer_tracking_board[row][col] = 'X' #update computer tracking board with X
            player_board[row][col] = 'X' #update player board with X
        else:
            print("Computer missed at", str(random_col) + str(row)) # else if ' ' 
            computer_tracking_board[row][col] = 'O' #update computer tracking board with a 'O'
            player_board[row][col] = 'O' #update player board with 'O'
        break
 

def check_game_over(grid):
    """
    checks the number of hits. If number of hits is == to the
    number of cells the ships take up. The if statement returns true.
    the game ends
    """
    score = 0
    for row in grid:
        for cell in row:
            if cell == "X":  # "X" represents a sunk ship
                score += 1
    if score == TOTAL_AREA_OF_ALL_SHIPS: #the for loop sum() that checks the total space the ships add up to
        return True  # All ships are sunk
    else:
        return False  # Game is not over yet

