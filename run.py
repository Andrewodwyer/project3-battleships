from random import randint #generate random number. e.g beg,end=1,8 for i in range(8): print(random.randint(beg,end))

"""
X = x-axis
Y = y-axis
"_" is the gameboard marking/spaces
Gameboard will be 8 * 8 in size
"." = water, space available to guess
“@" = players ship
"X" = Ship that was hit with bullet
“O" = Water that was shot with bullet, a miss because it hit no ship

Will need to chabge letters to numbers for column and user .upper() so if the player types lowercase it will be changed to upper 
Dictionary {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7}
"""
"""

rows = 8
columns = ["A", "B", "C", "D", "E", "F", "G", "H"]

#grid = gameboard(rows, columns)

#display top row
for i in range(rows):
    row = [str(i)] 
    for col in columns:
        row.append("_") # "_" is display spaces on grid
    grid.append(row)
    print(i, col)

rows = 8
columns = ["A", "B", "C", "D", "E", "F", "G", "H"]

grid = gameboard(rows, columns)
"""

"""
I want to refer to columns by letter not number.
I'm using a dictionary to get the letter from the numbers. Python numbers start with 0 so "A" is 0 and so on
"""
"""

grid = []

for i in range(0,8): 
    # start at 0 and finsh at 8
    grid.append("_"*8)

def print_board(grid):
    print("  A B C D E F G H")
    for row in grid:
        print(i," ".join(row))

print_board(grid)



"""


"""
letter_to_number = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}

def print_board():
    print("   A B C D E F G H")
    print("   _______________")
    row_number = 1
    for row in board:
        print("%d|%s|"(row_number, "|".join(row)))
        row_number +=1
print_board()

"""

def intro():
    print("Battleships\n")
    print("Would you like to see the rules Y/N")
    Yes = input().lower()
    if Yes == "y":
        print("Battleships is a classic two-player game played on a grid.\nYou'll play against the computer, each having 5 ships. \nThe first to hit all 5 ships is the winner. \nYou will see 2 grids, first is your grid with ship placement and the second is the computers grid. \nThe computers grid won’t display their ship positions.\nHowever it will be mark with an “X” if you get a hit or “O” if it’s a miss.\nTake a shot by entering coordinates (e.g., A1, B5) on the grid. \nThe goal is to sink all of the opponent's ships before they sink yours.\n")
    else:
        pass    
    print("What is your name?")
    username = input()
    print(f"Hi {username} are you ready to play?")

intro()

def create_grid():
    row = 0
    alphabet_index = 0
    alphabet = "ABCDEFGH"
    
    # Print column labels
    print("   " + " ".join(alphabet))
    
    while row <= 8:
        # Print row number
        print(row, end="  ")
        
        # Print cells in the row
        col = 0
        while col < len(alphabet):
            print(" ", end="")
            print("_", end="")  # Change "X" to whatever you want to represent each cell
            col += 1
        
        print()  # Move to the next line after printing a row
        row += 1

create_grid()

"""

def random_row(grid):
    return randint(0,len(grid)-1)

    #reason -1 because len() doesn't start at 0, it starts at one. we need to pair it up with the list starting at 0

def random_col(grid):
    return randint(0,len(grid)-1)
    
ship_row = random_row(grid)
ship_col = random_col(grid)
"""

print("Choose a row: eg. 1,2,3")
row_choice = int(input())

print("Choose a column: eg. A,B,C")
column_choice = str(input().upper()) #.upper makes the input uppercase