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
    Creates the game grid/board, ABCDEF for columns and 0-6 for rows
    """
    row = 0
    abc_header_index = 0
    abc_header = "ABCDEF" 
    
    # Print column labels
    print("    " + " ".join(abc_header)) #first "" is space from the start, second "" is space between letters
    print("  +-------------+")
    
    while row <= 5: # Print row number
        print(row, end=" |") #end=" " end is saying it'd finished and the next element does not need to go on a new line.
        
        # Print cells in the row
        col = 0
        while col < len(abc_header):
            print(" ", end="")
            print("~", end="")  # "~" represents each position a ship could be in.
            col += 1
        
        print(" |")  # Move to the next line after printing a row
        row += 1 #added a row and moves on until the row is less than or equal to 5, while loop
    print("  +-------------+")

create_grid()

def create_ships():
    """
    Place ship on the grid. There will be 5 ships on the board. Each ship will be in a row and column co-ordinates. 
    The function places the row and column at random and makes it = "S". 
    The nested while loop checks if any of the 5 random selections are equal to already created placement and if it is
    it will run it again until all 5 ships are in different places
    """
    for ship in range(5): # 5 ships to place on board
        ship_row, ship_column = randint(0,5), randint(0,5) #ship row is random, ship column is random, taken from random import randint
        while board[ship_row][ship_column] == 'S': #check if ship row or ship column is equal to "S" and if it is, random generate again
            ship_row, ship_column = randint(0,5), randint(0,5)
        board[ship_row][ship_column] = "S" #Ships are now on the board


row = ""
while row == "":
    row_number_input = input("Please enter a row guess, number between 0 and 5: ").strip()
    row_number_options = ["0", "1", "2", "3", "4", "5" ]
    if row_number_input in row_number_options : #set parameters between "0" to "5"
        row = row_number_input
    else:
        print(f"'{row_number_input}' is not a number between 0 and 5.")

print("You chose row:", row)

column = ""
while column == "":
    column_letter_input = input("Please enter a column guess, letter between 'A' and 'F': ").upper().strip() #.upper makes the input uppercase
    column_number_options = ["A", "B", "C", "D", "E", "F" ] 
    if column_letter_input in column_number_options : #set parameters between "A" to "F"
        column = column_letter_input
    else:
        print(f"'{column_letter_input}' is not a letter between 'A' and 'F'.")

print("You chose column:", column)


def see_ship_coordinates():
    return int(row), letter_to_number[column] #dictionary that has key:values
    print(int(row), letter_to_number[column])

ships_coordinates = see_ship_coordinates()
print(ships_coordinates)



def see_hits(board):
    count = 0
    for row in board:
        for column in row:
            if column =="S":
                count += 1
    return count

