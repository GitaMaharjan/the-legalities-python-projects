# 30.  Command-line Chess Game   
#     *Description*: Develop a simple chess game that can be played in the console.  
#     *Skills*: Object-oriented programming, game logic, recursion.

class Piece:
    def __init__(self, color):
        # Initialize a piece with its color (white or black)
        self.color = color

    def symbol(self):
        # Method to return the symbol of the piece, must be overridden in subclasses
        raise NotImplementedError("This method should be overridden in subclasses.")

# Define subclasses for each piece type
class Pawn(Piece):
    def symbol(self):
        # Return 'P' for white and 'p' for black
        return 'P' if self.color == 'white' else 'p'


class Rook(Piece):
    def symbol(self):
        # Return 'R' for white and 'r' for black
        return 'R' if self.color == 'white' else 'r'


class Knight(Piece):
    def symbol(self):
        # Return 'N' for white and 'n' for black
        return 'N' if self.color == 'white' else 'n'


class Bishop(Piece):
    def symbol(self):
        # Return 'B' for white and 'b' for black
        return 'B' if self.color == 'white' else 'b'


class Queen(Piece):
    def symbol(self):
        # Return 'Q' for white and 'q' for black
        return 'Q' if self.color == 'white' else 'q'


class King(Piece):
    def symbol(self):
        # Return 'K' for white and 'k' for black
        return 'K' if self.color == 'white' else 'k'


class Board:
    def __init__(self):
        # Initialize the board by creating a new chessboard
        self.board = self.create_board()

    def create_board(self):
        # Create the initial setup of the chessboard with pieces in their starting positions
        return [
            [Rook('black'), Knight('black'), Bishop('black'), Queen('black'), King('black'), Bishop('black'), Knight('black'), Rook('black')],
            [Pawn('black')] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [Pawn('white')] * 8,
            [Rook('white'), Knight('white'), Bishop('white'), Queen('white'), King('white'), Bishop('white'), Knight('white'), Rook('white')]
        ]

    def display(self):
        # Print the current state of the board to the console
        print("  a b c d e f g h")  # Print column labels
        for i, row in enumerate(self.board):
            print(8 - i, end=' ')  # Print row labels (1 to 8)
            for piece in row:
                print(str(piece.symbol()) if piece else '.', end=' ')  # Print piece symbol or '.' for empty squares
            print()  # New line after each row


class Game:
    def __init__(self):
        # Initialize the game with a board and track whose turn it is and captured pieces
        self.board = Board()
        self.current_turn = 'white'  # Set starting turn to white
        self.captured_pieces = {'white': 0, 'black': 0}  # Track the number of captured pieces

    def move_piece(self, from_pos, to_pos):
        # Handle the logic for moving a piece from one position to another
        col_from = ord(from_pos[0]) - ord('a')  # Convert column from 'a'-'h' to 0-7
        row_from = 8 - int(from_pos[1])          # Convert row from '1'-'8' to 0-7
        col_to = ord(to_pos[0]) - ord('a')      # Convert destination column
        row_to = 8 - int(to_pos[1])              # Convert destination row

        piece = self.board.board[row_from][col_from]  # Get the piece at the starting position
        
        # Check if the selected piece belongs to the current player
        if piece is None:
            print("No piece at the selected position. Please try again.")
            return False

        if piece.color != self.current_turn:
            print(f"It's {self.current_turn.capitalize()}'s turn. You cannot move the opponent's piece.")
            return False

        # Capture logic: Check if there's an opponent's piece at the destination
        target_piece = self.board.board[row_to][col_to]
        if target_piece and target_piece.color != self.current_turn:
            self.captured_pieces[self.current_turn] += 1  # Increment captured count
            print(f"{target_piece.symbol()} captured!")  # Notify capture

        # Move the piece to the new position
        self.board.board[row_to][col_to] = piece
        self.board.board[row_from][col_from] = None  # Empty the original position
        return True  # Move successful

    def play(self):
        # Main game loop to play the chess game
        print("Welcome to Console Chess!")  # Welcome message
        print("Piece representation:")  # Information about piece representation
        print("White pieces:  Uppercase (e.g., P, R, N, B, Q, K)")
        print("Black pieces:  Lowercase (e.g., p, r, n, b, q, k)")
        print()

        while True:
            self.board.display()  # Display the current board
            print(f"Captured pieces - White: {self.captured_pieces['white']}, Black: {self.captured_pieces['black']}")
            from_pos = input(f"{self.current_turn.capitalize()}'s turn. Move from (e.g., e2): ")  # Get starting position
            to_pos = input("Move to (e.g., e4): ")  # Get destination position
            if self.move_piece(from_pos, to_pos):  # Try to move the piece
                self.current_turn = 'black' if self.current_turn == 'white' else 'white'  # Switch turns
            else:
                print("Invalid move, try again.")  # If move failed, notify the player

# Entry point for the game
if __name__ == "__main__":
    game = Game()  # Create a new game instance
    game.play()    # Start the game
