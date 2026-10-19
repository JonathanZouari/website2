print("Hello, World!")
print("Hello Back")

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board):
    # check rows and columns
    for i in range(3):
        if (
            board[i][0] == board[i][1] == board[i][2] != " "
            or board[0][i] == board[1][i] == board[2][i] != " "
        ):
            return True
    # check diagonals
    if (
        board[0][0] == board[1][1] == board[2][2] != " "
        or board[0][2] == board[1][1] == board[2][0] != " "
    ):
        return True
    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        try:
            move = input(f"Player {current_player}, enter your move as row,col (1-3): ")
            row, col = map(int, move.strip().split(","))
            row -= 1
            col -= 1
            if row not in range(3) or col not in range(3):
                print("Invalid move: out of range.")
                continue
            if board[row][col] != " ":
                print("Invalid move: spot taken.")
                continue
            board[row][col] = current_player
            if check_win(board):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_player = "O" if current_player == "X" else "X"
        except Exception as e:
            print(f"Invalid input. Please enter in format 'row,col'.")

# Uncomment to play:
# tic_tac_toe()