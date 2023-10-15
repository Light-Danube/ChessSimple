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
        self.castled = False
    
    def move_castle(self, new_position, board, rook_class):
        row, col = self.pos
        new_row, new_col = new_position

        # Check if the target position is a valid move
        if new_position in self.get_valid_moves(board):
        # Check for castling move
            if new_row == row and abs(new_col - col) == 2:
                # Determine the rook's position based on the direction of castling
                if new_col > col:
                    rook = board[row][7]
                    rook_new_position = (new_row, new_col - 1)
                else:
                    rook = board[row][0]
                    rook_new_position = (new_row, new_col + 1)

                # Check if the rook is eligible for castling
                if isinstance(rook, rook_class) and not rook.has_moved:
                    # Perform castling
                    board[row][col] = None
                    board[new_row][new_col] = self
                    self.pos = new_position
                    self.has_moved = True
                    self.castled = True

                    board[rook.pos[0]][rook.pos[1]] = None
                    board[rook_new_position[0]][rook_new_position[1]] = rook
                    rook.pos = rook_new_position
                    rook.has_moved = True
                else:
                    # Invalid castling
                    print("Invalid castling.")
            else:
                target_piece = board[new_row][new_col]

                if target_piece is not None and target_piece.color != self.color:
                    board[new_row][new_col] = None

                board[row][col] = None
                board[new_row][new_col] = self
                self.pos = new_position
                self.has_moved = True
        else:
            print("Invalid move.")
    
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
        row, col = self.pos

        moves = [
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1),                     (row, col + 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
        ]

        for r, c in moves:
            if 0 <= r < 8 and 0 <= c < 8:
                target_piece = board[r][c]

                # Check if the target square is empty or has an enemy piece
                if target_piece is None or target_piece.color != self.color:
                    valid_moves.append((r, c))

        # Check for castling moves
        if not self.has_moved:
        # Kingside castling
            if col < 6 and all(board[row][col + i] is None for i in range(1, 3)):
                valid_moves.append((row, col + 2))

            # Queenside castling
            if col > 1 and all(board[row][col - i] is None for i in range(1, 4)):
                valid_moves.append((row, col - 2))

        return valid_moves
