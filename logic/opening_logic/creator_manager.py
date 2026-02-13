from tkinter import Canvas, Event, Button, Entry, NORMAL, DISABLED, END
from typing import Callable

from gui.game_controller import GameController
from logic.file_operations import append_file

class CreatorManager(GameController):
    def __init__(self, canvas: Canvas, file: str,
                 back_btn: Button, forward_btn: Button, delete_btn: Button, etr: Entry,
                 update_note_list:Callable[[], None],
                 update_variant_list: Callable[[], None]) -> None:
        GameController.__init__(self, canvas, 10, 10)

        self.file = file
        self.update_note_list = update_note_list
        self.update_variant_list = update_variant_list
        self.back_btn = back_btn
        self.forward_btn = forward_btn
        self.delete_btn = delete_btn

        self.variant = 0
        self.putback = 0
        self.etr = etr
        self.notation: list[str] = []

    def on_click(self, action: Event) -> bool:
        if not GameController.on_click(self, action):
            return False

        self.notation.append(self.move)

        self.update_note_list()
        self.back_btn.config(state=NORMAL)
        self.delete_btn.config(state=NORMAL)
        return True

    def save_variant(self) -> None:
        var_name = self.etr.get()

        if var_name == "":
            self.etr.config(bg="lightcoral")
            return

        line = var_name + ":" + " ".join(self.notation) + "\n"
        append_file("openings/" + self.file, line)

        self.etr.delete(0, END)
        self.etr.config(bg="white")
        self.update_variant_list()

    def delete_move(self) -> None:
        if len(self.notation) <= 0:
            assert False, "No moves to delete"

        if self.putback > 0:
            for move in self.notation[-self.putback:]:
                self.board.push_uci(move)
            self.putback = 0

        self.notation.pop()
        self.board.pop()

        self.draw_board(self.board)
        self.update_note_list()

        if len(self.notation) == 0:
            self.delete_btn.config(state=DISABLED)
    
    def back_move(self) -> None:
        if self.putback >= len(self.notation):
            assert False, "No moves to go back to"

        self.putback += 1
        self.board.pop()
        self.draw_board(self.board)
        self.forward_btn.config(state=NORMAL)

        if self.putback == len(self.notation):
            self.back_btn.config(state=DISABLED)

    def forward_move(self) -> None:
        if self.putback <= 0:
            assert False, "No moves to go forward to"

        self.board.push_uci(self.notation[-self.putback])
        self.putback -= 1
        self.draw_board(self.board)
        self.back_btn.config(state=NORMAL)

        if self.putback == 0:
            self.forward_btn.config(state=DISABLED)

    def restart_board(self) -> None:
        GameController.restart_board(self)
        self.putback = 0
        self.notation = []

        self.back_btn.config(state=DISABLED)
        self.forward_btn.config(state=DISABLED)
        self.delete_btn.config(state=DISABLED)

        self.update_note_list()
