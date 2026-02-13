from tkinter import Canvas, StringVar, Label
from typing import Optional

class TimerView:
    """
    The class responsible for the graphical representation of the timer.
    """
    def __init__(self, canvas: Canvas, x: int, y: int) -> None:
        self.canvas = canvas
        self.colour = "white"
        self.label_id: Optional[str] = None
        self.is_blinking: bool = False

        self.text = StringVar()
        self.label = Label(canvas, textvariable=self.text,
                           font=("Arial", 24))
        self.label.place(x=x, y=y)

    def _toggle(self) -> None:
        self.colour = "crimson" if self.colour == "white" else "white"
        self.label.config(bg=self.colour)
        self.label_id = self.label.after(500, self._toggle)

    def strat_blinking(self) -> None:
        if not self.is_blinking:
            self._toggle()
            self.is_blinking = True

    def stop_blinking(self) -> None:
        if self.is_blinking:
            assert self.label_id is not None, "Label ID is None while blinking"
            self.label.after_cancel(self.label_id)
            self.colour = "white"
            self.label.config(bg=self.colour)
            self.is_blinking = False

    def highlight_timeout(self) -> None:
        self.colour = "crimson"
        self.label.config(bg=self.colour)


    def update(self, value: str) -> None:
        self.text.set(value)

    def get_label(self) -> Label:
        return self.label
