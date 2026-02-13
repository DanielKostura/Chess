from gui.screen_manager import ScreenManager
from gui.base_screen import BaseScreen
from gui.board_view import BoardView

class GameMenu(BaseScreen, BoardView):
    """
    GameMenu manages the appearance of the game menu.
    """
    def __init__(self, manager: ScreenManager):
        BaseScreen.__init__(self, manager)
        BoardView.__init__(self, manager.canvas)

        self.draw_board()
        self._create_widgets()

    def _create_widgets(self) -> None:
        x = 60 * 8 + 20 * 2

        self.create_button(
            "1 + 0",
            lambda: self.manager.show_start_game(60, 0),
            x, 40
        )

        self.create_button(
            "1 + 1",
            lambda: self.manager.show_start_game(60, 1),
            x, 40 + 75
        )

        self.create_button(
            "10 + 0",
            lambda: self.manager.show_start_game(10*60, 0),
            x, 40 + 75 * 2
        )

        self.create_button(
            "10 + 3",
            lambda: self.manager.show_start_game(10*60, 3),
            x, 40 + 75 * 3
        )

        self.create_button(
            "Menu",
            self.manager.show_menu,
            x, 420
        )