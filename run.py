import gspread
from google.oauth2.service_account import Credentials
import random #generate random ship orientation and placement
import time #for delay in printing new boards after results

#Constants to represent elements on the grid/board
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Battleships-project3')
leaderboard = SHEET.worksheet('leaderboard')

data = leaderboard.get_all_values()
#print(data)

BOARD_SIZE_X = 9
BOARD_SIZE_Y = 9
LETTERS = "ABCDEFGHI"
NUMBERS = "012345678"

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
    user_in = input('What would you like: \n').lower().strip()
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
    
user_name = input("What is your name: \n")
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
    for i in range(BOARD_SIZE_X): #loop though 9 times
        row = '' # sting that stores the content of each row
        for j in range(BOARD_SIZE_Y): # nested loop for columns
            row += grid[i][j] # this appends/add the value of the cell eg A0
            if j < 8: # add '|' to inside columns only. only the first 8 cells
                row += '|'
        print(i, row)
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
        target = input("Enter target (e.g., A4): \n").upper()
        if len(target) == 2 and target[0] in LETTERS and target[1] in NUMBERS:
            row = int(target[1])
            col = ord(target[0]) - ord('A') #ord() converts letters to numbers
            if player_tracking_board[row][col] != 'X' and player_tracking_board[row][col] != 'O':
                if computer_board[row][col] != ' ':
                    print("Hit, jolly good shot old chap!")
                    player_tracking_board[row][col] = 'X'
                    computer_board[row][col] = 'X'
                else:
                    print("Miss, nothing but water!")
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
            if player_board[row][col] != ' ': #player_board position has to be ' ' otherwise it's a hit every time.
                print("Computer hit at", str(random_col) + str(row)) # strings e.g "A""2"
                computer_tracking_board[row][col] = 'X' #update computer tracking board with X
                player_board[row][col] = 'X' #update player board with X
                return 
            else:
                print("Computer missed at", str(random_col) + str(row)) # else if ' ' 
                computer_tracking_board[row][col] = 'O' #update computer tracking board with a 'O'
                player_board[row][col] = 'O' #update player board with 'O'
            break
    print("Player's ship positions:")
    print_board(player_board)
 

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

def main():
    """
    This is the main game run function. It calls for 4 boards. 2 for the player and 2 for the computer.
    player_board has the players ships placed on it.
    computer_board has the computer ships placed on it
    player_tracking_board has the positions of where they have fired. same with computer_tracking_board
    It prints 2 board to the terminal. 
    First, Player board with ship positions and second, players tracking board that shows hits or missed
    """
        
    player_board = create_grid()
    computer_board = create_grid()
    player_tracking_board = create_grid()
    computer_tracking_board = create_grid()

    print("Placing ships...")
    place_ships(player_board) #ships are placed in the player_board
    place_ships(computer_board) #ships are placed in the player_board

    print("Player's ship positions:")
    print_board(player_board) #player_board is printed to terminal

    play_game = True #game plays 
    while play_game:
        print("\nPlayer's Tracking Board:")
        print_board(player_tracking_board)
        player_turn(computer_board, player_tracking_board) #computer_board and player_tracking_board are arguments so see if the boards have an 'X', 'O' or ' ' and instructions on what to do
        if check_game_over(computer_board): #computer_board is an argument to see if score == TOTAL_AREA_OF_ALL_SHIPS
            print(f"{user_name}, You win!")
            break
        time.sleep(1.5)
        #print("\nPlayer's ship positions:")
        #print_board(player_board)
        computer_turn(player_board, computer_tracking_board)
        if check_game_over(player_board): #player_board is an argument to see if score == TOTAL_AREA_OF_ALL_SHIPS. player_board is the one with players ship positions, so if they're all hit, the computer wins
            print(f"Better Luck next time {user_name}, Computer wins!")
            break

if __name__ == "__main__": 
    main() #main is called directly