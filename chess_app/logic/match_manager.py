from chess import WHITE, BLACK
from tkinter import Canvas, Event

from gui.timer.timer_controller import TimerController
from gui.game_controller import GameController
from logic.chess_rules import is_enough_material

class MatchManager(GameController):
    def __init__(self, canvas: Canvas,
                 white_timer: TimerController, black_timer: TimerController):
        GameController.__init__(self, canvas, 10, 60)

        self.white_timer = white_timer
        self.black_timer = black_timer
        self.board.turn = WHITE

    def _stop_game(self) -> None:
        self.white_timer.stop()
        self.black_timer.stop()

    def check_game_state(self) -> bool:
        if GameController.check_game_state(self):
            self._stop_game()
            return True
        return False

    def check_timeout(self) -> None:
        result = None
        message = None

        if self.black_timer.timer.seconds == 0:
            if is_enough_material(WHITE, self.board):
                result = "VÝHRA"
                message = "Biely vyhral na nedostatok času"
            else:
                result = "REMÍZA"
                message = "Nedostatok materiálu"
        elif self.white_timer.timer.seconds == 0:
            if is_enough_material(BLACK, self.board):
                result = "VÝHRA"
                message = "Čierny vyhral na nedostatok času"
            else:
                result = "REMÍZA"
                message = "Nedostatok materiálu"

        if result and message:
            self._stop_game()
            self.draw_result(result, message)
    
    def on_click(self, action: Event) -> bool:
        if not (
            self.white_timer.timer.seconds > 0 and
            self.black_timer.timer.seconds > 0):
            return False

        if not GameController.on_click(self, action):
            return False

        if self.board.turn == WHITE:
            self.white_timer.start()
            self.black_timer.stop()
        else:
            self.black_timer.start()
            self.white_timer.stop()

        self.check_game_state()
        return True
    
