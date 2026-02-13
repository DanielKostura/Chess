from chess import Board, Color
from typing import Optional

from gui.screen_manager import ScreenManager
from gui.base_screen import BaseScreen
from logic.ai_manager import AiManager
from ui_component.notation_panel import NotationPanel

class AiGame(BaseScreen, AiManager):
    def __init__(self, manager: ScreenManager, color: Optional[Color]):
        BaseScreen.__init__(self, manager)
        AiManager.__init__(self, manager.canvas, color)

        self.draw_board(self.board)
        self._create_widgets()

        self.manager.canvas.bind(
            "<Button-1>",
            lambda action: self.on_click(action)
        )

    def _create_widgets(self) -> None:
        self.note_list = self.create_listbox(
            self.manager.width - 200, 60,
            200, 157
        )
        self.set_listbox(NotationPanel(self.note_list))

        self.menu_btn = self.create_button(
            "Menu", self.manager.show_ai_menu,
            self.manager.width - 200, 435,
            2, 21
        )
    
    def draw_board(self, board_logic: Optional[Board] = None) -> None:
        AiManager.draw_board(self, board_logic)
        self.manager.canvas.create_text(
            self.manager.width - 120, 35,
            text="Danko`s AI Game",
            font=('calibre', 15, 'bold')
            )