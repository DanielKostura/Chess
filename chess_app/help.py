from chess import Board, WHITE, BLACK, square_rank, square_file
from math import inf

def _evaluate_board(board: Board) -> float:
    if board.is_checkmate():
        return inf if board.turn == BLACK else -inf

    piece_values = {
        "P": 100, "N": 320, "B": 330,
        "R": 500, "Q": 900,"K": 0, # White pieces

        "p": -100, "n": -320, "b": -330,
        "r": -500, "q": -900, "k": 0  # Black pieces
    }

    # Material score
    score = 0
    for piece in board.piece_map().values():
        score += piece_values[piece.symbol()]

    # King safety
    if board.is_check():
        score += 50 if board.turn == BLACK else -50
    
    # Positional advantage can be added here
    score += board.legal_moves.count() * (1 if board.turn == WHITE else -1)
    return score

board = Board()
board.push_san("e4")
board.push_san("e5")
board.push_san("Bc4")
board.push_san("Nc6")
board.push_san("Qh5")
board.push_san("Nf6")
board.push_san("a3")
board.push_san("Bc5")
board.push_san("a4")
board.push_san("O-O")
print(board.is_castling(board.pop()))
#print(_evaluate_board(board))