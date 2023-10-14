import pygame
import os

class King:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        # Construct the file path to the image dynamically
        image_folder = os.path.join('chess_assets', 'images', 'imgs-80px')
        image_filename = f'{color}_king.png'
        image_path = os.path.join(image_folder, image_filename)

        # Load the image
        self.image = pygame.image.load(image_path)
        self.has_moved = False
    
    def move(self, new_position, board):
        row, col = self.pos
        new_row, new_col = new_position

        # Check if the target position is a valid move
        if new_position in self.get_valid_moves(board):
            # Check for castling move
            if new_row == row and abs(new_col - col) == 2:
                if new_col > col:  # Kingside castling
                    rook = board[row][7]
                    new_rook_position = (new_row, new_col - 1)
                else:  # Queenside castling
                    rook = board[row][0]
                    new_rook_position = (new_row, new_col + 1)

                # Move the rook to the new position
                board[row][col] = None
                board[new_row][new_col] = self
                self.pos = new_position
                self.has_moved = True

                board[rook.pos[0]][rook.pos[1]] = None
                board[new_rook_position[0]][new_rook_position[1]] = rook
                rook.pos = new_rook_position
                rook.has_moved = True
        else:
            target_piece = board[new_row][new_col]

            # Capture the target piece if it's an enemy piece
            if target_piece is not None and target_piece.color != self.color:
                board[new_row][new_col] = None

            # Move the pawn to the new position
            board[row][col] = None
            board[new_row][new_col] = self
            self.pos = new_position
            self.has_moved = True
            
    
    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.pos

        moves = [
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1),                     (row, col + 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
        ]

        for r, c in moves:
            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None or board[r][c].color != self.color:
                    valid_moves.append((r, c))

        return valid_moves
