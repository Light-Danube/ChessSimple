import pygame
import sys
from chess_data.board import Chessboard

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chess Game')

# Initialize the chessboard
chessboard = Chessboard(screen)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // chessboard.SQUARE_SIZE, x // chessboard.SQUARE_SIZE
            chessboard.handle_click((row, col))

    chessboard.draw()  # Draw the chessboard
    pygame.display.flip()

