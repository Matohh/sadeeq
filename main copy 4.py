import random

def display_board(board):
    for row in board:
        print(" ".join(row))

def create_board(size):
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(random.choice(['X', 'O', ' ']))
        board.append(row)
    return board

def check_win(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    for col in range(len(board)):
        check_col = []
        for row in board:
            check_col.append(row[col])
        if check_col.count(check_col[0]) == len(check_col) and check_col[0] != ' ':
            return True

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

def play_game():
    board = create_board(3)
    display_board(board)
    player = 'X'

    while not check_win(board):
        move = input(f"{player}'s turn. Enter your move (1-9): ")
        row, col = divmod(int(move) - 1, 3)

        if board[row][col] == ' ':
            board[row][col] = player
            display_board(board)
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

    print(f"{player} wins!")

play_game()