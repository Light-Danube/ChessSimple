class Queen:
    # ...
    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.position

        # Horizontal and Vertical
        for r in range(8):
            if r != row:
                if board[r][col] is None or board[r][col].color != self.color:
                    valid_moves.append((r, col))

        for c in range(8):
            if c != col:
                if board[row][c] is None or board[row][c].color != self.color:
                    valid_moves.append((row, c))

        # Diagonal (up-right)
        r, c = row - 1, col + 1
        while r >= 0 and c < 8:
            if board[r][c] is None:
                valid_moves.append((r, c))
            else:
                if board[r][c].color != self.color:
                    valid_moves.append((r, c))
                break
            r -= 1
            c += 1

        # Continue with the logic for other diagonal directions.

        return valid_moves
