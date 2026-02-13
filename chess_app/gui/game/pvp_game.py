from chess import Board

from gui.screen_manager import ScreenManager
from gui.base_screen import BaseScreen
from logic.match_manager import MatchManager

class ChessGame(BaseScreen, MatchManager):
    def __init__(self, manager: ScreenManager, time: int, bonus: int) -> None:
        BaseScreen.__init__(self, manager)

        self.manager = manager
        self.time = time
        self.bonus = bonus

        self.board = Board()
        self._create_widgets()

        MatchManager.__init__(
            self,
            self.manager.canvas,
            self.white_timer,
            self.black_timer
        )

        self.draw_board(self.board)

        self.manager.canvas.bind(
            "<Button-1>",
            lambda action: self.on_click(action)
        )

    def _create_widgets(self) -> None:
        self.create_button(
            "Menu",
            self.manager.show_menu,
            self.manager.width - 160 - 15,
            self.manager.height - 50,
            2, 20
        )

        self.black_timer = self.create_timer(
            self.time,
            self.bonus,
            self.check_timeout,
            10 + 15, 10
        )

        self.white_timer = self.create_timer(
            self.time,
            self.bonus,
            self.check_timeout,
            10 + 15, self.manager.height - 50
        )
        self.white_timer.start()
        