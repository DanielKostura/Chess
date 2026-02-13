from __future__ import annotations
from tkinter import Tk, Canvas, Button, Label, Entry, Listbox
from tkinter import Event, StringVar, DISABLED, NORMAL, END
from os import path, listdir
from typing import Callable
from chess import Board
from abc import ABC
from gui.board_view import BoardView

import sach  # delete later

ScreenType = type[Menu | GameMenu | OpeningLearnerMenu]
BUTTON_HEIGHT = 3
BUTTON_WIDTH = 28

class ScreenManager:
    def __init__(self):
        self.current = None

    def show(self, screen_cls: ScreenType, *args):
        if self.current:
            self.current.cleanup()
        self.current = screen_cls(*args)


class BaseScreen:
    def __init__(self, window, canvas):
        self.window = window
        self.canvas = canvas
        self.widgets = []

        self.canvas.delete("all")

    def cleanup(self):
        for widget in self.widgets:
            widget.destroy()
        self.widgets.clear()
        self.canvas.delete("all")

    def create_button(self, text, command, x, y, h=3, w=28):
        btn = Button(self.canvas, text=text, command=command, height=h, width=w)
        btn.place(x=x, y=y)
        self.widgets.append(btn)
        return btn

    def create_label(self, text, x, y):
        lbl = Label(self.canvas, text=text)
        lbl.place(x=x, y=y)
        self.widgets.append(lbl)
        return lbl

    def create_entry(self, variable, x, y):
        etr = Entry(self.canvas, textvariable=variable)
        etr.place(x=x, y=y)
        self.widgets.append(etr)
        return etr

    def create_listbox(self, x, y, h, w):
        lb = Listbox(self.window)
        lb.place(x=x, y=y, height=h, width=w)
        self.widgets.append(lb)
        return lb


"""
class BaseMenu(ABC):  # abstract class
    def __init__(self, window: Tk, canvas: Canvas,
                 width: int, height: int) -> None:
        self.window: Tk = window
        self.canvas: Canvas = canvas
        self.width: int = width
        self.height: int = height
        self.widgets: list[Button | Label | Entry | Listbox] = []

        canvas.config(width=width, height=height, bg='white')
        window.title("Menu")

    def new_canvas(self, MenuClass: type[Menu | GameMenu | BotMenu | OpeningLearnerMenu]):
        self.cleanup()
        MenuClass(self.window, self.canvas)

    def create_button(self, text: str,
                      command: Callable[[], None], x: int, y: int,
                      height: int = BUTTON_HEIGHT,
                      width: int = BUTTON_WIDTH) -> Button:
        btn = Button(self.canvas, text=text, command=command,
                     height=height, width=width)
        btn.place(x=x, y=y)
        self.widgets.append(btn)
        return btn

    def create_label(self, text: str, x: int, y: int) -> Label:
        lbl = Label(self.canvas, text=text)
        lbl.place(x=x, y=y)
        self.widgets.append(lbl)
        return lbl

    def create_entry(self, entry: StringVar, x: int, y: int) -> Entry:
        self.filename = StringVar()
        etr = Entry(self.canvas, textvariable=entry,
                    font=('calibre', 10, 'normal'), bg="lightgrey")
        etr.place(x=x, y=y)
        self.widgets.append(etr)
        return etr

    def create_text(self, text: str, colour: str, x: int, y: int):
        self.canvas.create_text(x, y, text=text, fill=colour,
                                font=('Helvetica', '10', 'bold'))

    def create_scroll_list(self, selection_fun: Callable[[], None],
                           x: int, y: int, height: int, width: int) -> Listbox:
        scroll_list = Listbox(self.window, font=10, selectmode="browse")
        scroll_list.place(x=x, y=y, height=height, width=width)

        # It open openings
        openings_path = \
            path.join(path.dirname(path.dirname(__file__)), "openings")

        # Cut last .txt and it add it in scroll_list
        for file in listdir(openings_path):
            if file.endswith('.txt'):
                scroll_list.insert(END, file[:-4])

        scroll_list.bind('<Button-1>', selection_fun)
        self.widgets.append(scroll_list)
        return scroll_list

    def cleanup(self):
        self.canvas.delete("all")

        for widget in self.widgets:
            widget.destroy()
"""

