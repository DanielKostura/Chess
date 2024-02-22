# https://python-chess.readthedocs.io/en/latest/
import chess

board = chess.Board()
#print(board.legal_moves)
#<LegalMoveGenerator at ... (Nh3, Nf3, Nc3, Na3, h3, g3, f3, e3, d3, c3, ...)>

#print(chess.Move.from_uci("g1f3") in board.legal_moves)

chess.Move.from_uci("a8a1") in board.legal_moves
#False

# kto je na tahu ? - print(board.turn)

board.push_san("e4")
#Move.from_uci('e2e4')
board.push_san("e5")
#Move.from_uci('e7e5')
board.push_san("Qh5")
#Move.from_uci('d1h5')
board.push_san("Nc6")
#Move.from_uci('b8c6')
board.push_san("Bc4")
#Move.from_uci('f1c4')
board.push_san("Nf6")
#Move.from_uci('g8f6')
board.push_san("Qxf7")
#Move.from_uci('h5f7')

print(board)

#print(board.is_checkmate())
#True  
