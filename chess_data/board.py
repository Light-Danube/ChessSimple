import pygame
from chess_data.square import Square
from chess_data.pieces.pawn import Pawn
from chess_data.pieces.rook import Rook
from chess_data.pieces.queen import Queen
from chess_data.pieces.bishop import Bishop
from chess_data.pieces.knight import Knight
from chess_data.pieces.king import King

class Chessboard:
    def __init__(self, screen):
        self.screen = screen
        self.SQUARE_SIZE = 50
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.selected_piece = None
        self.valid_moves = []
        self.squares = self.generate_squares()

    def generate_squares(self):
        squares = []
        for y in range(8):
            for x in range(8):
                square = Square(x, y, self.SQUARE_SIZE, self.SQUARE_SIZE)
                squares.append(square)
        return squares

    def draw(self):
        for square in self.squares:
            square.draw(self.screen)

    def handle_click(self, position, player_color):
        row, col = position
        square = self.get_square_from_pos(position)

        if square.occupying_piece and square.occupying_piece.color == player_color:
            if square.occupying_piece == self.selected_piece:
                self.selected_piece = None
                self.valid_moves = []
            else:
                self.selected_piece = square.occupying_piece
                self.valid_moves = self.get_valid_moves(player_color)
        elif self.selected_piece:
            if square in self.valid_moves:
                self.move_piece(self.selected_piece, square)
                self.selected_piece = None
                self.valid_moves = []

    def move_piece(self, piece, target_square):
        current_square = self.get_square_from_piece(piece)

        if target_square in self.valid_moves:
            current_square.occupying_piece = None
            target_square.occupying_piece = piece
            piece.position = target_square.pos

    def get_valid_moves(self, player_color):
        valid_moves = []
        for square in self.squares:
            if square.occupying_piece and square.occupying_piece.color == player_color:
                piece_valid_moves = square.occupying_piece.get_valid_moves(self)
                valid_moves.extend([s for s in self.squares if s.pos in piece_valid_moves])
        return valid_moves

    def get_square_from_pos(self, position):
        for square in self.squares:
            if square.pos == position:
                return square

    def get_square_from_piece(self, piece):
        for square in self.squares:
            if square.occupying_piece == piece:
                return square
