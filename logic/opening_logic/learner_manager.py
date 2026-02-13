from tkinter import Canvas, Button, Event
from typing import Optional, Callable

from logic.opening_logic.opening_coach import OpeningCoach


class LearnerManager(OpeningCoach):
    def __init__(self, canvas: Canvas, file: str, next_btn: Optional[Button],
                 menu_fun: Callable[[], None]):
        OpeningCoach.__init__(self, canvas, file, next_btn, menu_fun)

    def restart_board(self) -> None:
        OpeningCoach.restart_board(self)
        self.canvas.after(300, self.show_next_move)

    def next_variant(self) -> bool:
        if not OpeningCoach.next_variant(self):
            return False
        self.canvas.after(300, self.show_next_move)
        return True

    def on_click(self, action: Event) -> bool:
        if not OpeningCoach.on_click(self, action):
            return False
        self.canvas.after(300, self.show_next_move)
        return True