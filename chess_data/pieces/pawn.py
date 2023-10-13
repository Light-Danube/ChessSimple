import pygame

class Pawn:
    def __init__(self, color, pos, img_path):
        self.color = color
        self.pos = pos
        self.img_path = pygame.image.load(img_path)
        self.SQUARE_SIZE = self.image.get_width()
    
    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.position

        if self.color == 'white':
            if row > 0 and board[row - 1][col] is None:
                valid_moves.append((row - 1, col))
                if row == 6 and board[4][col] is None:
                    valid_moves.append((4, col))
            if row > 0 and col > 0 and board[row - 1][col - 1] is not None and board[row - 1][col - 1].color == 'black':
                valid_moves.append((row - 1, col - 1))
            if row > 0 and col < 7 and board[row - 1][col + 1] is not None and board[row - 1][col + 1].color == 'black':
                valid_moves.append((row - 1, col + 1))
        elif self.color == 'black':  # Black Pawn
            if row < 7 and board[row + 1][col] is None:
                valid_moves.append((row + 1, col))
                if row == 1 and board[3][col] is None:
                    valid_moves.append((3, col))
            
            # Diagonaly captures:
            if row < 7 and col > 0 and board[row + 1][col - 1] is not None and board[row + 1][col - 1].color == 'white':
                valid_moves.append((row + 1, col - 1))
            if row < 7 and col < 7 and board[row + 1][col + 1] is not None and board[row + 1][col + 1].color == 'white':
                valid_moves.append((row + 1, col + 1))

        return valid_moves
