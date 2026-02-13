from chess import WHITE, BLACK

from gui.screen_manager import ScreenManager
from gui.base_screen import BaseScreen
from gui.board_view import BoardView


class AiMenu(BaseScreen, BoardView):
    """
    AiMenu manages the appearance of the AI menu.
    """
    def __init__(self, manager: ScreenManager):
        BaseScreen.__init__(self, manager)
        BoardView.__init__(self, manager.canvas)

        self.draw_board()
        self._create_widgets()

    def _create_widgets(self) -> None:
        x = 60 * 8 + 20 * 2

        self.create_button(
            "Biely",
            lambda: self.manager.show_ai_game(WHITE),
            x, 40
        )
        self.create_button(
            "Čierny",
            lambda: self.manager.show_ai_game(BLACK),
            x, 40 + 75
        )
        self.create_button(
            "Náhodný výber",
            lambda: self.manager.show_ai_game(None),
            x, 40 + 75 * 2
        )

        self.create_button(
            "Menu",
            self.manager.show_menu,
            520, 420
        )
