import pygame
from chess_data.board import Chessboard
from chess_data.pieces.pawn import Pawn


# Initialize Pygame
pygame.init()

# Set up your screen
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
screen = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGHT)
pygame.display.set_caption('CG')

# Create a Chessboard instance
#chessboard = Chessboard(screen)

# Create black Pawns and add them to the board
for col in range(8):
    black_pawn = Pawn('black', [1, col])
    chessboard.board[1][col] = black_pawn

# Create white Pawns and add them to the board
for col in range(8):
    white_pawn = Pawn('white', [6, col])
    chessboard.board[6][col] = white_pawn


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle user clicks here
            pass

    # Draw the chessboard and pieces
    screen.fill((0, 0, 0))
    
    #chessboard.draw()
    #pygame.display.flip()

# Quit Pygame
pygame.quit()
