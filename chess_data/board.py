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
                if isinstance(self.selected_piece, King) and col == 6 and self.can_castle_kingside(player_color):
                    # Perform kingside castling
                    self.castle_kingside(player_color)
                elif isinstance(self.selected_piece, King) and col == 2 and self.can_castle_queenside(player_color):
                    # Perform queenside castling
                    self.castle_queenside(player_color)
                else:
                    # Call the move method to move the selected piece
                    self.selected_piece.move(position, self.board)
                self.selected_piece = None
                self.valid_moves = []

    def get_valid_moves(self, player_color):
        valid_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.color == player_color and piece == self.selected_piece:
                    piece_valid_moves = piece.get_valid_moves(self.board)
                    valid_moves.extend([(row, col, r, c) for r, c in piece_valid_moves])
        return valid_moves
    
    ###CASTLING
    
    def can_castle_kingside(self, player_color):
        # Check if the kingside castling is possible for the current player
        if player_color == 'white':
            row = 7
            kingside_rook = self.board[row][7]
        else:
            row = 0
            kingside_rook = self.board[row][7]

        # Check if the kingside rook and king have not moved
        if (
            isinstance(kingside_rook, Rook) and not kingside_rook.has_moved
            and isinstance(self.selected_piece, King) and not self.selected_piece.has_moved
        ):
            # Check if the squares between the king and kingside rook are empty
            if all(self.board[row][col] is None for col in range(5, 7)):
                return True
        return False
    
    def can_castle_queenside(self, player_color):
        # Check if the queenside castling is possible for the current player
        if player_color == 'white':
            row = 7
            queenside_rook = self.board[row][0]
        else:
            row = 0
            queenside_rook = self.board[row][0]

        # Check if the queenside rook and king have not moved
        if (
            isinstance(queenside_rook, Rook) and not queenside_rook.has_moved
            and isinstance(self.selected_piece, King) and not self.selected_piece.has_moved
        ):
            # Check if the squares between the king and queenside rook are empty
            if all(self.board[row][col] is None for col in range(1, 4)):
                return True
        return False
    
    
    def castle_kingside(self, player_color):
        # Perform kingside castling for the current player
        if player_color == 'white':
            row = 7
            kingside_rook = self.board[row][7]
            kingside_rook_position = (row, 7)
            new_king_position = (row, 6)
        else:
            row = 0
            kingside_rook = self.board[row][7]
            kingside_rook_position = (row, 7)
            new_king_position = (row, 6)

        # Move the king and rook
        self.selected_piece.move(new_king_position, self.selected_piece)
        self.selected_piece.move(kingside_rook_position, kingside_rook)
    
    def castle_queenside(self, player_color):
        # Perform queenside castling for the current player
        if player_color == 'white':
            row = 7
            queenside_rook = self.board[row][0]
            queenside_rook_position = (row, 0)
            new_king_position = (row, 2)
        else:
            row = 0
            queenside_rook = self.board[row][0]
            queenside_rook_position = (row, 0)
            new_king_position = (row, 2)

        # Move the king and rook       
        self.selected_piece.move(new_king_position, self.selected_piece)
        self.selected_piece.move(queenside_rook_position, queenside_rook)   
    
    
    ### CHECK
    
    ### CHECKMATE
    
    ### DRAW
    
    ### OTHER MOMENTS