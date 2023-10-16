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
        
        if self.is_check(player_color):
            print(f"{player_color.capitalize()} is in check!")

        # Check if the game is in checkmate
        if self.is_checkmate(player_color):
            print(f"{player_color.capitalize()} is in checkmate!")

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
            and not self.selected_piece.castled
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
            and not self.selected_piece.castled
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
        self.selected_piece.move_castle(new_king_position, self.board, Rook)
        kingside_rook.move(kingside_rook_position, self.board)
    
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
        self.selected_piece.move_castle(new_king_position, self.board, Rook)
        queenside_rook.move(queenside_rook_position, self.board)   
    
    ### CHECK
    def get_king_position(self, color):
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King) and piece.color == color:
                    return (row, col)
        return None
    
    def is_check(self, player_color, board=None):
        # Find the king's position
        if board is None:
            board = self.board

        for row in range(8):
            for col in range(8):
                piece = board[row][col]
                if isinstance(piece, King) and piece.color == player_color:
                    king_position = (row, col)
                    break
            else:
                continue
            break

        # Check if the king is threatened by any opponent's piece
        for row in range(8):
            for col in range(8):
                piece = board[row][col]
                if piece is not None and piece.color != player_color:
                    valid_moves = piece.get_valid_moves(board)
                    if king_position in valid_moves:
                        return True
        return False


    def is_checkmate(self, player_color):
        # Find the king's position
        if not self.is_check(player_color):
            return False
        
        king_position = self.get_king_position(player_color)
        if king_position is None:
            return False  # King not found

        king_row, king_col = king_position

        # 2. Check if the king has any legal moves left
        for r in range(king_row - 1, king_row + 2):
            for c in range(king_col - 1, king_col + 2):
                if 0 <= r < 8 and 0 <= c < 8:
                    if not self.is_check_move(king_position, (r, c), player_color):
                        return False  # The king can escape

        # 3. Check if any piece can capture the attacking piece or block its path
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece is not None and piece.color == player_color:
                    valid_moves = piece.get_valid_moves(self.board)
                    for move in valid_moves:
                        if not self.is_check_move((row, col), move, player_color):
                            return False  # A piece can capture or block the attack

        # If all conditions are met, it's checkmate
        return True

    def is_check_move(self, from_position, to_position, player_color):
        # Simulate a move to check if the king is still in check
        new_board = [row[:] for row in self.board]
        from_row, from_col = from_position
        to_row, to_col = to_position

        new_board[to_row][to_col] = new_board[from_row][from_col]
        new_board[from_row][from_col] = None

        return self.is_check(player_color, new_board)
    
    
    def display_possible_king_moves(self, king_position):
        king = self.board[king_position[0]][king_position[1]]
        if isinstance(king, King) and self.is_check(king.color):
            possible_moves = king.get_possible_king_moves(self.board)
            for move in possible_moves:
                pygame.draw.circle(self.screen, (0, 255, 0), (move[1] * self.SQUARE_SIZE + self.SQUARE_SIZE // 2, move[0] * self.SQUARE_SIZE + self.SQUARE_SIZE // 2), 10)

    
    ### DRAW
    
    ### OTHER MOMENTS