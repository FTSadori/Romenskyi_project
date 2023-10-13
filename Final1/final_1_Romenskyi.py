from random import randrange


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in range(len(board)):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   {0}   |   {1}   |   {2}   |".format(board[i][0], board[i][1], board[i][2]));
        print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    while True:
        try:
            user_move = int(input("Enter your move: ")) - 1
            if board[user_move // 3][user_move % 3] not in "OX":
                board[user_move // 3][user_move % 3] = 'O'
                return
        except Exception:
            continue


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_moves = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] not in "OX":
                free_moves.append((i, j))
    return free_moves


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    # Check rows
    for i in range(len(board)):
        if board[i][:] == [sign, sign, sign]:
            return True
    # Check columns
    for j in range(len(board[0])):
        if [board[0][j], board[1][j], board[2][j]] == [sign, sign, sign]:
            return True
    # Check diagonals
    if [board[0][0], board[1][1], board[2][2]] == [sign, sign, sign]:
        return True
    if [board[0][2], board[1][1], board[2][0]] == [sign, sign, sign]:
        return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_moves = make_list_of_free_fields(board)
    num = randrange(len(free_moves))
    move = free_moves[num]
    board[move[0]][move[1]] = 'X'


board = [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]
display_board(board)

while True:
    # Your turn
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("You won :)")
        break
    elif len(make_list_of_free_fields(board)) == 0:
        print("Draw :|")
        break

    # Bot turn
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("No :(")
        break
    elif len(make_list_of_free_fields(board)) == 0:
        print("Tie :|")
        break
