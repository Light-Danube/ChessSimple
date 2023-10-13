import pygame
import os

class Rook:
    def __init__(self, color, pos):
        self.color = color
        self.position = pos
        # Construct the file path to the image dynamically
        image_folder = os.path.join('chess_assets', 'images', 'imgs-80px')
        image_filename = f'{color}_rook.png'
        image_path = os.path.join(image_folder, image_filename)

        # Load the image
        self.image = pygame.image.load(image_path)
        self.has_moved = False
    
    def get_image(self):
        return self.image
    
    
    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.position

        # Check vertically
        for r in range(row + 1, 8):
            if board[r][col] is None:
                valid_moves.append((r, col))
            else:
                if board[r][col].color != self.color:
                    valid_moves.append((r, col))
                break

        for r in range(row - 1, -1, -1):
            if board[r][col] is None:
                valid_moves.append((r, col))
            else:
                if board[r][col].color != self.color:
                    valid_moves.append((r, col))
                break

        # Check horizontally
        for c in range(col + 1, 8):
            if board[row][c] is None:
                valid_moves.append((row, c))
            else:
                if board[row][c].color != self.color:
                    valid_moves.append((row, c))
                break

        for c in range(col - 1, -1, -1):
            if board[row][c] is None:
                valid_moves.append((row, c))
            else:
                if board[row][c].color != self.color:
                    valid_moves.append((row, c))
                break

        return valid_moves
