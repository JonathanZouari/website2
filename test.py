print("Hello, World!")
print("hi")
def print_board(board):
    for i in range(3):
        print(' | '.join(board[i]))
        if i < 2:
            print("--+---+--")

def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    for row in board:
        if any(cell == ' ' for cell in row):
            return False
    return True

def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        try:
            move = input("Enter your move as row,col (1-3 for each): ")
            row, col = map(int, move.split(','))
            row -= 1
            col -= 1
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Move out of bounds, try again.")
                continue
            if board[row][col] != ' ':
                print("Cell already taken, try again.")
                continue
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = 'O' if current_player == 'X' else 'X'
        except Exception as e:
            print("Invalid input, please use format row,col (e.g. 1,3)")

# To play the game, uncomment the next line:
# tic_tac_toe()