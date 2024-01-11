# 1. Name:
#      Ella Galbraith
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#       For me the hardest pert was saving and reading the boards. 
#       When I was reading the boards and they were empty I had a lot of errors pop up.
#       When I saved the boards, they saved even after the game had been won.
# 5. How long did it take for you to complete the assignment?
#      -It took me about 5 hours to do this project. (Im a little rusty and I struggled a good amount but I did it!)

import json
import os

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }


def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Put file reading code here.
    try:
        with open(filename, "r") as saved_file:
            json_data = saved_file.read()
            if json_data:
                board_info = json.loads(json_data)
                return board_info
    except FileNotFoundError:
        #print(f"Unable to open the file: {filename}")
        return blank_board

def save_board(filename, board):
    '''Save the current game to a file.'''
    # Put file writing code here.
    try:
        with open(filename, "wt") as saved_file:
            json_data = json.dumps(board)
            saved_file.write(json_data)
    except FileNotFoundError:
        print(f"Unable to open the file: {filename}")

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.
    board_list = board["board"]

    print(" " + board_list[0] + " | " + board_list[1] + " | " + board_list[2] + " ")
    print("---+---+---")
    print(" " + board_list[3] + " | " + board_list[4] + " | " + board_list[5] + " ")
    print("---+---+---")
    print(" " + board_list[6] + " | " + board_list[7] + " | " + board_list[8] + " ")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    x_count = board["board"].count(X)
    o_count = board["board"].count(O)
    
    # If the number of 'X' and 'O' is the same or it's the first move, it's X's turn
    return x_count == o_count or (x_count + o_count == 0)

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.

    file_name = "pre_board.json"
    board = read_board(file_name)
    end = False
    while not end:
        if is_x_turn(board):
            display_board(board)
            player_choice = input("X> ")
            if player_choice == "q":
                save_board(file_name, board)
                return False
            else:
                player_choice = int(player_choice)
                if 1 <= player_choice <= 9 and board["board"][player_choice - 1] == BLANK:
                    board["board"][player_choice - 1] = X
                    end = game_done(board["board"])
                    if end:
                    #    with open(file_name, "w") as file:
                    #        pass
                    # chat gpt helped me with this.
                    # It deletes the file so new games can be new.
                        if os.path.exists(file_name):
                            os.remove(file_name)
                            #print("The file has been deleted.")
                else:
                    print("Invalid move. Please try again.") 
            
        else:
            display_board(board)
            player_choice = input("O> ")
            if player_choice == "q":
                save_board(file_name, board)
                return False
            else:
                player_choice = int(player_choice)
                if 1 <= player_choice <= 9 and board["board"][player_choice - 1] == BLANK:
                    board["board"][player_choice - 1] = O
                    end = game_done(board["board"])
                    if end:
                    #    with open(file_name, "w") as file:
                    #        pass
                    # chat gpt helped me with this.
                    # It deletes the file so new games can be new.
                        if os.path.exists(file_name):
                                os.remove(file_name)
                                #print("The file has been deleted.")
                else:
                    print("Invalid move. Please try again.")

    return False

def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.
play_game(blank_board)