from tkinter import Listbox, Event, END


class ListboxManager:
    def __init__(self, listbox: Listbox) -> None:
        self.listbox = listbox

    def fill_listbox(self, items: list[str]) -> None:
        self.listbox.delete(0, END)
        for item in items:
            self.listbox.insert(END, item)

    def selection_listbox(self, action: Event) -> str:
        # Getting the index of the item you clicked on
        index = int(self.listbox.nearest(action.y))
        # Getting the text of the item you clicked on
        return str(self.listbox.get(index))

    def reset_listbox(self) -> None:
        self.listbox.delete(0, END)
