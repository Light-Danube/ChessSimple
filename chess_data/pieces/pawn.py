import pygame

class Pawn:
    def __init__(self, color, pos):
        self.color = color
        self.pos = pos
        #self.image = pygame.image.load(f'chess_assets/images/imgs-80px/{color}_pawn.png')
        self.radius = 20
        self.has_moved = False
        
    def draw(self, screen, square_size, row, col):
        x = col * square_size + square_size // 2
        y = row * square_size + square_size // 2
        color = (0, 0, 0) if self.color == 'black' else (255, 255, 255)
        pygame.draw.circle(screen, color, (x, y), self.radius)
    
    def get_image(self):
        return self.image
    
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