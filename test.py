def print_board(board):
    print("Current board:")
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")

def check_winner(board):
    # check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    print("Welcome to Tic Tac Toe!")
    print_board(board)
    while True:
        print(f"Player {current_player}'s turn.")
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue
        if 0 <= row < 3 and 0 <= col < 3:
            if board[row][col] == ' ':
                board[row][col] = current_player
                print_board(board)
                winner = check_winner(board)
                if winner:
                    print(f"Player {winner} wins!")
                    break
                if is_full(board):
                    print("It's a draw!")
                    break
                current_player = 'O' if current_player == 'X' else 'X'
            else:
                print("That cell is already occupied. Try again.")
        else:
            print("Invalid board position. Try again.")

if __name__ == "__main__":
    main()
    print("game over2")
