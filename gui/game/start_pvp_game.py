from gui.screen_manager import ScreenManager
from gui.base_screen import BaseScreen
from gui.board_view import BoardView

class StartGame(BaseScreen, BoardView):
    """
    StartGame manages the appearance of the start menu.
    """
    def __init__(self, manager: ScreenManager, time: int, bonus: int) -> None:
        BaseScreen.__init__(self, manager)
        BoardView.__init__(self, manager.canvas, 10, 60)

        self.manager = manager
        self.time = time
        self.bonus = bonus

        self.draw_board()
        self._create_widgets()

    def _create_widgets(self) -> None:
        self.create_button(
            "Štart",
            lambda: self.manager.show_chess_game(self.time, self.bonus),
            self.manager.width - 160 - 15,
            self.manager.height - 50,
            2, 20
        )