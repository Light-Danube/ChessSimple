class Rook:
    # ...
    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.position

        # Check vertically
        for r in range(row + 1, 8):
            if board[r][col] is None:
                valid_moves.append((r, col))
            else:
                if board[r][col].color != self.color:
                    valid_moves.append((r, col))
                break

        for r in range(row - 1, -1, -1):
            if board[r][col] is None:
                valid_moves.append((r, col))
            else:
                if board[r][col].color != self.color:
                    valid_moves.append((r, col))
                break

        # Check horizontally
        for c in range(col + 1, 8):
            if board[row][c] is None:
                valid_moves.append((row, c))
            else:
                if board[row][c].color != self.color:
                    valid_moves.append((row, c))
                break

        for c in range(col - 1, -1, -1):
            if board[row][c] is None:
                valid_moves.append((row, c))
            else:
                if board[row][c].color != self.color:
                    valid_moves.append((row, c))
                break

        return valid_moves
