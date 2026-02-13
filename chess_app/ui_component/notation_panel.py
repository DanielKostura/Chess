from tkinter import Listbox

from ui_component.listbox_manager import ListboxManager


class NotationPanel(ListboxManager):
    def __init__(self, listbox: Listbox):
        ListboxManager.__init__(self, listbox)

    def update(self, notation: list[str]) -> None:
        self.reset_listbox()
        items: list[str] = []
        for i in range(0, len(notation), 2):
            move_number = (i // 2) + 1
            white_move = notation[i]
            
            if i + 1 < len(notation):  # black move exist
                black_move = notation[i+1]
                line = f"{move_number}. {white_move:<7} {black_move}"
            else:
                line = f"{move_number}. {white_move}"
            
            items.append(line)
        self.fill_listbox(items)