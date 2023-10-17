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

# Define the initial player (white starts)
current_player = 'white'

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
                
                if current_player == 'white':
                    chessboard.handle_click((rr, cc), 'white')
                else:
                    chessboard.handle_click((rr, cc), 'black')

                # Switch to the next player's turn
                current_player = 'white' if current_player == 'black' else 'black'

    # Draw the chessboard and pieces
    screen.fill((0, 0, 0))
    chessboard.draw()
    pygame.display.flip()  # Update the display
    
    # Check for check and checkmate
    if chessboard.is_check('white'):
        print("White is in check!")
    if chessboard.is_check('black'):
        print("Black is in check!")
    if chessboard.is_checkmate('white'):
        print("Checkmate! Black wins!")
        running = False
    if chessboard.is_checkmate('black'):
        print("Checkmate! White wins!")
        running = False
    else:
        # Check if the black king is in check and display possible moves
        king_position = chessboard.get_king_position('black')
        if chessboard.is_check('black'):
            chessboard.display_possible_king_moves(king_position)

# Quit Pygame
pygame.quit()

