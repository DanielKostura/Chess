from __future__ import annotations # NotationPanel
from chess import Board, Color, Move, WHITE, BLACK
from chess import square_file, square_rank, square_mirror
from chess import PAWN, KNIGHT, BISHOP, ROOK, QUEEN, KING
from typing import Optional, TYPE_CHECKING
from tkinter import Canvas
from random import getrandbits
from math import inf
from enum import Enum

from gui.game_controller import GameController

if TYPE_CHECKING:
    from ui_component.notation_panel import NotationPanel


class Type(Enum):
    MAX = True
    MIN = False

class Node:
    def __init__(self, move: Move, type: Type):
        self.move: Move = move
        self.type = type  # "MAX" or "MIN"
        self.childs: list[Node] = [] 
        self.value: float = 0.0

PIECE_VALUES = {
    PAWN: 100,
    KNIGHT: 320,
    BISHOP: 330,
    ROOK: 500,
    QUEEN: 900,
    KING: 0
}

KNIGHT_PST = [
    -50,-40,-30,-30,-30,-30,-40,-50,
    -40,-20,  0,  0,  0,  0,-20,-40,
    -30,  0, 10, 15, 15, 10,  0,-30,
    -30,  5, 15, 20, 20, 15,  5,-30,
    -30,  0, 15, 20, 20, 15,  0,-30,
    -30,  5, 10, 15, 15, 10,  5,-30,
    -40,-20,  0,  5,  5,  0,-20,-40,
    -50,-40,-30,-30,-30,-30,-40,-50,
]

class AiManager(GameController):
    def __init__(self, canvas: Canvas, color: Optional[Color] = None):
        GameController.__init__(self, canvas, 10, 10)

        self.color: Color = \
            color if color is not None else (WHITE if bool(getrandbits(1)) else BLACK)
        self.ai_color: Color = BLACK if self.color == WHITE else WHITE
        if self.color == BLACK:
            self._make_ai_move()

        BOARD_SIZE = 60 * 8
        self.center_x = (BOARD_SIZE + self.offset_x) // 2
        self.center_y = (BOARD_SIZE + self.offset_y) // 2

        self.listbox: Optional[NotationPanel] = None
        self.notation: list[str] = []

    def _is_draw(self, board: Board) -> bool:
        return board.is_stalemate() or \
            board.can_claim_threefold_repetition() or \
            board.can_claim_fifty_moves() or \
            board.is_insufficient_material()

    def _generate_game_tree(self, board: Board, depth: int, type: Type) -> Node:
        node = Node(None, type)

        if depth == 0:
            node.value = self._evaluate_board(board)
            return node

        if board.is_checkmate():
            node.value = -inf if board.turn == WHITE else inf
            return node

        if self._is_draw(board):
            node.value = 0
            return node

        for move in board.legal_moves:
            board.push(move)
            child = self._generate_game_tree(
                board, depth - 1,
                Type.MIN if type == Type.MAX else Type.MAX
            )
            child.move = move
            node.childs.append(child)
            board.pop()

        return node

    def _get_center_bias(self, square: int) -> float:
        file = square_file(square) # 0-7
        rank = square_rank(square) # 0-7
        # Gauss function: exp( -((x-3.5)^2 + (y-3.5)^2) / (2 * sigma^2) )
        dist_sq = (file - 3.5)**2 + (rank - 3.5)**2
        return 5 * (2.718 ** (-dist_sq / 10.0))

    def _evaluate_castling(self, board: Board) -> float:
        bonus = 0

        for move in reversed(board.move_stack):
            if move.uci() == "e1g1" or move.uci() == "e1c1" or \
               move.uci() == "e8g8" or move.uci() == "e8c8":
                if board.color_at(move.to_square) == WHITE:
                    return 150
                else:
                    return -150

        # Biely
        if board.has_castling_rights(WHITE):
            bonus += 50
        # Čierny
        if board.has_castling_rights(BLACK):
            bonus -= 50
        return bonus

    def _evaluate_board(self, board: Board) -> float:
        score = 0
        # Material score
        for piece_type, value in PIECE_VALUES.items():
            for square in board.pieces(piece_type, WHITE):
                score += value
                if piece_type != KING:  # king wants to be safe, not in center
                    score += self._get_center_bias(square) * 5

            for square in board.pieces(piece_type, BLACK):
                score -= value
                if piece_type != KING:
                    score -= self._get_center_bias(square) * 5

        # King safety
        if board.is_check():
            score += -20 if board.turn == WHITE else 20
        
        score += self._evaluate_castling(board)

        return score

    def _alphabeta(self, node: Node, alpha: float, beta: float) -> float:
        if not node.childs:
            return node.value

        if node.type == Type.MAX:
            value = -inf
            for child in node.childs:
                child.value = self._alphabeta(child, alpha, beta)
                value = max(value, child.value)
                if value >= beta:
                    break
                alpha = max(alpha, value)
            return value
        else:
            value = inf
            for child in node.childs:
                child.value = self._alphabeta(child, alpha, beta)
                value = min(value, child.value)
                if value <= alpha:
                    break
            beta = min(beta, value)
        return value
    
    def _make_ai_move(self) -> None:
        root = self._generate_game_tree(
            self.board.copy(), 3,
            Type.MAX if self.ai_color == WHITE else Type.MIN
        )
        best_value = self._alphabeta(root, -inf, inf)

        best_move = None
        for child in root.childs:
            if child.value == best_value:
                best_move = child.move
                break

        assert best_move is not None, "AI could not find a valid move"
        self.notation.append(best_move.uci())
        self.board.push(best_move)
    
        self.draw_board(self.board)
        self.check_game_state()

    def on_click(self, action) -> bool:
        if GameController.on_click(self, action):
            self.notation.append(self.move)
            assert self.listbox is not None
            self.listbox.update(self.notation)

            if self.check_game_state():
                return True

            # wait a bit because board needs to render first
            self.canvas.after(10, self._make_ai_move)
            return True
        return False

    def set_listbox(self, listbox: NotationPanel) -> None:
        self.listbox = listbox
