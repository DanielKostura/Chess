from tkinter import NORMAL, DISABLED
from chess import Board
from typing import Optional

from gui.base_screen import BaseScreen
from gui.screen_manager import ScreenManager
from ui_component.notation_panel import NotationPanel
from logic.opening_logic.learner_manager import LearnerManager

class OpeningLearner(BaseScreen, LearnerManager):
    def __init__(self, manager: ScreenManager, file: str) -> None:
        BaseScreen.__init__(self, manager)

        self.next_btn = None
        LearnerManager.__init__(
            self, manager.canvas,
            file, self.next_btn,
            self.manager.show_opening_menu
        )

        self._create_widgets()
        self.draw_board(self.board)
    
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

        self.start_btn = self.create_button(
            "Štart", self.start_learning,
            self.manager.width - 200, 270,
            2, 21
        )
        self.repeat_btn = self.create_button(
            "Zopakovať ťah", self.show_next_move,
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
        self.repeat_btn.config(state=DISABLED)

    def draw_board(self, board_logic: Optional[Board] = None) -> None:
        LearnerManager.draw_board(self, board_logic)
        self.manager.canvas.create_text(
            self.manager.width - 120, 35,
            text=self.variant_name,
            font=('calibre', 15, 'bold')
        )

    def start_learning(self) -> None:
        self.start_btn.destroy()
        self.widgets.remove(self.start_btn)

        self.next_btn = self.create_button(
            "Ďalej", self.next_variant,
            self.manager.width - 200, 270,
            2, 21
        )

        self.canvas.bind(
            "<Button-1>",
            lambda action: self.on_click(action)
        )

        self.canvas.after(500, self.show_next_move)
        self.repeat_btn.config(state=NORMAL)
