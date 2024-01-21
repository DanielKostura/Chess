import chess

def create_board_peases(board):
    board_rows = []
    for i in reversed(range(8)):
        row = []
        for j in reversed(range(8)):
            current_piece = board.piece_at(chess.square(j, i))
            # empty squere
            current_piece = current_piece.symbol() if current_piece else ''

            # pawns
            if current_piece == "P":
                piece_symbol = "♟"
            elif current_piece == "p":
                piece_symbol = "♙"
            
            # rooks
            elif current_piece == "R":
                piece_symbol = "♜"
            elif current_piece == "r":
                piece_symbol = "♖"

            # Nights
            elif current_piece == "N":
                piece_symbol = "♞"
            elif current_piece == "n":
                piece_symbol = "♘"
            
            # Bishops
            elif current_piece == "B":
                piece_symbol = "♝"
            elif current_piece == "b":
                piece_symbol = "♗"
            
            # Queen
            elif current_piece == "Q":
                piece_symbol = "♛"
            elif current_piece == "q":
                piece_symbol = "♕"

            # Kings
            elif current_piece == "K":
                piece_symbol = "♚"
            elif current_piece == "k":
                piece_symbol = "♔"
            else:
                piece_symbol = current_piece
            
            row.append(piece_symbol)

        board_rows.append(row)
    
    return board_rows

# Create a chess board
chess_board = chess.Board()
chess_board.push_san("e4")
# Store the board as a list of lists of strings
board_matrix = create_board_peases(chess_board)

# Print the initial board
print(board_matrix)

"""
import chess

board = chess.Board()
print(board.piece_at(chess.square(0, 0)))
"""