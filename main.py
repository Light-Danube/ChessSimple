import pygame
from chess_data.board import Chessboard

# Initialize Pygame
pygame.init()

# Set up your screen
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
screen = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGHT)
pygame.display.set_caption('Chess Game')

# Create a Chessboard instance
chessboard = Chessboard(screen)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Handle user clicks here
            pass

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the chessboard and pieces
    chessboard.draw()

    # Update the display

# Quit Pygame
pygame.quit()
