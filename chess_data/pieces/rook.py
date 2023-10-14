import pygame
import os

from chess_data.pieces.king import King

class Rook:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        # Construct the file path to the image dynamically
        image_folder = os.path.join('chess_assets', 'images', 'imgs-80px')
        image_filename = f'{color}_rook.png'
        image_path = os.path.join(image_folder, image_filename)

        # Load the image
        self.image = pygame.image.load(image_path)
        self.has_moved = False
    
    def move(self, new_position, board):
        row, col = self.pos
        new_row, new_col = new_position

        # Check if the target position is a valid move
        valid_moves = self.get_valid_moves(board)
        if new_position in valid_moves:
            target_piece = board[new_row][new_col]

            # Capture the target piece if it's an enemy piece
            if target_piece is not None and target_piece.color != self.color:
                board[new_row][new_col] = None

            # Move the rook to the new position
            board[row][col] = None
            board[new_row][new_col] = self
            self.pos = new_position
            self.has_moved = True
    
    
    def get_valid_moves(self, board):
        valid_moves = []

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_row, new_col = self.pos[0] + dr, self.pos[1] + dc

            while 0 <= new_row < 8 and 0 <= new_col < 8:
                target_piece = board[new_row][new_col]

                if target_piece is None:
                    valid_moves.append((new_row, new_col))
                elif target_piece.color != self.color:
                    valid_moves.append((new_row, new_col))
                    break
                else:
                    break

                new_row, new_col = new_row + dr, new_col + dc

        return valid_moves
