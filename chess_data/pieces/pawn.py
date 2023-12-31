import pygame
import os

class Pawn:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        # Construct the file path to the image dynamically
        image_folder = os.path.join('chess_assets', 'images', 'imgs-80px')
        image_filename = f'{color}_pawn.png'
        image_path = os.path.join(image_folder, image_filename)

        # Load the image
        self.image = pygame.image.load(image_path)
        self.has_moved = False
        
    def capture(self, target_position, board):
        row, col = self.pos
        target_row, target_col = target_position

        # Check if the target position is a valid capture
        if abs(target_row - row) == 1 and abs(target_col - col) == 1:
            target_piece = board[target_row][target_col]

            if target_piece is not None and target_piece.color != self.color:
                board[target_row][target_col] = None
                self.move(target_position, board)
                return True
    
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

        if self.color == 'white':
            if row > 0 and board[row - 1][col] is None:
                valid_moves.append((row - 1, col))
                if row == 6 and board[4][col] is None:
                    valid_moves.append((4, col))
            if row > 0 and col > 0 and board[row - 1][col - 1] is not None and board[row - 1][col - 1].color == 'black':
                valid_moves.append((row - 1, col - 1))
            if row > 0 and col < 7 and board[row - 1][col + 1] is not None and board[row - 1][col + 1].color == 'black':
                valid_moves.append((row - 1, col + 1))
        elif self.color == 'black':
            if row < 7 and board[row + 1][col] is None:
                valid_moves.append((row + 1, col))
                if row == 1 and board[3][col] is None:
                    valid_moves.append((3, col))
            if row < 7 and col > 0 and board[row + 1][col - 1] is not None and board[row + 1][col - 1].color == 'white':
                valid_moves.append((row + 1, col - 1))
            if row < 7 and col < 7 and board[row + 1][col + 1] is not None and board[row + 1][col + 1].color == 'white':
                valid_moves.append((row + 1, col + 1))

        return valid_moves
