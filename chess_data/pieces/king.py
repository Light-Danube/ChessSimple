class King:
    # ...
    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.position

        moves = [
            (row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
            (row, col - 1),                     (row, col + 1),
            (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
        ]

        for r, c in moves:
            if 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] is None or board[r][c].color != self.color:
                    valid_moves.append((r, c))

        return valid_moves
