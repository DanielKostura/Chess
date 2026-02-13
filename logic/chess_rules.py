from chess import parse_square, Board, Move, Color, SQUARES, PAWN


def is_enough_material(player: Color, board: Board) -> bool:
    test_board = board.copy()
    player_piece = 0
    opponent_piece = 0

    for square in SQUARES:
        piece = test_board.piece_at(square)
        if piece and piece.color != player:
            test_board.remove_piece_at(square)
            opponent_piece += 1
        elif piece and piece.color == player:
            player_piece += 1

    return not test_board.is_insufficient_material() or \
        (player_piece >= 2 and opponent_piece >= 3)  # possible check-mate in corner


def is_valid_uci_move(move_uci: str, board: Board) -> bool:
    try:
        move = Move.from_uci(move_uci)
        if move in board.legal_moves:
            return True

        promotion_move = Move.from_uci(move_uci + 'q')
        return promotion_move in board.legal_moves
    except:
        return False

def is_promotion_move(board: Board, move_uci: str) -> bool:
    assert len(move_uci) == 4, f"Invalid UCI move format: {move_uci}"
    from_square = parse_square(move_uci[:2])
    piece = board.piece_at(from_square)
    if piece is None:
        return False
    return piece.piece_type == PAWN and (move_uci[3] == '8' or move_uci[3] == '1')  
