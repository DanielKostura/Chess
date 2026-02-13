from tkinter import StringVar, Event, DISABLED, NORMAL
from typing import Optional
from enum import Enum

from gui.screen_manager import ScreenManager
from gui.base_screen import BaseScreen
from gui.board_view import BoardView
from ui_component.listbox_manager import ListboxManager
from logic.file_operations import open_directory, only_txt_files, write_file, delete_file, open_file

class Mode(Enum):
    LEARN = 0
    REVIEW = 1
    CREATOR = 2


class OpeningMenu(BaseScreen, BoardView):
    """
    OpeningMenu manages the appearance of the opening menu.
    """
    def __init__(self, manager: ScreenManager) -> None:
        BaseScreen.__init__(self, manager)
        BoardView.__init__(self, manager.canvas)

        self.file_name = StringVar()
        self.mode = Mode.LEARN

        self.draw_board()
        self._create_widgets()
        self._learn()

        self.listbox_manager = ListboxManager(self.listbox)
        txt_items = only_txt_files(open_directory("openings"))
        self.listbox_manager.fill_listbox(txt_items)
        self.listbox.bind('<Button-1>', self._handle_menu_selection)
        self.listbox.bind('<Button-3>', self._delete_in_listbox)

    def _create_widgets(self) -> None:
        x = 60 * 8 + 20 * 2

        self.lbl = self.create_label("Zadaj názov otvorenia:", x + 40, 40)
        self.etr = self.create_entry(self.file_name, x + 30, 70, 20)
        self.listbox = self.create_listbox(
            self.manager.width - 230, 155,
            230, 204
        )

        self.create_btn = self.create_button(
            "Vytvoriť nové otvorenie",
            self._new_opening,
            x + 18, 95, 2, 22
        )
        self.learn_btn = self.create_button(
            "Učenie",
            self._learn,
            x, self.manager.height - 110, 2, 12
        )
        self.review_btn = self.create_button(
            "Precvičenie",
            self._review,
            x + 5 * 20 + 10, self.manager.height - 110, 2, 12
        )
        self.update_btn = self.create_button(
            "Upraviť",
            self._update,
            x, self.manager.height - 60, 2, 12
        )
        self.create_button(
            "Menu",
            self.manager.show_menu,
            x + 5 * 20 + 10, self.manager.height - 60, 2, 12
        )

    def _handle_menu_selection(self, action: Event) -> None:
        selected_item = self.listbox_manager.selection_listbox(action)
        if not selected_item:
            return

        content = open_file(f"openings/{selected_item}.txt")

        if self.mode == Mode.CREATOR:
            self.manager.show_opening_creator(selected_item)
        elif content == []:  # empty file
            self.canvas.delete("all")
            self.draw_board()

            self.canvas.create_text(
                self.manager.width - 20 * 2 - 88, 145,
                text="Súbor je prázdny",
                font=('Helvetica', 10, 'bold'), fill="red"
            )
        elif self.mode == Mode.LEARN:
            self.manager.show_opening_learner(selected_item)
        elif self.mode == Mode.REVIEW:
            self.manager.show_opening_reviewer(selected_item)
        else:
            assert False, "Unhandled mode in opening menu"

    def _delete_in_listbox(self, action: Event) -> None:
        selected_file_name = \
            self.listbox_manager.selection_listbox(action)
        if not selected_file_name:
            return

        delete_file("openings/" + selected_file_name + ".txt")

        txt_items = only_txt_files(open_directory("openings"))
        self.listbox_manager.fill_listbox(txt_items)

    def _new_opening(self) -> None:
        file_name_str = self.file_name.get()
        message: Optional[str] = None

        if file_name_str == "":
            message = "Musíte prve zadať názov otvorenia"
        elif len(file_name_str) >= 22:
            message = "Príliš dlhý názov otvorenia"
        elif file_name_str in only_txt_files(open_directory("openings")):
            message = "Názov otvorenia už exituje"
        else:
            write_file("openings/" + file_name_str + ".txt", [])
            self.manager.show_opening_creator(file_name_str)

        if message:
            self.canvas.delete("all")
            self.draw_board()

            self.canvas.create_text(
                self.manager.width - 20 * 2 - 88, 145, text=message,
                font=('Helvetica', 10, 'bold'), fill="red"
            )
            self.etr.config(bg="lightcoral")

    def _learn(self) -> None:
        self.mode = Mode.LEARN
        self.learn_btn.config(state=DISABLED)
        self.review_btn.config(state=NORMAL)
        self.update_btn.config(state=NORMAL)

    def _review(self) -> None:
        self.mode = Mode.REVIEW
        self.learn_btn.config(state=NORMAL)
        self.review_btn.config(state=DISABLED)
        self.update_btn.config(state=NORMAL)

    def _update(self) -> None:
        self.mode = Mode.CREATOR
        self.learn_btn.config(state=NORMAL)
        self.review_btn.config(state=NORMAL)
        self.update_btn.config(state=DISABLED)
