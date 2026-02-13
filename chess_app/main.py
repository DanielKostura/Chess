from tkinter import Tk, Canvas
from gui.screen_manager import ScreenManager

    
def main() -> None:
    window = Tk()
    canvas = Canvas(window, width=750, height=500, bg="white")
    canvas.pack()

    manager = ScreenManager(window, canvas, 750, 500)
    manager.show_menu()

    window.mainloop()


if __name__ == "__main__":
    main()
