# 13.  Tic-Tac-Toe Game   
#     *Description*: Create a two-player Tic-Tac-Toe game.  
#     *Skills*: Loops, conditionals, lists.


def raw_board():
    return [" " for _ in range(9)]

def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# display_board(raw_board())
def switch_player(player_mode):
    return "O" if player_mode == "X" else "X"

def player_move(board,player):
    while True:
        try:
            move=int(input(f'Player {player}: Enter your move(1-9): ')) - 1   
            
            if move <0 or move > 8 or board[move]!=" ":
                print("Invalid move. Try again.")
            else:
                board[move]=player
                # print(board)
                break
        except ValueError:
            print("You entered the invalid value")
            
# player_move(raw_board(),switch_player("O"))


def check_winners(board,player):
    winner_condition = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (1,4,8),(2,4,6)
    ]
    
    for condition in winner_condition:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Main game loop
def play_game():
    board = raw_board()
    current_player = "X"
    moves = 0

    while moves < 9:  # A maximum of 9 moves in Tic-Tac-Toe
        display_board(board)
        player_move(board, current_player)
        
        if check_winners(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        
        current_player = switch_player(current_player)
        moves += 1

    if moves == 9:  # If the board is full and no one wins
        display_board(board)
        print("It's a draw!")

# Start the game
play_game()