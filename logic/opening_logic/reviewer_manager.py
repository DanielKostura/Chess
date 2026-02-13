from tkinter import Canvas, Button, Event
from typing import Optional, Callable
from chess import Board
from logic.opening_logic.opening_coach import OpeningCoach

class ReviewerManager(OpeningCoach):
    def __init__(self, canvas: Canvas, file: str, next_btn: Optional[Button],
                 menu_fun: Callable[[], None]):
        OpeningCoach.__init__(self, canvas, file, next_btn, menu_fun)
        self.wrong_moves: list[int] = [0 for _ in range(len(self.moves) + 1)]
        self.redo_index: int = 0

    def _handle_wrong_move(self) -> None:
        self.wrong_moves[self.curr_move] = 3
        OpeningCoach._handle_wrong_move(self)
    
    def _handle_correct_move(self, move_uci: str) -> None:
        if self.is_correcting:
            if self.wrong_moves[self.curr_move] > 0:
                self.wrong_moves[self.curr_move] -= 1
        OpeningCoach._handle_correct_move(self, move_uci)

    def _process_next_correction(self) -> None:
        if not any(self.wrong_moves):
            self.is_correcting = False
            OpeningCoach.next_variant(self)
            return

        while self.wrong_moves[self.redo_index] == 0:
            if self.redo_index == 0:
                self.board = Board()
                self.notation = []

            if self.redo_index < len(self.moves):
                self.board.push_uci(self.moves[self.redo_index])
                self.notation.append(self.moves[self.redo_index])

            self.redo_index = (self.redo_index + 1) % len(self.wrong_moves)

            if self.redo_index == len(self.moves):
                self.is_end = True

        self.curr_move = self.redo_index
        self.redo_index = (self.redo_index + 1) % len(self.wrong_moves)

        assert self.listbox is not None, "Listbox is not initialized"
        self.listbox.update(self.notation)
        self.draw_board(self.board)

    def start_correcting(self) -> None:
        self.is_correcting = True
        self.board = Board()
        self.redo_index = 0
        self.curr_move = 0
        self.is_end = False
        self.notation = []
        self._process_next_correction()

    def next_variant(self) -> bool:
        if not self.is_end and not self.is_correcting:
            self.wrong_moves[self.curr_move] = 3
        
        if self.is_end and self.is_correcting and self.wrong_moves[self.curr_move] > 0:
            self.wrong_moves[self.curr_move] -= 1

        if any(self.wrong_moves) and self.is_end:
            self.start_correcting()
            return False

        self.is_correcting = False
        return OpeningCoach.next_variant(self)

    def on_click(self, action: Event) -> bool:
        result = OpeningCoach.on_click(self, action)
        if self.is_correcting and result:
            self.canvas.after(300, self._process_next_correction)
        return result
    
    def restart_board(self) -> None:
        OpeningCoach.restart_board(self)
        self.wrong_moves = [0 for _ in range(len(self.moves) + 1)]
        self.redo_index = 0
        self.is_correcting = False