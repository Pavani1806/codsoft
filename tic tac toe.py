import math

board = [" " for _ in range(9)]

def print_board():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print()

def check_winner(player):
    win_combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in win_combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def is_draw():
    return " " not in board

def minimax(is_ai):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if is_draw():
        return 0

    if is_ai:
        best = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best = min(best, score)
        return best

def ai_move():
    best_score = -math.inf
    move = 0
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    board[move] = "O"

print("Tic-Tac-Toe: You are X, AI is O")

while True:
    print_board()
    user_move = int(input("Enter position (0-8): "))
    board[user_move] = "X"

    if check_winner("X"):
        print_board()
        print("You win!")
        break

    if is_draw():
        print("Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI wins!")
        break
