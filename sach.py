from tkinter import *
import tkinter as tk
import typing
import chess
# pip install chess
# python -m pip install chess

def menu():
    menu.window = Tk()
    menu.window.title("Menu")

    W = 1000
    H = 80 * 8 + 20
    menu.canvas = Canvas(width=W, height=H,bg='white')
    menu.canvas.pack()

    buttons()
    draw_board(menu.canvas, False)
    menu.canvas.mainloop()

def draw_board(current_canvas: Tk, pieces: bool, bonus_x=0, bonus_y=0,
               chess_board: list[list[str]]=[[""]]):
    for row in range(8):
        for column in range(8):
            if (row + column) % 2 == 1:
                farba = "green"
            else:
                farba = "white"

            x = column*80+10+bonus_x
            y = row*80+10+bonus_y
            current_canvas.create_rectangle(x, y, x+80, y+80,
                                            fill=farba ,outline='black',width='5')
    
            if pieces == True:
                board = chess_board
                current_canvas.create_text(x+40, y+40, text=board[row][column],
                                           font=('Helvetica','50','bold'))

def create_chess_array(board):
    board_rows = []
    for i in reversed(range(8)):
        row = []
        for j in reversed(range(8)):
            current_piece = board.piece_at(chess.square(j, i))
            # empty squere
            current_piece = current_piece.symbol() if current_piece else ''

            # pawns
            if current_piece == "P":
                piece_symbol = "♟"
            elif current_piece == "p":
                piece_symbol = "♙"
            
            # rooks
            elif current_piece == "R":
                piece_symbol = "♜"
            elif current_piece == "r":
                piece_symbol = "♖"

            # Nights
            elif current_piece == "N":
                piece_symbol = "♞"
            elif current_piece == "n":
                piece_symbol = "♘"
            
            # Bishops
            elif current_piece == "B":
                piece_symbol = "♝"
            elif current_piece == "b":
                piece_symbol = "♗"
            
            # Queen
            elif current_piece == "Q":
                piece_symbol = "♛"
            elif current_piece == "q":
                piece_symbol = "♕"

            # Kings
            elif current_piece == "K":
                piece_symbol = "♚"
            elif current_piece == "k":
                piece_symbol = "♔"
            else:
                piece_symbol = current_piece
            
            row.append(piece_symbol)

        board_rows.append(row)
    
    return board_rows

# --------------------- button functions ---------------------
def blitz_start():
    draw_board(blitz.canvas, True, 0, 50, create_chess_array(chess.Board()))
    b = Button(blitz.canvas, text="Menu", command=blitz_end, height=2, width=20)
    b.place(x=10, y=80*8+20+100-50)

def blitz_end():
    blitz.window.destroy()
    menu()

def rapid_start():
    draw_board(rapid.canvas, True, 0, 50)
    b = Button(rapid.canvas, text="Menu", command=rapid_end, height=2, width=20)
    b.place(x=10, y=80*8+20+100-50)

def rapid_end():
    rapid.window.destroy()
    menu()
# --------------------- button functions ---------------------


# ----------------------- menu buttons -----------------------
def buttons():
    Button(menu.canvas, text = "Blitz", command=blitz, height= 3, width=30).place(x = 80*9, y = 100)
    Button(menu.canvas, text = "Rapid", command=rapid, height= 3, width=30).place(x = 80*9, y = 100+75)
    Button(menu.canvas, text = "Precvičenie otvorení", command=openings, height= 3, width=30).place(x = 80*9, y = 100+75*2)
    Button(menu.canvas, text = "Pravidlá", command=rules, height= 3, width=30).place(x = 80*9, y = 500)

def blitz():
    menu.window.destroy()

    blitz.window = tk.Tk()  # Vytvořte nové okno
    blitz.window.title('Blitz')

    W = 80 * 8 + 20
    H = 80 * 8 + 20 + 100
    blitz.canvas = Canvas(width=W, height=H, bg='white')
    blitz.canvas.pack()

    draw_board(blitz.canvas, False, 0, 50)
    b = Button(blitz.canvas, text="START", command=blitz_start, height=2, width=20)
    b.place(x=10, y=H-50)

    blitz.canvas.mainloop()
    
def rapid():
    menu.window.destroy()

    rapid.window = tk.Tk()  # Vytvořte nové okno
    rapid.window.title('Blitz')

    W = 80 * 8 + 20
    H = 80 * 8 + 20 + 100
    rapid.canvas = Canvas(width=W, height=H, bg='white')
    rapid.canvas.pack()

    draw_board(rapid.canvas, False, 0, 50)
    b = Button(rapid.canvas, text="START", command=rapid_start, height=2, width=20)
    b.place(x=10, y=H-50)

    rapid.canvas.mainloop()

def openings():
    menu.window.destroy()
    rules_window = Tk()  # Vytvořte nové okno
    rules_window.title('Pravidlá šachu')

    W = 500
    H = 500
    p = Canvas(width=W, height=H,bg='white')
    p.pack()

def rules():
    menu.window.destroy()
    rules_window = Tk()  # Vytvořte nové okno
    rules_window.title('Pravidlá šachu')

    W = 500
    H = 500
    p = Canvas(width=W, height=H,bg='white')
    p.pack()

    p.create_text(W//2, 30, text = "DDD", fill="black")
# ----------------------- menu buttons -----------------------

menu()