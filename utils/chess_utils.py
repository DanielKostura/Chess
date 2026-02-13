from chess import Board, square

def create_chess_array(board: Board, reverse: bool = False) -> list[list[str]]:
    piece_map = {
        "p": "♟", "P": "♙",
        "r": "♜", "R": "♖",
        "n": "♞", "N": "♘",
        "b": "♝", "B": "♗",
        "q": "♛", "Q": "♕",
        "k": "♚", "K": "♔",
        "": ""
    }

    board_rows: list[list[str]] = []
    for y in reversed(range(8)):
        row: list[str] = []
        for x in reversed(range(8)):
            # Coordinates to squqre_idx = y * 8 + x
            square_idx: int = square(x, 7 - y) if reverse else square(7 - x, y)
            piece = board.piece_at(square_idx)

            symbol = piece.symbol() if piece else ""
            row.append(piece_map.get(symbol, symbol))

        board_rows.append(row)
    return board_rows
