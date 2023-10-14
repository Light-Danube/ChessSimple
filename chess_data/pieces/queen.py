import pygame
import os

class Queen:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        # Construct the file path to the image dynamically
        image_folder = os.path.join('chess_assets', 'images', 'imgs-80px')
        image_filename = f'{color}_queen.png'
        image_path = os.path.join(image_folder, image_filename)

        # Load the image
        self.image = pygame.image.load(image_path)
        self.has_moved = False
    
    def move(self, new_position, board):
        row, col = self.pos
        new_row, new_col = new_position

        # Check if the target position is a valid move
        if new_position in self.get_valid_moves(board):
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

        # Horizontal and Vertical
        for r in range(8):
            if r != row:
                if board[r][col] is None or board[r][col].color != self.color:
                    valid_moves.append((r, col))

        for c in range(8):
            if c != col:
                if board[row][c] is None or board[row][c].color != self.color:
                    valid_moves.append((row, c))

        # Diagonal (up-right)
        r, c = row - 1, col + 1
        while r >= 0 and c < 8:
            if board[r][c] is None:
                valid_moves.append((r, c))
            else:
                if board[r][c].color != self.color:
                    valid_moves.append((r, c))
                break
            r -= 1
            c += 1

        # Continue with the logic for other diagonal directions.

        return valid_moves
