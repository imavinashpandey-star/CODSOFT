#Tic Tac Toe AI
import math
board = [" " for _ in range(9)]
# Display the game board
def print_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i < 6:
            print("---+---+---")
    print()

# Check winner
def check_winner(player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in pos) for pos in win_positions)

# Check draw
def is_draw():
    return " " not in board

# Minimax Algorithm
def minimax(is_max):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_max:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = " "
        return best

# AI Move
def ai_move():
    best_score = -math.inf
    best_move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

# Player Move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1

            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move! Try again.")

        except ValueError:
            print("Please enter a valid number.")

# Main Game
def main():
    print("=" * 40)
    print("       TIC TAC TOE AI")
    print("=" * 40)
    print("You are X | AI is O\n")

    print("Board Positions")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9\n")

    while True:
        print_board()

        player_move()

        if check_winner("X"):
            print_board()
            print("Congratulations! You Win!")
            break

        if is_draw():
            print_board()
            print("It's a Draw!")
            break

        print("\nAI is making a move...\n")
        ai_move()

        if check_winner("O"):
            print_board()
            print("AI Wins!")
            break

        if is_draw():
            print_board()
            print("It's a Draw!")
            break

if __name__ == "__main__":
    main()
