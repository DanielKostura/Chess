from tkinter import *
import tkinter as tk
# import typing
import chess
# pip install chess
# python -m pip install chess

def draw_board(current_canvas: Tk, pieces: bool, bonus_x=0, bonus_y=0,
               chess_board: list[list[str]]=[[""]]):
    for row in range(8):
        for column in range(8):
            if (row + column) % 2 == 1:
                farba = "green"
            else:
                farba = "white"

            x = column*60+10+bonus_x
            y = row*60+10+bonus_y
            current_canvas.create_rectangle(x, y, x+60, y+60,
                                            fill=farba ,outline='black',width='5')
    
            if pieces == True:
                board = chess_board
                current_canvas.create_text(x+30, y+30, text=board[row][column],
                                           font=('Helvetica','50','bold'))

def create_chess_array(board):
    board_rows = []
    for i in reversed(range(8)):
        row = []
        for j in reversed(range(8)):
            current_piece = board.piece_at(chess.square(7-j, i))
            # empty squere
            current_piece = current_piece.symbol() if current_piece else ''

            # pawns
            if current_piece == "p":
                piece_symbol = "♟"
            elif current_piece == "P":
                piece_symbol = "♙"
            
            # rooks
            elif current_piece == "r":
                piece_symbol = "♜"
            elif current_piece == "R":
                piece_symbol = "♖"

            # Nights
            elif current_piece == "n":
                piece_symbol = "♞"
            elif current_piece == "N":
                piece_symbol = "♘"
            
            # Bishops
            elif current_piece == "b":
                piece_symbol = "♝"
            elif current_piece == "B":
                piece_symbol = "♗"
            
            # Queen
            elif current_piece == "q":
                piece_symbol = "♛"
            elif current_piece == "Q":
                piece_symbol = "♕"

            # Kings
            elif current_piece == "k":
                piece_symbol = "♚"
            elif current_piece == "K":
                piece_symbol = "♔"
            else:
                piece_symbol = current_piece
            
            row.append(piece_symbol)

        board_rows.append(row)
    return board_rows

def on_click(action):
        x = action.x
        y = action.y

        if 10 < x < 60*8 + 10 and 60 < y < 60*9:
            file = chr(ord('a') + (x - 10) // 60)
            rank = str(8 - (y - 60) // 60)
            game.position += file + rank
            game.position = game.position[2:]
            try:
                if chess.Move.from_uci(game.position) in game.board.legal_moves:
                    game.board.push_san(game.position)
                    draw_board(game.canvas, True, 0, 50,
                               create_chess_array(game.board))
            except:
                pass

            if game.board.is_checkmate() == True:
                game.canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                              fill="lightgrey", outline="black")
                game.canvas.create_text((60 * 8 + 20)//2, 
                                         (60 * 8 + 20 + 100)//2,
                                         text="ŠACH MAT",
                                         font=('Helvetica','50','bold'))  
            elif game.board.is_stalemate() == True:
                game.canvas.create_rectangle(60, 60+60*3, 15+60*7, 60*6,
                                              fill="grey", outline="black")
                game.canvas.create_text((60 * 8 + 20)//2-5, 
                                         (60 * 8 + 20 + 100)//2,
                                         text="REMÍZA",
                                         font=('Helvetica','50','bold'))
                game.canvas.create_text((60 * 8 + 20)//2, 
                                         (60 * 8 + 20 + 100)//2+40,
                                         text="Patová situácia",
                                         font=('Helvetica','15','bold'))
            elif game.board.is_insufficient_material() == True:
                game.canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                              fill="lightgrey", outline="black")
                game.canvas.create_text((60 * 8 + 20)//2-5, 
                                         (60 * 8 + 20 + 100)//2,
                                         text="REMÍZA",
                                         font=('Helvetica','50','bold'))
                game.canvas.create_text((60 * 8 + 20)//2, 
                                         (60 * 8 + 20 + 100)//2+40,
                                         text="Nedostatok materiálu",
                                         font=('Helvetica','15','bold'))
            elif game.board.can_claim_threefold_repetition() == True:
                game.canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                              fill="lightgrey", outline="black")
                game.canvas.create_text((60 * 8 + 20)//2, 
                                         (60 * 8 + 20 + 100)//2-5,
                                         text="REMÍZA",
                                         font=('Helvetica','50','bold'))
                game.canvas.create_text((60 * 8 + 20)//2, 
                                         (60 * 8 + 20 + 100)//2+40,
                                         text="Opakovanie ťahou",
                                         font=('Helvetica','15','bold'))


# --------------------- game functions ---------------------
def game():
    menu.window.destroy()

    # vytvorenie noveho okna
    game.window = tk.Tk()
    game.window.title('Hra s priteľom')

    W = 60 * 8 + 20
    H = 60 * 8 + 20 + 100
    game.canvas = Canvas(width=W, height=H, bg='white')
    game.canvas.pack()

    # vykreslenie sachovnice
    draw_board(game.canvas, False, 0, 50)

    # button START
    b = Button(game.canvas, text="START", command=game_start, height=2, width=20)
    b.place(x=10, y=H-50)

    game.canvas.mainloop()

def game_start():
    game.board = chess.Board()
    draw_board(game.canvas, True, 0, 50, create_chess_array(game.board))

    # button MENU
    b = Button(game.canvas, text="Menu", command=game_end, height=2, width=20)
    b.place(x=10, y=60*8+20+100-50)

    # urcovanie suradnic
    game.canvas.bind("<Button-1>", on_click)
    game.position = "...."

def game_end():
    game.window.destroy()
    menu()
# --------------------- game functions ---------------------


def menu():
    menu.window = Tk()
    menu.window.title("Menu")

    W = 750
    H = 60 * 8 + 20
    menu.canvas = Canvas(width=W, height=H,bg='white')
    menu.canvas.pack()

    menu_buttons()
    draw_board(menu.canvas, False)
    menu.canvas.mainloop()

# ----------------------- menu buttons -----------------------
def menu_buttons():
    Button(menu.canvas, text = "Hra s priaťelom", command=game_menu, height= 3, width=28).place(x = 60*8+2*20, y = 40)
    Button(menu.canvas, text = "Precvičenie otvorení", command=openings, height= 3, width=28).place(x = 60*8+2*20, y = 40+75)
    # Button(menu.canvas, text = "Rapid", command=rapid, height= 3, width=28).place(x = 60*8+2*20, y = 40+75*2)
    Button(menu.canvas, text = "Pravidlá", command=rules, height= 3, width=28).place(x = 60*8+2*20, y = 420)

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

def game_menu():
    game()

menu()