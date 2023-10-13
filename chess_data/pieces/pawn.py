import pygame
import os

class Pawn:
    def __init__(self, color, pos, board):
        self.color = color
        self.position = pos
        self.board = board  # Reference to the board
        # Construct the file path to the image dynamically
        image_folder = os.path.join('chess_assets', 'images', 'imgs-80px')
        image_filename = f'{color}_pawn.png'
        image_path = os.path.join(image_folder, image_filename)

        # Load the image
        self.image = pygame.image.load(image_path)
        self.has_moved = False

    def draw(self, display, x, y):
        # Draw the pawn piece at the specified position (x, y) on the display
        display.blit(self.image, (x, y))

    def get_image(self):
        return self.image

    def move(self, new_position):
        # Implement the move logic for the pawn
        # Ensure that the move is valid before updating the position
        if self.is_valid_move(new_position):
            self.position = new_position
            self.has_moved = True
    
    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.position

        if self.color == 'white':
            # Move one square forward if empty
            if row > 0 and board[row - 1][col] is None:
                valid_moves.append((row - 1, col))
                if not self.has_moved and board[row - 2][col] is None:
                    valid_moves.append((row - 2, col))
            
            # Capture diagonally
            if row > 0 and col > 0 and board[row - 1][col - 1] is not None and board[row - 1][col - 1].color == 'black':
                valid_moves.append((row - 1, col - 1))
            if row > 0 and col < 7 and board[row - 1][col + 1] is not None and board[row - 1][col + 1].color == 'black':
                valid_moves.append((row - 1, col + 1))
        elif self.color == 'black':
            # Move one square forward if empty
            if row < 7 and board[row + 1][col] is None:
                valid_moves.append((row + 1, col))
                if not self.has_moved and board[row + 2][col] is None:
                    valid_moves.append((row + 2, col))
            
            # Capture diagonally
            if row < 7 and col > 0 and board[row + 1][col - 1] is not None and board[row + 1][col - 1].color == 'white':
                valid_moves.append((row + 1, col - 1))
            if row < 7 and col < 7 and board[row + 1][col + 1] is not None and board[row + 1][col + 1].color == 'white':
                valid_moves.append((row + 1, col + 1))
        
        return valid_moves