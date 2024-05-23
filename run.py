# Text style
from art import tprint
# generate random ship orientation and placement
import random
# for delay in printing new boards after results
import time
# Color to terminal
from colorama import Fore, Back, Style, init
init(autoreset=True)


# Constants to represent elements on the grid/board

BOARD_SIZE_X = 9
BOARD_SIZE_Y = 9
LETTERS = "ABCDEFGHI"
NUMBERS = "012345678"
# player misses, shown on player board
MISS_MRK = Fore.WHITE + Back.BLUE + 'O' + Style.RESET_ALL
# player hits, shown on players tracking board
HIT_MRK = Fore.WHITE + Back.RED + 'X' + Style.RESET_ALL
SHIPS = {"aircraft_carrier": 5,
         "battleship": 4,
         "destroyer": 3,
         "submarine": 2,
         "cruiser": 2}
TOTAL_AREA_OF_ALL_SHIPS = sum(SHIPS[item] for item in SHIPS)
# Colorama color and style
SRA = Style.RESET_ALL
BW = Back.WHITE
SN = Style.NORMAL
FW = Fore.WHITE
FB = Fore.BLACK
BR = Back.RED
BB = Back.BLUE
FR = Fore.RED


"""
SHIPS[item] retrieves the length of each ship (the value).
for item in SHIPS iterates over each ship type in the SHIPS dictionary.
sum() checks the total space the ships add up to
"""


def battleships_intro():
    """
    Intro to the game with 3 options
    """
    # large title text
    tprint("Battleships")
    print("Welcome to Battleships")
    menu_request = ''
    # menu_request will keep being displayed until 3 is selected
    while menu_request != '3':
        print("""
    What would you like to do?
    1. Read Instructions
    2. Game information
    3. Play Game
            """)
        user_in = input('What would you like: ').lower().strip()
        possible_answers = ['1', '2', '3']
        if user_in in possible_answers:
            print(f"Thanks, you have chosen {user_in}!")
            menu_request = user_in
            if menu_request == '1':
                print("""
            Battleships is a classic two-player game played on a grid.
            You'll play against the computer, each having 5 ships of
            varying sizes. The first to hit all 5 ships is the winner.
            You will see 2 grids, a tracking board and a ships position
            board. Both boards update with a 'X' for a hit and a 'O'
            for a miss. The tracking board shows if you hit the computer
            ship. The ship position board will show if the computer has
            hit or missed your ship. Take a shot by entering coordinates
            (e.g., A1, B5) on the grid. The goal is to sink all of the
            opponent's ships before they sink yours.
                """)
            elif menu_request == '2':
                print("""
            Battleship is a strategy type guessing game for two players.
            It is played on a grid on which each player's fleet of warships
            are marked. The locations of the fleets are concealed from the
            other player. Players alternate turns taking shots at coordinates
            (e.g. A1, B5) at the other player's ships, and the objective of
            the game is to destroy the opposing player's fleet.
                """)
        else:
            print(f"{FR}No, you just need to input 1, 2, or 3{SRA}")

    user_name = input("What is your name: \n").strip()
    # no or empty input gives invalid message
    while user_name == '':
        # .strip takes out the empty space
        user_name = input(f"{FR}Invalid!{SRA} What is your name: \n").strip()
    print(f"Hello {user_name}, are you ready to play?\n")
    return user_name


def create_grid():
    """
    List Comprehension, Returns a 9x9 grid with each cell
    initialized to an empty space.
    """
    return [[' ' for y in range(BOARD_SIZE_Y)] for x in range(BOARD_SIZE_X)]


def print_board(grid1, grid2):
    """
    Takes the parameter of grid1, grid2. It's called in main game
    and has arguments of player_shot, player_board
    prints a header with letters, a frame top and bottom.
    prints rows numbered 0-8 and columns, separated with
    a '|'. the '|' is a viual que of the cells

    """
    print("   Tracking Board      |       Ship position  ")
    print("  A B C D E F G H I          A B C D E F G H I")
    print(" +-----------------+       +-----------------+")
    for i in range(BOARD_SIZE_X):
        # for first board
        row1 = ''
        # for second board
        row2 = ''
        for j in range(BOARD_SIZE_Y):
            row1 += grid1[i][j]
            if j < 8:
                row1 += '|'
            row2 += grid2[i][j]
            if j < 8:
                row2 += '|'
        print(f"{i} {row1}       {i} {row2}")
    print(" +-----------------+       +-----------------+")
    print()


