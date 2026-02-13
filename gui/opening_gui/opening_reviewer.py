from typing import Optional
from chess import Board

from gui.base_screen import BaseScreen
from gui.screen_manager import ScreenManager
from logic.opening_logic.reviewer_manager import ReviewerManager
from ui_component.notation_panel import NotationPanel

class OpeningReviewer(BaseScreen, ReviewerManager):
    def __init__(self, manager: ScreenManager, file: str):
        BaseScreen.__init__(self, manager)

        self.next_btn = None
        ReviewerManager.__init__(
            self, manager.canvas,
            file, self.next_btn,
            self.manager.show_opening_menu
        )

        self._create_widgets()
        self.draw_board(self.board)

        self.canvas.bind(
            "<Button-1>",
            lambda action: self.on_click(action)
        )

    def _create_widgets(self) -> None:
        self.manager.canvas.create_text(
            self.manager.width - 120, 35,
            text=self.variant_name,
            font=('calibre', 15, 'bold')
        )

        self.note_list = self.create_listbox(
            self.manager.width - 200, 60,
            200, 157
        )
        self.set_listbox(NotationPanel(self.note_list))

        self.next_btn = self.create_button(
            "Ďalej", self.next_variant,
            self.manager.width - 200, 270,
            2, 21
        )
        self_hint_btn = self.create_button(
            "Nápoveda", self.show_next_move,
            self.manager.width - 200, 325,
            2, 21
        )
        self.restart_btn = self.create_button(
            "Resetovať šachovnicu", self.restart_board,
            self.manager.width - 200, 380,
            2, 21
        )
        self.menu_btn = self.create_button(
            "Menu", self.manager.show_opening_menu,
            self.manager.width - 200, 435,
            2, 21
        )

    def draw_board(self, board_logic: Optional[Board] = None) -> None:
        ReviewerManager.draw_board(self, board_logic)
        self.manager.canvas.create_text(
            self.manager.width - 120, 35,
            text=self.variant_name,
            font=('calibre', 15, 'bold')
            )
