#!/usr/bin/env python3

PLAYER_X = "X"
PLAYER_O = "O"
EMPTY_CELL = " "

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != EMPTY_CELL:
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY_CELL:
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY_CELL:
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY_CELL:
        return True

    return False

def is_full(board):
    for row in board:
        if EMPTY_CELL in row:
            return False
    return True

def switch_player(current_player):
    return PLAYER_O if current_player == PLAYER_X else PLAYER_X

def tic_tac_toe():
    board = [[EMPTY_CELL]*3 for _ in range(3)]
    player = PLAYER_X
    print("Welcome to Tic-Tac-Toe!")
    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter 0, 1, or 2.")
                continue
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if board[row][col] == EMPTY_CELL:
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            player = switch_player(player)
        else:
            print("That spot is already taken! Try again.")

tic_tac_toe()