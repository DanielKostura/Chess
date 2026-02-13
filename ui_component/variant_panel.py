from tkinter import Event, Listbox

from ui_component.listbox_manager import ListboxManager
from logic.file_operations import open_file, write_file

class VariantPanel(ListboxManager):
    def __init__(self, listbox: Listbox, file: str):
        ListboxManager.__init__(self, listbox)
        self.file = file

    def update(self) -> None:
        self.reset_listbox()
        lines = open_file(f"openings/{self.file}")
        self.fill_listbox(
            [line[:line.index(":")] for line in lines]
        )

    def delete_variant(self, action: Event) -> None:
        selected_variant_name = self.selection_listbox(action)

        file_path = f"openings/{self.file}"
        lines = open_file(file_path)
        new_lines = \
            [line for line in lines \
                  if not line.startswith(f"{selected_variant_name}:")]

        write_file(file_path, new_lines)
        self.update()

    def handle_selection(self, action: Event) -> list[str]:
        selected_variant_name = \
            self.selection_listbox(action)
        lines = open_file(f"openings/{self.file}")

        for line in lines:
            name, moves_str = line.split(":", 1)

            if selected_variant_name == name:
                self.notation = moves_str.strip().split()
                return self.notation
        assert False, "Variant not found"