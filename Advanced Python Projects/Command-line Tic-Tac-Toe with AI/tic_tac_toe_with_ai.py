# 40.  Command-line Tic-Tac-Toe with AI   
#     *Description*: Implement a Tic-Tac-Toe game that includes an AI opponent using basic algorithms.  
#     *Skills*: Game logic, conditionals, loops.

import random

# Function to initialize the game board
def raw_board():
    return [" " for _ in range(9)]  # Create a list with 9 empty spaces

# Function to display the current state of the board
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Function to switch the current player
def switch_player(player_mode):
    return "O" if player_mode == "X" else "X"  # Toggle between "X" and "O"

# Function for the player's move
def player_move(board, player):
    while True:
        try:
            # Prompt the player to enter their move (1-9)
            move = int(input(f'Player {player}: Enter your move (1-9): ')) - 1
            
            # Check for valid move
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move. Try again.")
            else:
                board[move] = player  # Place the player's marker on the board
                break
        except ValueError:
            print("You entered an invalid value")

# Minimax algorithm to find the best move for the AI
def minimax(board, depth, is_maximizing):
    # Check for a terminal state: win, lose, or draw
    if check_winners(board, "O"):
        return 1  # AI wins
    elif check_winners(board, "X"):
        return -1  # Player wins
    elif " " not in board:
        return 0  # Draw

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"  # AI's turn
                score = minimax(board, depth + 1, False)
                board[i] = " "  # Undo move
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"  # Player's turn
                score = minimax(board, depth + 1, True)
                board[i] = " "  # Undo move
                best_score = min(score, best_score)
        return best_score

# Function for the AI's move using Minimax
def ai_move(board, player):
    best_score = -float('inf')
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = player  # AI makes a move
            score = minimax(board, 0, False)  # Call Minimax
            board[i] = " "  # Undo move
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = player  # Place the AI's marker on the board
    print(f"AI ({player}) has selected position {best_move + 1}")  # Inform about AI's move

# Function to check for a winner
def check_winners(board, player):
    # Define winning conditions
    winner_condition = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    
    # Check if the current player has met any winning condition
    for condition in winner_condition:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Main game loop
def play_game():
    board = raw_board()  # Initialize the game board
    # Ask user to select game mode: Player vs Player or Player vs AI
    mode = input("Choose game mode: 1 for Player vs Player, 2 for Player vs AI: ")

    current_player = "X"  # Player "X" always starts first
    moves = 0  # Track the number of moves made

    # Main game loop
    while moves < 9:  # A maximum of 9 moves in Tic-Tac-Toe
        display_board(board)  # Display the current board
        
        # Check game mode
        if mode == "1":  # Player vs Player
            player_move(board, current_player)
        elif mode == "2" and current_player == "X":  # Player vs AI, Player "X" turn
            player_move(board, current_player)
        elif mode == "2" and current_player == "O":  # AI's turn when player is "X"
            ai_move(board, current_player)  # AI makes its move
        
        # Check if the current player has won
        if check_winners(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")  # Announce winner
            break
        
        # Switch to the next player
        current_player = switch_player(current_player)
        moves += 1  # Increment the number of moves

    # Check for a draw
    if moves == 9:  # If the board is full and no one wins
        display_board(board)
        print("It's a draw!")  # Announce draw

# Start the game
play_game()
