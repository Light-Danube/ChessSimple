import pygame
from chess_data.board import Chessboard

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Chess Game')

    # Initialize the Chessboard
    chessboard = Chessboard(screen)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row = pos[1] // chessboard.SQUARE_SIZE
                col = pos[0] // chessboard.SQUARE_SIZE
                chessboard.handle_click((row, col))

        # Draw the chessboard
        chessboard.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()