import pygame
from chess_data.board import Chessboard
from chess_data.pieces.pawn import Pawn


# Initialize Pygame
pygame.init()

# Set up your screen
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
screen = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGHT)
pygame.display.set_caption('Chess Game')

# Create a Chessboard instance
chessboard = Chessboard(screen)

# Create black Pawns and add them to the board
chessboard.board[1][0] = Pawn('black', (1, 0))

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
    
    chessboard.draw()
    pygame.display.update()

# Quit Pygame
pygame.quit()
