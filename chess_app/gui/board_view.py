from tkinter import Canvas
from chess import Board, WHITE, Color
from typing import Optional
from utils.chess_utils import create_chess_array


class BoardView:
    """
    BoardView exclusively draws the board and 
    that's why they are separated from BaseScreen.
    """
    def __init__(self, canvas: Canvas,
                 offset_x: int = 10, offset_y: int = 10) -> None:
        self.canvas: Canvas = canvas
        self.color: Color = WHITE

        self.offset_x: int = offset_x
        self.offset_y: int = offset_y
        self.center_x: int = (60 * 8 + 20) // 2
        self.center_y: int = (60 * 8 + 20 + 100) // 2

    def draw_board(self, board_logic: Optional[Board] = None) -> None:

        SQUARE_SIZE = 60
        HALF_SQUARE = SQUARE_SIZE // 2

        self.canvas.delete("all")

        board_display = create_chess_array(board_logic) if board_logic else None

        for row in range(8):
            for col in range(8):
                x1 = col * SQUARE_SIZE + self.offset_x
                y1 = row * SQUARE_SIZE + self.offset_y
                x2, y2 = x1 + SQUARE_SIZE, y1 + SQUARE_SIZE

                color: str = "green" if (row + col) % 2 == 1 else "white"
                self.canvas.create_rectangle(
                    x1, y1, x2, y2, 
                    fill=color, outline='black', width=5
                )

                if board_display:
                    piece = board_display[row][col] \
                        if self.color == WHITE else board_display[7 - row][7 - col]
                    if piece:
                        self.canvas.create_text(
                            x1 + HALF_SQUARE, y1 + HALF_SQUARE,
                            text=piece, 
                            font=('Helvetica', 50, 'bold')
                        )

    def draw_result(self, title: str, subtitle: str) -> None:
        BG_WIDTH = 200
        BG_HEIGHT = 80

        self.canvas.create_rectangle(
            self.center_x - BG_WIDTH, self.center_y - BG_HEIGHT,
            self.center_x + BG_WIDTH, self.center_y + BG_HEIGHT,
            fill="lightgrey", outline="black", width=2
        )

        self.canvas.create_text(
            self.center_x, self.center_y - 5,
            text=title,
            font=('Helvetica', 50, 'bold')
        )
        self.canvas.create_text(
            self.center_x, self.center_y + 40,
            text=subtitle,
            font=('Helvetica', 15, 'bold')
        )
