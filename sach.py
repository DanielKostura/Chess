from tkinter import *
import tkinter as tk
# import typing
import chess
# pip install chess
# python -m pip install chess

def draw_board(current_canvas: Tk, pieces: bool, bonus_x=0, bonus_y=0,
               board: list[list[str]]=[[""]]):
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

            fun.position += file + rank
            fun.position = fun.position[2:]

            try:
                if chess.Move.from_uci(fun.position) in fun.board.legal_moves:
                    # urobenie tahu
                    fun.board.push_san(fun.position)

                    # zapinanie hodiniek
                    if Game.board.turn == chess.WHITE:
                        white_timer.start_timer()
                        black_timer.stop_timer()
                    else:
                        black_timer.start_timer()
                        white_timer.stop_timer()

                    # vykreslenie tahu
                    draw_board(fun.canvas, True, 0, 50,
                               create_chess_array(fun.board))

            except:
                pass

            if fun.board.is_checkmate() == True:
                white_timer.stop_timer()
                black_timer.stop_timer()
                fun.canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                             fill="lightgrey", outline="black")
                fun.canvas.create_text((60 * 8 + 20)//2-5, 
                                         (60 * 8 + 20 + 100)//2,
                                         text="VÝHRA",
                                         font=('Helvetica','50','bold'))
                if Game.board.turn == chess.BLACK:
                    fun.canvas.create_text((60 * 8 + 20)//2, 
                                            (60 * 8 + 20 + 100)//2+40,
                                            text="Biely vyhral šachmatom",
                                            font=('Helvetica','15','bold'))
                else:
                    fun.canvas.create_text((60 * 8 + 20)//2, 
                                            (60 * 8 + 20 + 100)//2+40,
                                            text="Čierny vyhral šachmatom",
                                            font=('Helvetica','15','bold'))
            elif fun.board.is_stalemate() == True:
                white_timer.stop_timer()
                black_timer.stop_timer()
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
                white_timer.stop_timer()
                black_timer.stop_timer()
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
                white_timer.stop_timer()
                black_timer.stop_timer()
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
        Menu.canvas = Canvas(width=W, height=H,bg='white')
        Menu.canvas.pack()

        # menu buttons
        Button(Menu.canvas, text = "Hra s priaťelom", command=self.gameMenu,
               height= 3, width=28).place(x = 60*8+2*20, y = 40)
        Button(Menu.canvas, text = "Precvičenie otvorení", command=self.openingLearner,
               height= 3, width=28).place(x = 60*8+2*20, y = 40+75)
        Button(Menu.canvas, text = "Pravidlá", command=self.rules, height= 3,
               width=28).place(x = 60*8+2*20, y = 420)
        
        # vykreslenie sachovnice
        draw_board(Menu.canvas, False)

        Menu.canvas.mainloop()

    def gameMenu(self):
        self.window.destroy()
        GameMenu()

    def openingLearner(self):
        self.window.destroy()
        OpeningLearner()

    def rules(self):
        self.window.destroy()
        rules_window = Tk()  # Vytvořte nové okno
        rules_window.title('Pravidlá šachu')

        W = 500
        H = 500
        p = Canvas(width=W, height=H,bg='white')
        p.pack()

        p.create_text(W//2, 30, text = "DDD", fill="black")


class GameMenu:
    def __init__(self) -> None:
        # vytvorenie noveho okna
        self.window = tk.Tk()
        self.window.title("Menu")

        # vytvorenie noveho platna
        W = 750
        H = 60 * 8 + 20
        GameMenu.canvas = Canvas(width=W, height=H,bg='white')
        GameMenu.canvas.pack()

        
        # menu buttons
        Button(GameMenu.canvas, text = "1 + 0", command=self.blitz,
               height= 3, width=28).place(x = 60*8+2*20, y = 40)
        Button(GameMenu.canvas, text = "1 + 1", command=self.blitz_bonus,
               height= 3, width=28).place(x = 60*8+2*20, y = 40+75)
        Button(GameMenu.canvas, text = "10 + 0", command=self.rapid,
               height= 3, width=28).place(x = 60*8+2*20, y = 40+75*2)
        Button(GameMenu.canvas, text = "10 + 3", command=self.rapid_bonus,
               height= 3, width=28).place(x = 60*8+2*20, y = 40+75*3)
        Button(GameMenu.canvas, text = "Menu", command=self.menu, height= 3,
               width=28).place(x = 60*8+2*20, y = 420)
        
        # vykreslenie sachovnice
        draw_board(GameMenu.canvas, False)

        GameMenu.canvas.mainloop()

    def blitz(self):
        self.window.destroy()
        Game(1*60, 0)

    def blitz_bonus(self):
        self.window.destroy()
        Game(1*60, 1)

    def rapid(self):
        self.window.destroy()
        Game(10*60, 0)
    
    def rapid_bonus(self):
        self.window.destroy()
        Game(10*60, 3)

    def menu(self):
        self.window.destroy()
        Menu()

class Game:
    def __init__(self, time, bonus) -> None:
        # vytvorenie noveho okna
        self.window = tk.Tk()
        self.window.title('Hra s priteľom')

        self.W = 60 * 8 + 20
        self.H = 60 * 8 + 20 + 100
        self.time = time
        self.bonus = bonus

        # premenné pre funkciu piece_move
        Game.position = "...."
        Game.board = chess.Board()
        Game.white_on_turn = True
        
        # vytvorenie noveho platna
        Game.canvas = Canvas(width=self.W, height=self.H, bg='white')
        Game.canvas.pack()

        # vykreslenie sachovnice
        draw_board(Game.canvas, False, 0, 50)

        # button START
        Button(Game.canvas, text="START", command=self.game_start,
               height=2, width=20).place(x=self.W-160-15, y=self.H-50)

        Game.canvas.mainloop()

    def game_start(self):
        draw_board(Game.canvas, True, 0, 50, create_chess_array(Game.board))

        # button MENU
        Button(Game.canvas, text="Menu", command=self.game_end,
               height=2, width=20).place(x=self.W-160-15, y=self.H-50)

        # timers
        global black_timer, white_timer
        black_timer = Timer(Game.canvas, self.time, self.bonus, 10+15, 10)
        white_timer = Timer(Game.canvas, self.time, self.bonus, 10+15, self.H-50)

        white_timer.start_timer()

        # urcovanie suradnic
        Game.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, action):
        piece_move(action.x, action.y, Game)

    def game_end(self):
        white_timer.stop_timer()
        black_timer.stop_timer()
        self.window.destroy()
        Menu()

