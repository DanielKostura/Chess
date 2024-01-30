import tkinter as tk

class Chessboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Šachovnica")
        self.board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        self.draw_board()

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "black"
                label = tk.Label(self.master, text=self.board[i][j], width=5, height=2, bg=color)
                label.grid(row=i, column=j)
                label.bind("<Button-1>", lambda event, row=i, col=j: self.on_click(row, col))

    def on_click(self, row, col):
        print(f"Clicked on {chr(col + 97)}{8 - row}")

if __name__ == "__main__":
    root = tk.Tk()
    chessboard = Chessboard(root)
    root.mainloop()

