import tkinter as tk
import chess

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chess Game")
        self.canvas = tk.Canvas(self, width=480, height=480, bg="white")
        self.canvas.pack()
        self.position = ""
        self.turn = 0

        # Bind mouse click event to the canvas
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        x = event.x
        y = event.y
        
        # Check if the click is within the chessboard area
        if 10 < x < 490 and 50 < y < 490:
            file = chr(ord('a') + (x - 10) // 60)
            rank = str(8 - (y - 50) // 60)
            new_position = file + rank
            
            try:
                if chess.Move.from_uci(new_position) in self.board.legal_moves:
                    self.position += new_position
                    self.position = self.position[-2:]  # Keep only the last two characters

                    if self.correcting_mistakes:
                        self.board.push_san(self.position)
                        self.after(1000, self.handle_correct_move)
                    else:
                        self.board.push_san(self.position)
                        self.after(1000, self.handle_wrong_move)
                    
            except ValueError:
                # Invalid move
                pass
    
    def handle_correct_move(self):
        # Perform actions after a correct move with a delay
        draw_board(True, create_chess_array(self.board), 0, 50)
        self.title()
        self.turn += 1
        self.correct()

    def handle_wrong_move(self):
        # Perform actions after a wrong move with a delay
        draw_board(True, create_chess_array(self.board), 0, 50)
        self.title()
        self.board.pop()
        draw_board(True, create_chess_array(self.board), 0, 50)
        self.fixed[self.n] += 1
        self.correct()

        if self.fixed[self.n] == 3:
            self.fixed.pop(self.n)
            self.mistakes.pop(self.n)

if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