def place_ships(grid):
    """
    Places ships on the grid. To be called later for player_board and
    computer_board. SHIPS constant is a dictionary with ship types and
    their sizes. .items() gets the key (ship_type) and value (size).
    In the while loop, a random direction is used with the function
    random.choice(), calling 'horizontal' or 'vertical'.
    Ships are placed in the grid area and only on empty spaces.
    """
    for ship_type, size in SHIPS.items():
        placed = False
        while not placed:
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                # BOARD_SIZE_X is 9 so -1 as the board starts at 0, not 1
                row = random.randint(0, BOARD_SIZE_X - 1)
                col = random.randint(0, BOARD_SIZE_X - 1 - size)
                # Checks if grid row and column coordinates are ' ' (empty)
                if all(grid[row][col + j] == ' ' for j in range(size)):
                    for j in range(size):
                        # Color ship and first letter from name of ship
                        grid[row][col + j] = BW+SN + ship_type[0].upper()+SRA
                    # Successfully placed the ship
                    placed = True
            # If direction is vertical
            else:
                row = random.randint(0, BOARD_SIZE_Y - 1 - size)
                col = random.randint(0, BOARD_SIZE_Y - 1)
                if all(grid[row + i][col] == ' ' for i in range(size)):
                    for i in range(size):
                        # Color ship and first letter from name of ship
                        grid[row + i][col] = BW+SN + ship_type[0].upper()+SRA
                    # Successfully placed the ship
                    placed = True


def player_turn(computer_board, player_shot):
    """
    players chooses a row and column e.g A4
    Check to see if length is 2, first (0) is a letter, second(1) is a number
    from the constants LETTERS, NUMBERS
    letter has to be converted to a number for the position using ord()
    we - ord('A') as A is one on the grid but numbers start at 0
    we return the col letter and row number to the terminal and say
    if it hit or miss. inner else the cell is marked with X or O,
    you've fired at this position already.
    outer else input not in ==2 or not number or not letter.
    we only break (stop loop) when it's a hit of miss.
    """
    player_turn = True
    while player_turn:
        # print("Your turn:")
        target = input(f"Your turn. Enter target (e.g. A4):\n").upper().strip()
        if len(target) == 2 and target[0] in LETTERS and target[1] in NUMBERS:
            r = int(target[1])
            # ord() converts letters to numbers
            c = ord(target[0]) - ord('A')
            if player_shot[r][c] != HIT_MRK and player_shot[r][c] != MISS_MRK:
                if computer_board[r][c] != ' ':
                    print(f"{FW+BR}Hit, jolly good shot old chap!{SRA}\n")
                    # print what ship was hit
                    if computer_board[r][c] == BW+SN + "B" + SRA:
                        print(f"{FW+BR}Computer's Battleship hit!{SRA}\n")
                    elif computer_board[r][c] == BW+SN + "C" + SRA:
                        print(f"{FW+BR}Computer's Cruiser hit!{SRA}\n")
                    elif computer_board[r][c] == BW+SN + "A" + SRA:
                        print(f"{FW+BR}Comp's Aircraft Carrier hit!{SRA}\n")
                    elif computer_board[r][c] == BW+SN + "D" + SRA:
                        print(f"{FW+BR}Computer's Destroyer hit!{SRA}\n")
                    elif computer_board[r][c] == BW+SN + "S" + SRA:
                        print(f"{FW+BR}Computer's Submarine hit!{SRA}\n")
                    # HIT_MRK = red X
                    player_shot[r][c] = HIT_MRK
                    computer_board[r][c] = 'X'
                else:
                    print(f"{FW + BB}Miss, nothing but water!{SRA}\n")
                    # MISS_MRK = Blue O
                    player_shot[r][c] = MISS_MRK
                # loop only breaks when it's a hit or miss(X or O)
                break
            else:
                print(f"{BW}{FB}You've already fired at this location.")
        else:
            print(f"{Fore.RED}Invalid input. Please enter a valid target.")


