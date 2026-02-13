from tkinter import StringVar, Listbox, Event, NORMAL, DISABLED
from typing import Optional
from chess import Board

from gui.base_screen import BaseScreen
from gui.screen_manager import ScreenManager
from logic.opening_logic.creator_manager import CreatorManager

from ui_component.variant_panel import VariantPanel
from ui_component.notation_panel import NotationPanel


class OpeningCreator(BaseScreen, CreatorManager):
    """
    OpeningCreator manages the appearance of the creator menu.
    """
    def __init__(self, manager: ScreenManager, file: str) -> None:
        BaseScreen.__init__(self, manager)

        self.name_variant = StringVar()
        self.note_list: Optional[Listbox] = None
        self.variant_list: Optional[Listbox] = None

        self._create_widgets()

        CreatorManager.__init__(
            self, self.canvas, file,
            self.back_btn, self.forward_btn, self.delete_btn, self.etr,
            self.update_note_list, self.update_variant_list
        )

        self.draw_board(self.board)

        self.canvas.bind(
            "<Button-1>",
            lambda action: self.on_click(action)
        )

    def _create_widgets(self) -> None:
        self.note_list = self.create_listbox(
            self.manager.width - 200, 40,
            190, 157
        )
        self.notation_panel = NotationPanel(self.note_list)

        self.etr = self.create_entry(
            self.name_variant,
            self.manager.width - 200, 243,
            15
        )

        self.note_btn = self.create_button(
            "Zápis", self._show_note_list,
            self.manager.width - 200, 18,
            1, 5
        )
        self.variant_btn = self.create_button(
            "Varianty", self._show_variant_list,
            self.manager.width - 156, 18,
            1, 6
        )
        self.save_btn = self.create_button(
            "Uložiť", self.save_variant,
            self.manager.width - 88, 239,
            1, 5 
        )
        self.menu_btn = self.create_button(
            "Menu", self.manager.show_opening_menu,
            self.manager.width - 200, 260 + 10,
            2, 21
        )
        self.restart_btn = self.create_button(
            "Resetovať šachovnicu", self.restart_board,
            self.manager.width - 200, 315 + 10,
            2, 21
        )
        self.delete_btn = self.create_button(
            "Vymaž", self.delete_move,
            self.manager.width - 200, 370 + 10,
            2, 21
        )
        self.back_btn = self.create_button(
            "<", self.back_move,
            self.manager.width - 200, 425 + 10,
            2, 7
        )
        self.forward_btn = self.create_button(
            ">", self.forward_move,
            self.manager.width - 102, 425 + 10,
            2, 7
        )
        self.note_btn.config(state=DISABLED)
        self.delete_btn.config(state=DISABLED)
        self.back_btn.config(state=DISABLED)
        self.forward_btn.config(state=DISABLED)


    def _show_note_list(self) -> None:
        if self.variant_list is None:
            return

        self.variant_list.destroy()
        self.variant_list = None

        self.note_list = self.create_listbox(
            self.manager.width - 200, 40,
            190, 157
        )
        self.notation_panel = NotationPanel(self.note_list)
        self.update_note_list()

        self.note_btn.config(state=DISABLED)
        self.variant_btn.config(state=NORMAL)

    def _show_variant_list(self) -> None:
        if self.note_list is None:
            return

        self.note_list.destroy()
        self.note_list = None

        self.variant_list = self.create_listbox(
            self.manager.width - 200, 40,
            190, 157
        )
        self.variant_panel: VariantPanel = VariantPanel(self.variant_list, self.file)
        self.update_variant_list()
        self.variant_list.bind('<Button-1>', self._handle_variant_selection)
        self.variant_list.bind('<Button-3>', self.variant_panel.delete_variant)

        self.note_btn.config(state=NORMAL)
        self.variant_btn.config(state=DISABLED)


    def _handle_variant_selection(self, action: Event) -> None:
        self.notation = self.variant_panel.handle_selection(action)

        self.board = Board()
        for move in self.notation:
            self.board.push_uci(move)
        self.draw_board(self.board)

        self.putback = 0
        self.delete_btn.config(state=NORMAL)
        self.back_btn.config(state=NORMAL)
        self.forward_btn.config(state=DISABLED)
    
    def update_note_list(self) -> None:
        if self.note_list is None:
            self._show_note_list()
        self.notation_panel.update(self.notation)

    def update_variant_list(self) -> None:
        if self.variant_list is None:
            self._show_variant_list()
        self.variant_panel.update()
