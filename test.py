print("Hello, World!")
# Simple Tic Tac Toe implementation

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        try:
            move = input(f"Player {current_player}, enter row and column (e.g. 1 2): ")
            row, col = map(int, move.split())
            if board[row][col] != " ":
                print("Cell already taken! Try again.")
                continue
            board[row][col] = current_player
        except (ValueError, IndexError):
            print("Invalid input! Please enter row and column as numbers between 0 and 2.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# Uncomment the next line to play the game when running the script
# play_tic_tac_toe()