from __future__ import annotations  # bacause of BaseScreen in _show
from typing import TYPE_CHECKING, Optional, Callable
from tkinter import Tk, Canvas

if TYPE_CHECKING:
    from gui.base_screen import BaseScreen


class ScreenManager:
    """
    ScreenManager manages what is displayed on the screen.
    """
    def __init__(self, window: Tk, canvas: Canvas,
                 width: int, height: int) -> None:
        self.window = window
        self.canvas = canvas
        self.width = width
        self.height = height

        self.current: Optional[BaseScreen] = None

    def _show(self, screen_factory: Callable[[], BaseScreen]) -> None:
        if self.current is not None:
            self.current.cleanup()

        self.current = screen_factory()

    def _wider_screen(self) -> None:
        self.width = 750
        self.height = 500
        self.canvas.config(width=self.width, height=self.height)

    def _higher_screen(self) -> None:
        self.width = 60 * 8 + 20
        self.height = 60 * 8 + 20 + 100
        self.canvas.config(width=self.width, height=self.height)


    def show_menu(self) -> None:
        self.window.title('Menu')
        self._wider_screen()
        from gui.menus.menu import Menu
        self._show(lambda: Menu(self))


    def show_game_menu(self) -> None:
        self.window.title('Menu')
        self._wider_screen()
        from gui.menus.game_menu import GameMenu
        self._show(lambda: GameMenu(self))

    def show_ai_menu(self) -> None:
        self.window.title('Menu')
        self._wider_screen()
        from gui.menus.ai_menu import AiMenu
        self._show(lambda: AiMenu(self))

    def show_opening_menu(self) -> None:
        self.window.title('Menu')
        self._wider_screen()
        from gui.menus.opening_menu import OpeningMenu
        self._show(lambda: OpeningMenu(self))


    def show_start_game(self, time: int, bonus: int) -> None:
        self.window.title('Hra s priteľom')
        self._higher_screen()
        from gui.game.start_pvp_game import StartGame
        self._show(lambda: StartGame(self, time, bonus))

    def show_chess_game(self, time: int, bonus: int) -> None:
        self.window.title('Hra s priteľom')
        self._higher_screen()
        from gui.game.pvp_game import ChessGame
        self._show(lambda: ChessGame(self, time, bonus))


    def show_ai_game(self, color: Optional[bool]) -> None:
        self.window.title('Hra proti počitaču')
        self._wider_screen()
        from gui.game.ai_game import AiGame
        self._show(lambda: AiGame(self, color))


    def show_opening_creator(self, file_name: str) -> None:
        self.window.title('Vytváranie otvorenia')
        self._wider_screen()
        from gui.opening_gui.opening_creator import OpeningCreator
        self._show(lambda: OpeningCreator(self, file_name + ".txt"))
    
    def show_opening_learner(self, file_name: str) -> None:
        self.window.title('Učenie otvorenia')
        self._wider_screen()
        from gui.opening_gui.opening_learner import OpeningLearner
        self._show(lambda: OpeningLearner(self, file_name + ".txt"))

    def show_opening_reviewer(self, file_name: str) -> None:
        self.window.title('Precvičenie otvorenia')
        self._wider_screen()
        from gui.opening_gui.opening_reviewer import OpeningReviewer
        self._show(lambda: OpeningReviewer(self, file_name + ".txt"))
