# Battleships

Battleships is a classic two-player game. You will play the computer, each having 5 ships of varying sizes. The first to hit all 5 ships is the winner. 
This version is a terminal based game. You'll view 2 grids, a tracking board to see where you have fired and a ship position grid for your ships.


## Live Game

The live game can be seen here:
https://battleship-project3-a-133f293668e9.herokuapp.com/

## Project Goal

- I wanted to design a terminal based battleships game that followed the same format as the original. 

## Research

I got the information on the game from https://en.wikipedia.org/wiki/Battleship_(game) and https://battleship.fandom.com/wiki/Battleship_(game)
Using this research I wrote instructions on how to play my game and information on the concept of the game.
This information was used in the intro to the game. Read Instructions is option one and Game Information is option 2.

- 1. Read Instructions
    - Battleships is a classic two-player. You will play the computer and each having 5 ships of varying sizes. The first to hit all 5 ships is the winner. You will see 2 grids, a tracking board and a ships position board. Both boards update with a ‘X’ for a hit and a ‘O’ for a miss. The tracking board shows if you hit the computer ship. The ship position board will show if the computer has hit or missed your ship. 
    The player takes turns against the computer to guess the locations of the computer's ships by entering co-ordinates (e.g., A3, B7) on the grid. The goal is to sink all of the computer's ships before they sink yours.

- 2. Game Information
    - Battleship is a strategy type guessing game for two players. It is played on a grid on which each player's fleet of warships are marked. The locations of the fleets are concealed from the other player. Players alternate turns taking shots at coordinates (e.g. A1, B5) at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.

