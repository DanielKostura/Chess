from chess import BLACK, WHITE, Board
from tkinter import Canvas, Event

from gui.board_view import BoardView
from logic.chess_rules import is_valid_uci_move, is_promotion_move


class GameController(BoardView):
    def __init__(self, canvas: Canvas, offset_x: int, offset_y: int) -> None:
        BoardView.__init__(self, canvas, offset_x, offset_y)

        self.board = Board()
        self.move = "...."

    def on_click(self, action: Event) -> bool:
        x, y = action.x, action.y

        SQUARE = 60
        if not (
            self.offset_x < x < self.offset_x + 8 * SQUARE and
            self.offset_y < y < self.offset_y + 8 * SQUARE
        ):
            return False

        file = chr(ord('a') + (x - self.offset_x) // SQUARE) if self.color == WHITE \
            else chr(ord('h') - (x - self.offset_x) // SQUARE)
        rank = str(8 - (y - self.offset_y) // SQUARE) if self.color == WHITE \
            else str(1 + (y - self.offset_y) // SQUARE)
        self.move = (self.move + file + rank)[2:]

        if not is_valid_uci_move(self.move, self.board):
            return False

        if is_promotion_move(self.board, self.move):
            self.move += 'q'  # Auto promote to queen

        self.board.push_uci(self.move)
        self.draw_board(self.board)

        if len(self.move) == 5:
            self.move = "...."
        return True

    def check_game_state(self) -> bool:
        result = None
        message = None

        if self.board.is_checkmate():
            winner = "Biely" if self.board.turn == BLACK else "Čierny"
            result = "VÝHRA"
            message = f"{winner} vyhral šachmatom"
        elif self.board.is_stalemate():
            result = "REMÍZA"
            message = "Patová situácia"
        elif self.board.is_insufficient_material():
            result = "REMÍZA"
            message = "Nedostatok materiálu"
        elif self.board.can_claim_threefold_repetition():
            result = "REMÍZA"
            message = "Opakovanie ťahov"

        if result and message:
            self.draw_result(result, message)
            return True
        return False

    def restart_board(self) -> None:
        self.board = Board()
        self.move = "...."
        self.draw_board(self.board)