class Timer:
    def __init__(self, canvas, time, bonus, x, y):
        self.canvas = canvas
        self.time = time
        self.bonus = bonus
        self.formated_time = tk.StringVar()
        self.formated_time.set(self.format_time())
        
        self.time_label = tk.Label(canvas, textvariable=self.formated_time,
                                   font=("Arial", 24)).place(x=x, y=y)

        self.active_timer = None

    def format_time(self):
        mins = self.time // 60
        secs = self.time % 60
        return f"{mins:02}:{secs:02}"

    def start_timer(self):
        if self.time > 0:
            self.time -= 1
            self.formated_time.set(self.format_time())
            self.active_timer = self.canvas.after(1000, self.start_timer)
        else:
            white_timer.stop_timer()
            black_timer.stop_timer()
            Game.canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                         fill="lightgrey", outline="black")
            
            if Game.board.can_claim_draw():
                Game.canvas.create_text((60 * 8 + 20)//2-5, 
                                    (60 * 8 + 20 + 100)//2,
                                     text="REMÍZA",
                                     font=('Helvetica','50','bold'))
                Game.canvas.create_text((60 * 8 + 20)//2, 
                                        (60 * 8 + 20 + 100)//2+40,
                                        text="Nedostatok času a nedostatok materiálu",
                                        font=('Helvetica','15','bold'))
            else:
                Game.canvas.create_text((60 * 8 + 20)//2-5, 
                                        (60 * 8 + 20 + 100)//2,
                                        text="VÝHRA",
                                        font=('Helvetica','50','bold'))
                if Game.board.turn == chess.BLACK:
                    Game.canvas.create_text((60 * 8 + 20)//2, 
                                            (60 * 8 + 20 + 100)//2+40,
                                            text="biely vyhral - nedostatok času",
                                            font=('Helvetica','15','bold'))
                else:
                    Game.canvas.create_text((60 * 8 + 20)//2, 
                                            (60 * 8 + 20 + 100)//2+40,
                                            text="čierny vyhral - nedostatok času",
                                            font=('Helvetica','15','bold'))

    def stop_timer(self):
        if self.active_timer is not None:
            self.time += self.bonus
            self.formated_time.set(self.format_time())
            self.canvas.after_cancel(self.active_timer)


class OpeningLearner:
    def __init__(self) -> None:
        # vytvorenie noveho okna
        self.window = tk.Tk()
        self.window.title("Menu")

        # vytvorenie noveho platna
        W = 750
        H = 60 * 8 + 20
        OpeningLearner.canvas = Canvas(width=W, height=H,bg='white')
        OpeningLearner.canvas.pack()
        
        # OpeningLearner buttons
        Button(OpeningLearner.canvas, text = "Vytvoriť nové otvorenie", command=self.new_opening,
               height= 3, width=28).place(x = 60*8+2*20, y = 40)
        Button(OpeningLearner.canvas, text = "Menu", command=self.menu, height= 3,
               width=28).place(x = 60*8+2*20, y = 420)

        # vykreslenie sachovnice
        draw_board(OpeningLearner.canvas, False)

        OpeningLearner.canvas.mainloop()
    
    def new_opening(self):
        pass

    def menu(self):
        self.window.destroy()
        Menu()

Menu()