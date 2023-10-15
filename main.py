import pygame
from chess_data.board import Chessboard

# Initialize Pygame
pygame.init()

# Set up your screen
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('SimpleChess')

# Create a Chessboard instance
chessboard = Chessboard(screen)

# Main game loop
running = True
selected_piece = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button click
                # Get the clicked square
                mx, my = pygame.mouse.get_pos()
                cc = mx // chessboard.SQUARE_SIZE
                rr = my // chessboard.SQUARE_SIZE
                
                chessboard.handle_click((rr, cc), 'white')

    # Draw the chessboard and pieces
    screen.fill((0, 0, 0))
    chessboard.draw()
    pygame.display.flip()  # Update the display

# Quit Pygame
pygame.quit()

