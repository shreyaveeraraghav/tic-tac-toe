import random

def print_board_borders():
    print("|     |     |     |")

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-----+-----+-----+")
    for i in range(3):
        print_board_borders()
        print("|",end="")
        for j in range(3):
            if j == 2:
                print(" ",board[i][j]," |")
            else:
                print(" ",board[i][j]," |",end="")
        # print("\n")
        print_board_borders()
        print("+-----+-----+-----+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    flag = 0
    user_move = int(input("Enter your move: "))
    free_fields = make_list_of_free_fields(board)
    if user_move in free_fields.keys():
        loc = free_fields[user_move]
        board[loc[0]][loc[1]] = 'O'
    else:
        print("Move not possible")
        
def make_list_of_free_fields(board):
    # The function browses the board and builds a dictionary of all the free squares; 
    # the values for each of the keys consists of tuples, where each tuple is a pair of row and column numbers.
    free_fields = {}
    for i in range(3):
        for j in range(3):
            if (board[i][j] != 'O') and (board[i][j] != 'X'):
                free_fields[board[i][j]] = (i,j)
    # print(free_fields)
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] == sign:
            return True
    
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] == sign:
            return True
        
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]==sign :
        return True
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]==sign:
        return True
    
    return None
              

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_fields = make_list_of_free_fields(board)
    free_cells = list(free_fields.keys())
    computer_move = random.choice(free_cells)
    loc = free_fields[computer_move]
    board[loc[0]][loc[1]] = 'X'
    # print(computer_move)
    
    
board = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

display_board(board)
print("GAME BEGINS")
print("-----------\n")

while True:
    draw_move(board)
    display_board(board)
    enter_move(board)
    display_board(board)
    computer_winner = victory_for(board, 'X')
    if computer_winner == None:
        user_winner = victory_for(board, 'O')
        if user_winner == True:
            print("You won !!")
            break
    else:
        print("You lost !!")
        break
    
if user_winner != True and computer_winner != True:
    print("It's a tie!")





