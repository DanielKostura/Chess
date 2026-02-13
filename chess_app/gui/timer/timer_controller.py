from tkinter import Canvas
from typing import Optional, Callable
from logic.timer import Timer
from gui.timer.timer_view import TimerView

class TimerController:
    """
    TimerController class that manages the logic and display of the timer.
    Connects Timer (logic) to TimerView (graphics).
    """
    def __init__(self, canvas: Canvas, timer: Timer, view: TimerView,
                 on_timeout: Callable[[], None]) -> None:
        self.canvas = canvas
        self.timer = timer
        self.view = view
        self.on_timeout = on_timeout
        self._timer_id: Optional[str] = None
        self.ticking = False

        # Write time to previously empty timer
        self.view.update(self.timer.format_time())

    def _ticking(self) -> None:
        if self.timer.tick():
            if self.timer.seconds <= 10:
                self.view.strat_blinking()
            self.view.update(self.timer.format_time())
            self._timer_id = self.view.get_label().after(1000, self._ticking)
        else:
            self.view.stop_blinking()
            self.view.highlight_timeout()
            self.on_timeout()

    def start(self) -> None:
        assert not self.ticking, "Timer is already running"
        self.ticking = True
        self._ticking()

    def stop(self) -> None:
        if self._timer_id:
            self.ticking = False
            self.view.get_label().after_cancel(self._timer_id)
            self.view.stop_blinking()
            self.timer.add_bonus()
            self.view.update(self.timer.format_time())