## Design
I used [Lucidchart](https://www.lucidchart.com/) to design a flowchart to map out how the game would operate. 
The chart was a referance when writing the code.
![Flowchart](images/flowchart.png)

## Setting Up the Game:

- Function 1, Intro
    - intro page with 3 options. 
        - 1. Read instructions
        - 2. Game information
        - 3. Play Game
    - The options would display after the player chooses 1 and 2. Game would only start when the player chooses option 3
    - Input name: if the input is empty you’ll get an invalid message

- Function 2, create a grid. 
    - After research on the original game I used a 9x9 grid. 9 row and 9 columns. Board size can be changed if required as the sizes are constants called BOARD_SIZE_X and BOARD_SIZE_Y. 
    - This function will be used to create 4 boards. 1 each for the computer and players ship positions and 1 each for the computer and players shots.

- Function 3. Print board
    - Two boards are printed. player_shot (tracking board) and player_board (ship position) are placed in as arguments.

- Function 3, Place ships. 
    - The 5 ships of varying sizes are placed on the board, both horizontal and vertical. With random orientation and position on the grid. 
    - The ships are given a grey colour to match the original game. A letter to indicate what type of ship it is. e.g. ’S’ would be a submarine.
    - The 5 ships are:
        - Aircraft carrier, taking up 5 spaces
        - Battleship, 4 spaces
        - Destroyer, 3 spaces
        - Submarine, 2 spaces
        - Cruiser, 2 spaces

- Function 4, players turn.
    - The computers board (ship position) is checked to see if there is a ship at those coordinates and updates the board with a X for hit or O for miss. 
    - There is a printed message to say if was a hit and another printed message to say what type of ship was hit

- Function 5, computers turn.
    - The player board (ship position) is checked to see if there is a ship at those coordinates and updates the board with a X for hit or O for miss. 
    - There is a printed message to say if was a hit and another printed message to say what type of ship was hit

- Function 6, check game over.
    - The counter starts at 0 and when it reaches the constant of TOTAL_AREA_OF_ALL_SHIPS (sum of all ships) the game finishes.
        - To get the total number of spaces the 5 battleships took up. I placed the ships in a dictionary with their ship names and the value of their spaces. Using list comprehension I got the integer for each ship, summed those values and got the TOTAL_AREA_OF_ALL_SHIPS which I used in check_game_over. Score is 0, if score == TOTAL_AREA_OF_ALL_SHIPS, return true. This check_game_over() was used to check player and computer after each turn. 

- Function 7, main. 
    - 1, intro
        - 2, 4 board are created to track hit and miss. 
        - 3, Place ship function is called for player board and computer board.
        - 4, while play_game is true, do the following
            - print the board for the player to see, player_shot (tracking board) and player_board (ship position).
            - player turn and update hit and miss
            - check game over on computer board. if so you win
            - time.sleep(1) 1 second before moving on to computers turn
            - Computers turn and update hit and miss
            - check game over on player board. if so you loose
            - break loop
        - Option to play again when game is over

# UX Design

- Intro to the game.
    - [ASCII art](https://pypi.org/project/art/)
    I used ASCII art to print the title of the game “Battleship”
    ![Battleship ASCII art](images/intro_page.png)

- Colours within the game play
    - [Colorama](https://pypi.org/project/colorama/)
    Colorama was used a number of times for UX design
    - Error text red, indicating there was an error 
    - Hit or Miss. I used a red background for a hit and a blue background for a miss, for both the tracking boards (showing where the player had shot) and player ship positions (showing if the computer had hit the players ship). 
    - Red background with an ‘X’ for a hit or blue background with a ‘O’ for miss. 
    - Text for hit and miss. I used the same red and blue backgrounds for the text that was printed to the terminal after the players turn and computers turn
    ![hit, miss and ship colour](images/game_play.png)

- time.sleep()
    - After player shot and received the information on whether it was a hit or miss, I wanted a delay of 1 second so the player could take it in before been distracted by the two grids again.
    ![time.sleep(1)](images/time_sleep.png)

- Game Board design:
    - The player tracking grid and the player ship positions were on top of each other initially, making it hard to see without scrolling up. In order to fix this I placed 2 grids side by side in the print_board function and gave it parameters for 2 boards, the tracking board and the players ship positions.
    This function is called in the main game and is given the arguments, player_shot and player_board to print these boards to the terminal

## Manual Testing

- Game loads with link
- Options 1, 2, 3. game should only start if 3 is input
    - Read Instructions displays instructions when input is 1. 3 options appear again
    - Game information displays correctly when input is 2. 3 options appear again
    - Game starts when input is 3
    - When input is anything other then 1,2,3. an error message is printed. 3 options appear again
    ![error message](images/input_error_intro.png)
- Name input: When an empty input is returned, it displays an Invalid message and asks to input again
    ![name empty](images/empty_input_for_name.png)
- Co-ordinate input error: When the input length isn't 2 and isn't 0-8 for row and a-i for column
    ![Co-ordinate input error](images/co-ordinates_not_valid.png)

- Everything works correctly after manual testing


## Automated Testing

- The code was passed through the Code Institute Python Linter without any errors
![Screenshot of tezt results](images/ci_python_linter.png)


## Bugs Fixed
- I used (0, (BOARD_SIZE_X -1)) in placing the ships on the board. BOARD_SIZE_X = 9 so I needed to subtract 1 to make it fit into the board. Grid size starts at 0 not 1.
- In the computer_turn function, I had checked if the computer_tracking_board didn’t have a hit or miss (‘X’ or ‘O’) but I didn’t have an if statement to check if player_board’s position was ‘ ‘. Without this statement, the computer would get a hit on any cell.
- Player_turn() not showing the outer else message of “You’ve already fired at this location”. This is because I changed the “X” to have a red background and the “O” to have a blue background. Because of the difference in colour the outer if statement didn’t recognise the printed coloured cell. To make this work, I had to update the outer if statement with the colorama style too.
- Colorama making code too long: When using CI Linter, the code was too long in areas I had used colorama. To resolve this I made constants of the different colour options and only used the first initials. This made for shorter code.


## Code for later changes

- More ships: I created a constant that added up the value(size) of each ship. If the number of ships increased the TOTAL_AREA_OF_ALL_SHIPS
would be updated and the check_game_over() would still work without changes.
- Board size: a constant was given to board size. This value could be updated at a later date. BOARD_SIZE_X & BOARD_SIZE_Y


## Deployment

- Heroku was used to deploy my project online. Below are the steps
    - On the heroku dashboard, click "New" and select "Create new app"
    - Input a name for the app
    - Select Europe for the region
    - Press the button Create app
    - Next choose "Settings" from the nav bar above
    - "Add buildpack", heroku/python first and heroku/nodejs second. Make sure it is in this order.
    - From the nav bar above, select "Deploy"
    - Select "GitHub"
    - Select the "Connect to GitHub" button
    - Find your GitHub repository with the search bar and press connect
    - Finally click "Deploy Branch"


## Credits and resources 

- Code institute: Python code and walk-through project 
- Mentor Support: Spencer Barriball
- Tutor Support: Tutors at Code institute
- Random randint() function in Python: [Random function](https://www.geeksforgeeks.org/python-randint-function/)
- Geeksforgeeks: [string .join()](https://www.geeksforgeeks.org/python-string-join-method/) 
- String .join: [W3schools](https://www.w3schools.com/python/ref_string_join.asp)
- W3schools .strip: [.strip()](https://www.w3schools.com/python/ref_string_strip.asp) takes out any space before or after.
- W3schools .items: [.items()](https://www.w3schools.com/python/ref_dictionary_items.asp) view object, key-value pairs
- W3school .ord: [.ord()](https://www.w3schools.com/python/ref_func_ord.asp) return the number that represents the letter
- realpython.com how to add delay in your code. import time,  running  time.sleep()
- Caleb Curry: [python](https://www.youtube.com/watch?v=s3IvdkCq2_c&list=PLM5gEw77Ulp6NS27tsxG82WYwFzqP93nh&index=7)
- YouTube: [TechwithTim](https://www.youtube.com/@TechWithTim)
- Colorama: [Colorama](https://pypi.org/project/colorama/)
- ASCII: [ASCII art](https://pypi.org/project/art/)


## Content

- All text was written by the developer, Andrew O'Dwyer
- Photoshop was used to crop and stitch images together for the read me.
