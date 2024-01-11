# 1. Name:
#      Ella Galbraith
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      This program must display a sudoku board and allow the user to play
#      It will not allow invalid moves
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out how to check the box to see if the  was correct.
#      Another thing that was really hard was going through and making sure every test case handles the error in a smooth way.
# 5. How long did it take for you to complete the assignment?
#      It took me about 4 hours to do including the video.

import json

def main():
    user_board = input("What is the name of the board?: ")
    board = read_board(user_board)
    display_board(board)
    keep_going = play_round(board)
    write_board(user_board, board)
    while keep_going != None:
        if keep_going == False:
            return
        display_board(board)
        keep_going = play_round(board)
        write_board(user_board, board)

    return

def read_board(file_name):
    # send a board to main
    with open(file_name, "r") as board:
        board_data = json.load(board)
        the_board = board_data["board"]
    return the_board

def display_board(board):
    # display the board
    print("A B C D E F G H I ")
    for row in range(9):
        if row == 3 or row == 6:
            print("- - + - - + - - +")
        for column in range(9):
            separator = "  |  |  \n"
            if  1 <= board[row][column] <= 9:
                print(board[row][column], end="")
                print(separator[column], end="")
            else:
                print(" ", end="")
                print(separator[column], end="")

def play_round(board):
    # update the board by calling two functions
    print("Specify a coordinate to edit or 'Q' to save and quit")
    coordinates = input("> ").upper()
    if coordinates == "Q":
        print("Thank you for playing! ")
        return False
    # first function called
    spot = parse_input(coordinates, board)
    while spot[0] == -1 or spot[1] == -1:
        print("invalid Input. Try again. ")
        coordinates = input("> ").upper()
        if coordinates == "Q":
            return False
        spot = parse_input(coordinates, board)

    number = input(f"What number goes in {coordinates}?: ").upper()
    if number == "Q":
        print("Thank you for playing! ")
        return False
    while number == "S":
        # display the options in a list
        show_options(spot, board)
        number = input(f"What number goes in {coordinates}?: ").upper()
        if number == "Q":
            print("Thank you for playing! ")
            return False

    while number.isdigit() == False:
        print("Invalid input. Try again.")
        number = input(f"What number goes in {coordinates}?: ").upper()
        if number == "Q":
            print("Thank you for playing! ")
            return False
    
    number = int(number)
    # second function called
    is_valid = is_legal(board, spot, number)
    while is_valid != True:
        print("Your move was invalid. Try again. ")
        number = input(f"What number goes in {coordinates}?: ").upper()
        if number == "S":
            show_options(coordinates, board)
        
        number = int(number)
        spot = parse_input(coordinates, board)
        is_valid = is_legal(board, spot, number)
    
    board[spot[0]][spot[1]] = int(number)
    return board    

def show_options(coordinates, board):
    row = coordinates[0]
    column = coordinates[1]
    box_row = 3 * (row // 3)
    box_column = 3 * (column // 3)
    possible = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for num in possible:
        if num in board[row]:
            possible.remove(num)
        elif num in board[column]:
            if num in possible:
                possible.remove(num)
        for i in range(box_row, box_row + 3):
            for ind in range(box_column, box_column + 3):
                if board[i][ind] == num:
                    if num in possible:
                        possible.remove(num)    
    return print(f"Your options for the spot {coordinates} is: {possible}")

def parse_input(text, board):
    # turns an input like A4 into a row & column like 0 7
    row = -1
    column = -1

    if text[0].isdigit():
        text = text[::-1]

    if len(text) != 2:
        return (row, column)

    for letter in text:
        if "A" <= letter <= "I":
            column = ord(letter) - ord("A")
        elif letter.isdigit() and "1" <= letter <= "9":
            row = int(letter) - 1

# check if the coordinates dont equal 0 then a move can't be made
    if board[row][column] != 0:
        print("Your coordinates are full and / or its an ", end="")
        row = -1
        column = -1

    return (row, column)

def is_legal(board, coordinates, number):
    # will check board, row and column and determine if the number fits
    row = coordinates[0]
    column = coordinates[1]
    x = board[row]
    box_row = 3 * (row // 3)
    box_column = 3 * (column // 3)
    # check if row has the number
    if number in x:
        return False
    # check if column has number
    for i in range(9):
        if board[i][column] == number:
            return False
    # check if the little box has number
    for i in range(box_row, box_row + 3):
        for ind in range(box_column, box_column + 3):
            if board[i][ind] == number:
                return False

    return True

def write_board(board_name, board):
    data = {
        "board" : board
    }
    with open(board_name, 'w') as board_file:
        json.dump(data, board_file)
        # board_file.write(board)

# if __debug__:


main()