def computer_turn(player_board, computer_shot):
    """
    computer chooses a random number for row and random letter for column.
    like players_turn, the letter has to be converted to a number for the
    position using ord(). we return the col letter and row number to the
    terminal and say if it hit or miss
    """
    computer_turn = True
    while computer_turn:
        # r is a row
        # BOARD_SIZE_X constant is 9, we -1 as the row starts at 0
        r = random.randint(0, (BOARD_SIZE_X - 1))
        # r_c = random choice of the letters in constant LETTERS
        r_c = LETTERS[random.randint(0, BOARD_SIZE_X - 1)]
        # ord() converts letters to numbers
        # c is col
        c = ord(r_c) - ord('A')
        # checks if the cell is marked with an X for hit or O for miss
        if computer_shot[r][c] != 'X' and computer_shot[r][c] != 'O':
            # player_board position has to be ' ' otherwise it's a hit
            if player_board[r][c] != ' ':
                # strings e.g "A""2"
                print(f"{FW + BR}Computer hit at {str(r_c)}{str(r)}{BR}")
                # print what ship was hit
                if player_board[r][c] == BW+SN + "B" + SRA:
                    print(f"{FW+BR}Your Battleship is hit!{SRA}")
                elif player_board[r][c] == BW+SN + "C" + SRA:
                    print(f"{FW+BR}Your Cruiser is hit!{SRA}")
                elif player_board[r][c] == BW+SN + "A" + SRA:
                    print(f"{FW+BR}Your Aircraft Carrier hit!{SRA}")
                elif player_board[r][c] == BW+SN + "D" + SRA:
                    print(f"{FW+BR}Your Destroyer is hit!{SRA}")
                elif player_board[r][c] == BW+SN + "S" + SRA:
                    print(f"{FW+BR}Your Submarine is hit!{SRA}")
                # update computer tracking board with X
                computer_shot[r][c] = 'X'
                # update player board with a red background X
                player_board[r][c] = HIT_MRK
                return
            else:
                # else ' ' (empty)
                print(f"{FW + BB}Computer missed at {str(r_c)}{str(r)}{BR}")
                # update computer tracking board with a 'O'
                computer_shot[r][c] = 'O'
                # update player board with a blue background 'O'
                player_board[r][c] = MISS_MRK
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
            # "X" represents a sunk ship
            if cell == "X":
                score += 1
    # the for loop sum() that checks the total space the ships add up too
    if score == TOTAL_AREA_OF_ALL_SHIPS:
        # All ships are sunk
        return True
    else:
        # Game is not over yet
        return False


def main():
    """
    This is the main game run function. It calls for 4 boards.
    2 for the player and 2 for the computer.
    player_board has the players ships placed on it.
    computer_board has the computer ships placed on it
    player_shot has the positions of where they
    have fired. same with computer_shot
    It prints 2 board to the terminal.
    First, Player board with ship positions and second,
    players tracking board that shows hits or missed
    """

    user_name = battleships_intro()

    while True:
        player_board = create_grid()
        computer_board = create_grid()
        player_shot = create_grid()
        computer_shot = create_grid()

        print("Placing ships...")
        # ships are placed in the player_board
        place_ships(player_board)
        # ships are placed in the player_board
        place_ships(computer_board)

        play_game = True
        while play_game:
            print("\nPlayer's Board:")
            print_board(player_shot, player_board)
            # computer_board and player_shot are arguments.
            # check 'X', 'O' or ' ' & instructions on what to do
            player_turn(computer_board, player_shot)
            if check_game_over(computer_board):
                print(f"{user_name}, You win!")
                break
            time.sleep(1)
            computer_turn(player_board, computer_shot)
            # player_board is an argument,
            # check score == TOTAL_AREA_OF_ALL_SHIPS
            # player_board is the one with players ship positions
            # if they're all hit, the computer wins
            if check_game_over(player_board):
                print(f"{user_name}, You lose!")
                break

        play_again = input("Play again? (Y/N): ").strip().upper()
        # If input is not Y, game is over
        if play_again != 'Y':
            print("Thanks for playing Battleships!")
            break


if __name__ == "__main__":
    main()
    """
    main is called directly
    """
