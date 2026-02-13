from tkinter import Button, Label, Entry, Listbox, StringVar
from typing import Callable

from gui.screen_manager import ScreenManager
from gui.timer.timer_controller import TimerController
from gui.timer.timer_view import TimerView
from logic.timer import Timer

class BaseScreen:
    """
    BaseScreen manages widgets and their lifecycle.
    """
    def __init__(self, manager: ScreenManager) -> None:
        self.manager = manager
        self.window = manager.window
        self.canvas = manager.canvas
        self.widgets: list[Button | Label | Entry | Listbox] = []

        self.canvas.delete("all")

    def cleanup(self) -> None: 
        for widget in self.widgets:
            widget.destroy()
        self.widgets.clear()
        self.canvas.delete("all")

    def create_button(self, text: str, command: Callable[[], bool | None],
                      x: int, y: int, h: int = 3, w: int = 28) -> Button:
        btn = Button(self.canvas, text=text, command=command,
                     height=h, width=w)
        btn.place(x=x, y=y)
        self.widgets.append(btn)
        return btn

    def create_label(self, text: str, x: int, y: int) -> Label:
        lbl = Label(self.canvas, text=text)
        lbl.place(x=x, y=y)
        self.widgets.append(lbl)
        return lbl

    def create_entry(self, variable: StringVar,
                     x: int, y: int, w: int) -> Entry:
        etr = Entry(
            self.canvas, textvariable=variable,
            font=('calibre', 10, 'normal'), bg="lightgrey",
            width=w
        )
        etr.place(x=x, y=y)
        self.widgets.append(etr)
        return etr

    def create_listbox(self, x: int, y: int, h: int, w: int) -> Listbox:
        lb = Listbox(self.window, font='20', selectmode="browse")
        lb.place(x=x, y=y, height=h, width=w)
        self.widgets.append(lb)
        return lb
    
    def create_timer(self, sec: int, bonus: int,
                     on_timeout: Callable[[], None],
                     x: int, y: int) -> TimerController:
        timer_view = TimerView(self.canvas, x, y)
        timer = Timer(sec, bonus)
        timer_controller = TimerController(self.canvas, timer, timer_view, on_timeout)
        self.widgets.append(timer_view.get_label())
        return timer_controller
