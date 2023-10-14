import pygame
from chess_data.pieces.pawn import Pawn
from chess_data.pieces.rook import Rook
from chess_data.pieces.queen import Queen
from chess_data.pieces.bishop import Bishop
from chess_data.pieces.knight import Knight
from chess_data.pieces.king import King

class Chessboard:
    def __init__(self, screen):
        self.screen = screen
        self.SQUARE_SIZE = 50
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.selected_piece = None
        self.valid_moves = []
        self.turn = 'white'  # Add a turn attribute

        # Define the initial configuration
        initial_config = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
            ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['', '', '', '', '', '', '', ''],
            ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP'],
            ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']
        ]

        self.setup_board(initial_config)

    def setup_board(self, config):
        for row in range(8):
            for col in range(8):
                piece_code = config[row][col]
                if piece_code:
                    piece = self.create_piece(piece_code, (row, col))
                    self.board[row][col] = piece

    def create_piece(self, piece_code, position):
        color = 'white' if piece_code[0] == 'w' else 'black'
        piece_type = piece_code[1]
        
        if piece_type == 'P':
            return Pawn(color, position)
        if piece_type == 'K':
            return King(color, position)
        if piece_type == 'N':
            return Knight(color, position)
        if piece_type == 'B':
            return Bishop(color, position)
        if piece_type == 'Q':
            return Queen(color, position)
        if piece_type == 'R':
            return Rook(color, position)

    def draw(self):
        for row in range(8):
            for col in range(8):
                color = (200, 200, 200) if (row + col) % 2 == 0 else (100, 100, 100)
                pygame.draw.rect(self.screen, color, (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE))
                
                piece = self.board[row][col]
                if piece:
                    piece_image = piece.image

                    # Resize the image to fit within the 50x50 pixel square
                    piece_image = pygame.transform.scale(piece_image, (self.SQUARE_SIZE, self.SQUARE_SIZE))

                    # Determine the offset to center the image within the square
                    x_offset = (self.SQUARE_SIZE - piece_image.get_width()) // 2
                    y_offset = (self.SQUARE_SIZE - piece_image.get_height()) // 2

                    # Calculate the position to blit the image on the screen
                    blit_position = (col * self.SQUARE_SIZE + x_offset, row * self.SQUARE_SIZE + y_offset)
                    
                    if piece == self.selected_piece:
                        pygame.draw.rect(self.screen, (0, 255, 0), (col * self.SQUARE_SIZE, row * self.SQUARE_SIZE, self.SQUARE_SIZE, self.SQUARE_SIZE), 4)

                    self.screen.blit(piece_image, blit_position)

    def handle_click(self, position, player_color):
        row, col = position
        piece = self.board[row][col]

        print("Clicked at", position, "Piece:", piece)  # Add this line

        if piece and piece.color == player_color:
            if piece == self.selected_piece:
                # Deselect the piece if it's already selected
                self.selected_piece = None
                self.valid_moves = []
            else:
                # Select the piece if it's not selected
                self.selected_piece = piece
                self.valid_moves = self.get_valid_moves(player_color)
                print("Valid Moves for", player_color, "Piece at", piece.pos, ":", self.valid_moves)
        elif self.selected_piece:
            print("Moving....")
            if (self.selected_piece.pos[0], self.selected_piece.pos[1], row, col) in self.valid_moves:
                # Call the move function to move the selected piece
                #print("Moving....")
                self.selected_piece.move((row, col), self.board)
                self.selected_piece = None
                self.valid_moves = []

    """def move_piece(self, piece, new_position):
        current_row, current_col = piece.pos
        new_row, new_col = new_position

        # Check if the clicked position is a valid move for the selected piece
        if new_position in self.valid_moves and piece is not None:
            self.board[current_row][current_col] = None  # Remove the piece from the old position
            piece.pos = new_position  # Update the piece's position
            self.board[new_row][new_col] = piece
            
            self.draw()

        # Deselect the piece after the move
        self.selected_piece = None
        self.valid_moves = []"""


    def get_valid_moves(self, player_color):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.color == player_color and piece == self.selected_piece:
                    piece_valid_moves = piece.get_valid_moves(self.board)
                    valid_moves.extend([(row, col, r, c) for r, c in piece_valid_moves])
        return valid_moves