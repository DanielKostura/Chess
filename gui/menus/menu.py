from gui.screen_manager import ScreenManager
from gui.base_screen import BaseScreen
from gui.board_view import BoardView

class Menu(BaseScreen, BoardView):
    """
    Menu manages the appearance of the menu.
    """
    def __init__(self, manager: ScreenManager) -> None:
        BaseScreen.__init__(self, manager)
        BoardView.__init__(self, manager.canvas)

        self.draw_board()
        self._create_widgets()

    def _create_widgets(self) -> None:
        x = 60 * 8 + 40

        self.create_button(
            "Hra s priateľom",
            self.manager.show_game_menu,
            x, 40
        )

        self.create_button(
            "Hra proti počítaču",
            self.manager.show_ai_menu,
            x, 40 + 75
        )

        self.create_button(
            "Precvičenie otvorení",
            self.manager.show_opening_menu,
            x, 40 + 75 * 2
        )

        self.create_button(
            "Koniec",
            self.window.destroy,
            x, 420
        )
