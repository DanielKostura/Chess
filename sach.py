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

def piece_move(x, y, fun):
        if 10 < x < 60*8 + 10 and 60 < y < 60*9:
            file = chr(ord('a') + (x - 10) // 60)
            rank = str(8 - (y - 60) // 60)

            print(Game.board)
            fun.position += file + rank
            fun.position = fun.position[2:]

            try:
                if chess.Move.from_uci(fun.position) in fun.board.legal_moves:
                    fun.board.push_san(fun.position)
                    draw_board(fun.canvas, True, 0, 50,
                               create_chess_array(fun.board))
            except:
                pass

            if fun.board.is_checkmate() == True:
                fun.canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                              fill="lightgrey", outline="black")
                fun.canvas.create_text((60 * 8 + 20)//2, 
                                         (60 * 8 + 20 + 100)//2,
                                         text="ŠACH MAT",
                                         font=('Helvetica','50','bold'))  
            elif fun.board.is_stalemate() == True:
                fun.canvas.create_rectangle(60, 60+60*3, 15+60*7, 60*6,
                                              fill="grey", outline="black")
                fun.canvas.create_text((60 * 8 + 20)//2-5, 
                                         (60 * 8 + 20 + 100)//2,
                                         text="REMÍZA",
                                         font=('Helvetica','50','bold'))
                fun.canvas.create_text((60 * 8 + 20)//2, 
                                         (60 * 8 + 20 + 100)//2+40,
                                         text="Patová situácia",
                                         font=('Helvetica','15','bold'))
            elif fun.board.is_insufficient_material() == True:
                fun.canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                              fill="lightgrey", outline="black")
                fun.canvas.create_text((60 * 8 + 20)//2-5, 
                                         (60 * 8 + 20 + 100)//2,
                                         text="REMÍZA",
                                         font=('Helvetica','50','bold'))
                fun.canvas.create_text((60 * 8 + 20)//2, 
                                         (60 * 8 + 20 + 100)//2+40,
                                         text="Nedostatok materiálu",
                                         font=('Helvetica','15','bold'))
            elif fun.board.can_claim_threefold_repetition() == True:
                fun.canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                              fill="lightgrey", outline="black")
                fun.canvas.create_text((60 * 8 + 20)//2, 
                                         (60 * 8 + 20 + 100)//2-5,
                                         text="REMÍZA",
                                         font=('Helvetica','50','bold'))
                fun.canvas.create_text((60 * 8 + 20)//2, 
                                         (60 * 8 + 20 + 100)//2+40,
                                         text="Opakovanie ťahou",
                                         font=('Helvetica','15','bold'))


class Menu:
    def __init__(self) -> None:
        # vytvorenie noveho okna
        self.window = tk.Tk()
        self.window.title("Menu")

        # vytvorenie noveho platna
        W = 750
        H = 60 * 8 + 20
        self.canvas = Canvas(width=W, height=H,bg='white')
        self.canvas.pack()

        # menu buttons
        Button(self.canvas, text = "Hra s priaťelom", command=self.game,
               height= 3, width=28).place(x = 60*8+2*20, y = 40)
        Button(self.canvas, text = "Precvičenie otvorení", command=self.openings,
               height= 3, width=28).place(x = 60*8+2*20, y = 40+75)
        Button(self.canvas, text = "Pravidlá", command=self.rules, height= 3,
               width=28).place(x = 60*8+2*20, y = 420)
        
        # vykreslenie sachovnice
        draw_board(self.canvas, False)

        self.canvas.mainloop()

    def openings(self):
        self.window.destroy()
        rules_window = Tk()  # Vytvořte nové okno
        rules_window.title('Šachové otvorenia')

        W = 500
        H = 500
        p = Canvas(width=W, height=H,bg='white')
        p.pack()

    def rules(self):
        self.window.destroy()
        rules_window = Tk()  # Vytvořte nové okno
        rules_window.title('Pravidlá šachu')

        W = 500
        H = 500
        p = Canvas(width=W, height=H,bg='white')
        p.pack()

        p.create_text(W//2, 30, text = "DDD", fill="black")
    
    def game(self):
        self.window.destroy()
        Game()


class Game:
    def __init__(self) -> None:
        # vytvorenie noveho okna
        self.window = tk.Tk()
        self.window.title('Hra s priteľom')

        # premenné pre funkciu on_click
        Game.position = "...."
        Game.board = chess.Board()

        # vytvorenie noveho platna
        W = 60 * 8 + 20
        H = 60 * 8 + 20 + 100
        self.canvas = Canvas(width=W, height=H, bg='white')
        self.canvas.pack()

        # vykreslenie sachovnice
        draw_board(self.canvas, False, 0, 50)

        # button START
        b = Button(self.canvas, text="START", command=self.game_start, height=2, width=20)
        b.place(x=10, y=H-50)

        self.canvas.mainloop()

    def game_start(self):
        draw_board(self.canvas, True, 0, 50, create_chess_array(Game.board))

        # button MENU
        Button(self.canvas, text="Menu", command=self.game_end,
               height=2, width=20).place(x=10, y=60*8+20+100-50)

        # urcovanie suradnic
        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, action):
        piece_move(action.x, action.y, Game)
        draw_board(self.canvas, True, 0, 50, create_chess_array(Game.board))

    def game_end(self):
        self.window.destroy()
        Menu()


Menu()