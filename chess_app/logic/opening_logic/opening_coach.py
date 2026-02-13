from __future__ import annotations  # NotationPanel
from chess import Board
from tkinter import Canvas, Button, Event
from typing import Optional, Callable, TYPE_CHECKING, Optional

from gui.game_controller import GameController
from logic.file_operations import parse_opening_variants
from gui.visual_efects import blink

if TYPE_CHECKING:
    from ui_component.notation_panel import NotationPanel


class OpeningCoach(GameController):
    def __init__(self, canvas: Canvas, file: str, next_btn: Optional[Button],
                 menu_fun: Callable[[], None]):
        GameController.__init__(self, canvas, 10, 10)

        self.file: str = file
        self.next_btn: Optional[Button] = next_btn
        self.menu_fun: Callable[[], None] = menu_fun

        self.curr_variant: int = 0
        self.curr_move: int = 0

        self.preview_after_id: Optional[str] = None
        self.preview_move: Optional[str] = None

        self.is_end: bool = False
        self.is_correcting: bool = False  # from reviewer manager
        self.notation: list[str] = []
        self.listbox: Optional[NotationPanel] = None

        self.variants = parse_opening_variants(self.file)
        self.variant_name, self.moves = self.variants[self.curr_variant]

    def _undo_preview_move(self) -> None:
        self.preview_after_id = None

        if self.board.move_stack:
            self.board.pop()
            self.draw_board(self.board)

    def show_next_move(self) -> None:
        if self.preview_after_id is not None:  # move is in show proces
            return

        if self.is_end:
            assert self.next_btn is not None, "next_btn is not initialized"
            blink(self.next_btn, "green")
            return

        self.preview_move = self.moves[self.curr_move]

        self.board.push_uci(self.preview_move)
        self.draw_board(self.board)

        self.preview_after_id = self.canvas.after(
            1000, self._undo_preview_move
        )

    def next_variant(self) -> bool:
        if not self.is_end:
            assert self.next_btn is not None, "next_btn is not initialized"
            blink(self.next_btn, "red")
            return False

        self.curr_variant += 1
        if self.curr_variant >= len(self.variants):
            self.canvas.after(300, self.menu_fun)
            return False

        self.board = Board()
        self.notation = []
    
        self.variant_name, self.moves = self.variants[self.curr_variant]

        assert self.listbox is not None, "Listbox is not initialized"
        self.listbox.update(self.notation)
        self.draw_board(self.board)

        self.curr_move = 0
        self.is_end = False
        return True

    def restart_board(self) -> None:
        if self.preview_after_id is not None:
            self.canvas.after_cancel(self.preview_after_id)
            self.preview_after_id = None

        GameController.restart_board(self)

        self.curr_move = 0
        self.notation = []
        assert self.listbox is not None, "Listbox is not initialized"
        self.listbox.update(self.notation)

    def _handle_wrong_move(self) -> None:
        self.board.pop()
        self.canvas.after(300, lambda: self.draw_board(self.board))
    
    def _handle_correct_move(self, move_uci: str) -> None:
        assert self.listbox is not None, "Listbox is not initialized"
        self.notation.append(move_uci)
        self.listbox.update(self.notation)

        if self.curr_move == len(self.moves) - 1:
            self.is_end = True
            
        self.curr_move += 1

    def on_click(self, action: Event) -> bool:
        if self.preview_after_id is not None:
            return False

        expected_board = self.board.copy()
        if not GameController.on_click(self, action):
            return False

        if self.is_end and not self.is_correcting:  # must be after previous if
            self._handle_wrong_move()
            return False

        correct_uci = self.moves[self.curr_move]
        expected_board.push_uci(correct_uci)

        self.draw_board(self.board)

        if self.board != expected_board:
            self._handle_wrong_move()
            return False

        self._handle_correct_move(correct_uci)
        return True

    def set_listbox(self, listbox: NotationPanel) -> None:
        self.listbox = listbox
