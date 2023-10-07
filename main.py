import random

def display_board(board):
    print("\n".join(map(str, board)))

def check_win(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            return True

    for col in range(len(board)):
        check_col = []
        for row in board:
            check_col.append(row[col])
        if check_col.count(check_col[0]) == len(check_col) and check_col[0] != 0:
            return True

    return False

def check_draw(board):
    for row in board:
        for item in row:
            if item == 0:
                return False
    return True

def player_move(board, player):
    valid_move = False
    while not valid_move:
        move = input(f"Player {player}, enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move)
            row = (move - 1) // 3
            col = (move - 1) % 3
            if board[row][col] == 0:
                valid_move = True
                board[row][col] = player
            else:
                print("Invalid move, that spot is already occupied.")
        else:
            print("Invalid move, please enter a number between 1 and 9.")

def play_game():
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    current_player = 1
    display_board(board)

    while not check_win(board) and not check_draw(board):
        player_move(board, current_player)
        display_board(board)
        current_player = 2 if current_player == 1 else 1

    if check_win(board):
        print(f"Player {current_player} wins!")
    else:
        print("It's a draw!")

play_game()