class Menu(BaseScreen):
    def __init__(self, window: Tk, canvas: Canvas, manager: ScreenManager):
        super().__init__(window, canvas)

        self.manager = manager
        self.window.title("Menu")

        self._create_widgets()

    def _create_widgets(self) -> None:
        x = 60 * 8 + 40

        self.create_button(
            text="Hra s priateľom",
            command=lambda: self.manager.show("game_menu"),
            x=x, y=40
        )

        self.create_button(
            text="Hra proti počítaču",
            command=lambda: self.manager.show("bot_menu"),
            x=x, y=40+75
        )

        self.create_button(
            text="Precvičenie otvorení",
            command=lambda: self.manager.show("opening_menu"),
            x=x, y=40+75*2
        )

        self.create_button(
            text="Koniec",
            command=self.window.destroy,
            x=x, y=420
        )
        
    """def __init__(self, window: Tk, canvas: Canvas) -> None:
        super().__init__(window, canvas, 750, 60 * 8 + 20)

        # Menu buttons
        self.create_button("Hra s priateľom",
                           lambda: self.new_canvas(GameMenu),
                           60*8+2*20, 40)
        self.create_button("Hra proti počítaču",
                           lambda: self.new_canvas(BotMenu),
                           60*8+2*20, 40+75)
        self.create_button("Precvičenie otvorení",
                           lambda: self.new_canvas(OpeningLearnerMenu),
                           60*8+2*20, 40+75*2)
        self.create_button("Koniec",
                           lambda: self.window.destroy(),
                           60*8+2*20, 420)

        # Chessboard rendering"""


class GameMenu(BaseScreen):  # missing Game
    def __init__(self, window: Tk, canvas: Canvas) -> None:
        super().__init__(window, canvas, 750, 60 * 8 + 20)

        # Menu buttons
        self.create_button("1 + 0", lambda: self.play_game(60, 0),
                           60*8+2*20, 40)
        self.create_button("1 + 1", lambda: self.play_game(60, 1),
                           60*8+2*20, 40+75)
        self.create_button("10 + 0", lambda: self.play_game(10*60, 0),
                           60*8+2*20, 40+75*2)
        self.create_button("10 + 3", lambda: self.play_game(10*60, 3),
                           60*8+2*20, 40+75*3)
        self.create_button("Menu", lambda: self.new_canvas(Menu),
                           60*8+2*20, 420)

        # Chessboard rendering
        self.draw_board()

    def play_game(self, time: int, bonus: int) -> None:
        self.cleanup()
        Game(time, bonus)


class BotMenu(BaseScreen):  # empty
     def __init__(self, window: Tk, canvas: Canvas) -> None:
         super().__init__(window, canvas, 750, 60 * 8 + 20)


class OpeningLearnerMenu(BaseScreen):  # missing OpeningLearner, OpeningReviewer, OpeningCreator
    def __init__(self, window: Tk, canvas: Canvas) -> None:
        super().__init__(window, canvas, 750, 60 * 8 + 20)
        self.filename = StringVar()
        self.lerning = 0

        # OpeningLearnerMenu wigets
        self.create_label("Zadaj názov otvorenia:", 60*8+2*20+40, 40)
        self.etr = self.create_entry(self.filename, 60*8+2*20+30, 70)

        self.create_button("Vytvoriť nové otvorenie", self.new_opening,
                           60*8+2*20+18, 100, 2, 22)
        self.learing_b = self.create_button("Učenie", self.learn,
                                            60*8+2*20, self.height-110, 2, 12)
        self.learing_b.config(state=DISABLED)
        self.review_b = self.create_button("Precvičenie", self.review,
                                           60*8+7*20+10, self.height-110, 2, 12)
        self.update_b = self.create_button("Upraviť", self.update, 60*8+2*20,
                                           self.height-60, 2, 12)
        self.create_button("Menu", lambda: self.new_canvas(Menu), 60*8+7*20+10,
                           self.height-60, 2, 12)

        self.scroll_list = self.create_scroll_list(self.open_opening,
                                                   self.width-230, 155,
                                                   230, 204)

        # Chessboard rendering
        self.draw_board()

    def open_opening(self, action: Event) -> None:
        # Getting the index of the item you clicked on
        index = self.scroll_list.nearest(action.y)
        # Getting the text of the item you clicked on
        selected_item = self.scroll_list.get(index)

        if self.lerning == 0:
            self.select_mode(OpeningLearner, selected_item)
        elif self.lerning == 1:
            self.select_mode(OpeningReviewer, selected_item)
        elif self.lerning == 2:
            self.select_mode(OpeningCreator, selected_item)

    def new_opening(self) -> None:
        name = self.filename.get()

        if name != "":
            # Create/Clean File
            f = open(name + ".txt", "w")
            f.close()

            self.select_mode(OpeningCreator, name)
        else:
            self.create_text("Prve vložte názov otvorenia", "red",
                             self.width-20*2-88, 150)
            self.etr.config(bg="lightcoral")

    def select_mode(self, OpeningMode: type[OpeningLearner | OpeningReviewer | OpeningCreator],
                    filename: str) -> None:
        self.cleanup()
        OpeningMode(filename + ".txt")

    def learn(self) -> None:
        self.lerning = 0
        self.learing_b.config(state=DISABLED)
        self.review_b.config(state=NORMAL)
        self.update_b.config(state=NORMAL)

    def review(self) -> None:
        self.lerning = 1
        self.learing_b.config(state=NORMAL)
        self.review_b.config(state=DISABLED)
        self.update_b.config(state=NORMAL)

    def update(self) -> None:
        self.lerning = 2
        self.learing_b.config(state=NORMAL)
        self.review_b.config(state=NORMAL)
        self.update_b.config(state=DISABLED)
