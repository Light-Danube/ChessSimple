class Bishop:
    # ...
    def get_valid_moves(self, board):
        valid_moves = []
        row, col = self.position

        # Check diagonally (up-right)
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

        # Check diagonally (up-left)
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] is None:
                valid_moves.append((r, c))
            else:
                if board[r][c].color != self.color:
                    valid_moves.append((r, c))
                break
            r -= 1
            c -= 1

        # Check diagonally (down-right)
        r, c = row + 1, col + 1
        while r < 8 and c < 8:
            if board[r][c] is None:
                valid_moves.append((r, c))
            else:
                if board[r][c].color != self.color:
                    valid_moves.append((r, c))
                break
            r += 1
            c += 1

        # Check diagonally (down-left)
        r, c = row + 1, col - 1
        while r < 8 and c >= 0:
            if board[r][c] is None:
                valid_moves.append((r, c))
            else:
                if board[r][c].color != self.color:
                    valid_moves.append((r, c))
                break
            r += 1
            c -= 1

        return valid_moves
