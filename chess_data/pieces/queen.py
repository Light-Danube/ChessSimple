import pygame
import os

class Queen:
    def __init__(self, color, pos):
        self.color = color
        self.position = pos
        # Construct the file path to the image dynamically
        image_folder = os.path.join('chess_assets', 'images', 'imgs-80px')
        image_filename = f'{color}_queen.png'
        image_path = os.path.join(image_folder, image_filename)

        # Load the image
        self.image = pygame.image.load(image_path)
        self.has_moved = False
    
    def get_image(self):
        return self.image
    
    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.position

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
