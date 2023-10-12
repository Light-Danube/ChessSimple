import pygame
#from .pieces.pawn import Pawn  # Import the Pawn class from the pieces package
#from .pieces.rook import Rook
#from .pieces.queen import Queen
#from .pieces.king import King
#from .pieces.knight import Knight
#from .pieces.bishop import Bishop

class Chessboard:
    def __init__(self, screen):
        self.screen = screen
        self.SQUARE_SIZE = screen.get_width() // 8
        self.board = self.setup_board()
        self.selected_piece = None
        self.valid_moves = []

    def setup_board(self):
        ### Initialize the chessboard with pieces
        board = [[None] * 8 for _ in range(8)]

        # Set up pawns for both sides
        #for col in range(8):
            #board[1][col] = Pawn('black', (1, col))
            #board[6][col] = Pawn('white', (6, col))

        # You would continue to set up other pieces (rooks, knights, etc.) here.

        return board

    def draw(self):
        for row in range(8):
            for col in range(8):
                color = (200, 200, 200) if (row + col) % 2 == 0 else (100, 100, 100)
                pygame.draw.rect(self.screen, color, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))
                
                piece = self.board[row][col]
                if piece:
                    piece.draw(self.screen)

    def handle_click(self, position):
        row, col = position
        if not self.selected_piece:
            piece = self.board[row][col]
            if piece is not None:  # Check if there's a piece on the clicked square
                if piece.color == 'white':
                    self.selected_piece = piece
                    self.valid_moves = self.get_valid_moves(piece)
        else:
            if position in self.valid_moves:
                # Move the selected piece
                self.move_piece(self.selected_piece, position)
                self.selected_piece = None
                self.valid_moves = []

    def move_piece(self, piece, new_position):
        # Update the board and piece's position
        current_row, current_col = piece.position
        new_row, new_col = new_position
        self.board[current_row][current_col] = None
        self.board[new_row][new_col] = piece
        piece.position = new_position

    def get_valid_moves(self, player_color):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.color == player_color:
                    piece_valid_moves = piece.get_valid_moves(self.board)
                    valid_moves.extend([(row, col, r, c) for r, c in piece_valid_moves])
        return valid_moves
