import pygame
import os

class Knight:
    def __init__(self, color, pos):
        self.color = color
        self.position = pos
        # Construct the file path to the image dynamically
        image_folder = os.path.join('chess_assets', 'images', 'imgs-80px')
        image_filename = f'{color}_knight.png'
        image_path = os.path.join(image_folder, image_filename)

        # Load the image
        self.image = pygame.image.load(image_path)
        self.has_moved = False
    
    def get_image(self):
        return self.image
    
    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.position

        moves = [(row - 2, col - 1), (row - 2, col + 1), (row - 1, col - 2), (row - 1, col + 2),
                 (row + 1, col - 2), (row + 1, col + 2), (row + 2, col - 1), (row + 2, col + 1)]

        for r, c in moves:
            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None or board[r][c].color != self.color:
                    valid_moves.append((r, c))

        return valid_moves
