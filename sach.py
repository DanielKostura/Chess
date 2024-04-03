from tkinter import *
import tkinter as tk
import os
# import typing
import chess
# pip install chess
# python -m pip install chess

def draw_board(pieces: bool, board: list[list[str]]=[[""]],
               bonus_x=0, bonus_y=0):
    canvas.delete("all")

    for row in range(8):
        for column in range(8):
            if (row + column) % 2 == 1:
                farba = "green"
            else:
                farba = "white"

            x = column*60+10+bonus_x
            y = row*60+10+bonus_y
            canvas.create_rectangle(x, y, x+60, y+60,
                                    fill=farba, outline='black',width='5')
    
            if pieces == True:
                canvas.create_text(x+30, y+30, text=board[row][column],
                                           font=('Helvetica','50','bold'))

def create_chess_array(board, reverse = False):
    board_rows = []
    for i in reversed(range(8)):
        row = []
        for j in reversed(range(8)):
            if reverse == False:
                current_piece = board.piece_at(chess.square(7-j, i))
            elif reverse == True:
                current_piece = board.piece_at(chess.square(j, 7-i))
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
                if fun.board.turn == chess.WHITE:
                    white_timer.start_timer()
                    black_timer.stop_timer()
                else:
                    black_timer.start_timer()
                    white_timer.stop_timer()

                # vykreslenie tahu
                draw_board(True, create_chess_array(fun.board), 0, 50)

        except:
            pass

        if fun.board.is_checkmate() == True:
            white_timer.stop_timer()
            black_timer.stop_timer()
            canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                    fill="lightgrey", outline="black")
            canvas.create_text((60 * 8 + 20)//2-5, 
                                (60 * 8 + 20 + 100)//2,
                                text="VÝHRA",
                                font=('Helvetica','50','bold'))
            if Game.board.turn == chess.BLACK:
                canvas.create_text((60 * 8 + 20)//2, 
                                    (60 * 8 + 20 + 100)//2+40,
                                    text="Biely vyhral šachmatom",
                                    font=('Helvetica','15','bold'))
            else:
                canvas.create_text((60 * 8 + 20)//2, 
                                    (60 * 8 + 20 + 100)//2+40,
                                    text="Čierny vyhral šachmatom",
                                    font=('Helvetica','15','bold'))
        elif fun.board.is_stalemate() == True:
            white_timer.stop_timer()
            black_timer.stop_timer()
            canvas.create_rectangle(60, 60+60*3, 15+60*7, 60*6,
                                    fill="grey", outline="black")
            canvas.create_text((60 * 8 + 20)//2-5, 
                                (60 * 8 + 20 + 100)//2,
                                text="REMÍZA",
                                font=('Helvetica','50','bold'))
            canvas.create_text((60 * 8 + 20)//2, 
                                (60 * 8 + 20 + 100)//2+40,
                                text="Patová situácia",
                                font=('Helvetica','15','bold'))
        elif fun.board.is_insufficient_material() == True:
            white_timer.stop_timer()
            black_timer.stop_timer()
            canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                    fill="lightgrey", outline="black")
            canvas.create_text((60 * 8 + 20)//2-5, 
                                (60 * 8 + 20 + 100)//2,
                                text="REMÍZA",
                                font=('Helvetica','50','bold'))
            canvas.create_text((60 * 8 + 20)//2, 
                                (60 * 8 + 20 + 100)//2+40,
                                text="Nedostatok materiálu",
                                font=('Helvetica','15','bold'))
        elif fun.board.can_claim_threefold_repetition() == True:
            white_timer.stop_timer()
            black_timer.stop_timer()
            canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                    fill="lightgrey", outline="black")
            canvas.create_text((60 * 8 + 20)//2, 
                                (60 * 8 + 20 + 100)//2-5,
                                text="REMÍZA",
                                font=('Helvetica','50','bold'))
            canvas.create_text((60 * 8 + 20)//2, 
                                (60 * 8 + 20 + 100)//2+40,
                                text="Opakovanie ťahou",
                                font=('Helvetica','15','bold'))

def clean_canvas(pole):
    # Delete all objects on the canvas
    canvas.delete("all")
        
    # Destroy or remove buttons, labels, and entries
    for widget in pole:
        widget.destroy()

class Menu:
    def __init__(self) -> None:
        w = 750
        h = 60 * 8 + 20
        canvas.config(width=w, height=h, bg='white')
        window.title("Menu")

        # menu buttons
        self.b1 = Button(canvas, text = "Hra s priaťelom",
                        command=self.gameMenu, height= 3, width=28)
        self.b1.place(x = 60*8+2*20, y = 40)

        self.b2 = Button(canvas, text = "Precvičenie otvorení",
                         command=self.openingLearnerMenu, height= 3, width=28)
        self.b2.place(x = 60*8+2*20, y = 40+75)

        self.b3 = Button(canvas, text = "Pravidlá", command=self.rules, height= 3,
                        width=28)
        self.b3.place(x = 60*8+2*20, y = 420)
        
        # vykreslenie sachovnice
        draw_board(False)
        
        canvas.mainloop()

    def gameMenu(self):
        clean_canvas([self.b1, self.b2, self.b3])
        GameMenu()

    def openingLearnerMenu(self):
        clean_canvas([self.b1, self.b2, self.b3])
        OpeningLearnerMenu()

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
        window.title('Menu')
        # menu buttons
        self.b1 = Button(canvas, text = "1 + 0", command=self.blitz,
                         height= 3, width=28)
        self.b1.place(x = 60*8+2*20, y = 40)

        self.b2 = Button(canvas, text = "1 + 1", command=self.blitz_bonus,
                         height= 3, width=28)
        self.b2.place(x = 60*8+2*20, y = 40+75)

        self.b3 = Button(canvas, text = "10 + 0", command=self.rapid,
                         height= 3, width=28)
        self.b3.place(x = 60*8+2*20, y = 40+75*2)

        self.b4 = Button(canvas, text = "10 + 3", command=self.rapid_bonus,
                         height= 3, width=28)
        self.b4.place(x = 60*8+2*20, y = 40+75*3)

        self.bm = Button(canvas, text = "Menu", command=self.menu,
                         height= 3, width=28)
        self.bm.place(x = 60*8+2*20, y = 420)
        
        # vykreslenie sachovnice
        draw_board(False)

        canvas.mainloop()

    def blitz(self):
        clean_canvas([self.b1, self.b2, self.b3, self.b4, self.bm])
        Game(1*60, 0)

    def blitz_bonus(self):
        clean_canvas([self.b1, self.b2, self.b3, self.b4, self.bm])
        Game(1*60, 1)

    def rapid(self):
        clean_canvas([self.b1, self.b2, self.b3, self.b4, self.bm])
        Game(10*60, 0)
    
    def rapid_bonus(self):
        clean_canvas([self.b1, self.b2, self.b3, self.b4, self.bm])
        Game(10*60, 3)

    def menu(self):
        clean_canvas([self.b1, self.b2, self.b3, self.b4, self.bm])
        Menu()

class OpeningLearnerMenu:
    def __init__(self) -> None:
        global w, h
        w = 750
        h = 60 * 8 + 20
        canvas.config(width=w, height=h, bg='white')
        window.title("Menu")
        
        self.filemane = tk.StringVar()
        self.lerning = 0
        
        # OpeningLearnerMenu buttons
        self.l = Label(canvas, text = "Zadaj názov otvorenia:")
        self.l.place(x = 60*8+2*20+40, y = 40)

        self.e = Entry(canvas, textvariable = self.filemane, 
                        font=('calibre', 10, 'normal'), bg="lightgrey")
        self.e.place(x = 60*8+2*20+30, y = 70)

        self.b1 = Button(canvas, text = "Vytvoriť nové otvorenie",
                         command=self.new_opening, height= 2, width=22)
        self.b1.place(x = 60*8+2*20+18, y = 100)

        self.b2 = Button(canvas, text = "Učenie",
                         command=self.learn, height= 2, width=12)
        self.b2.place(x = 60*8+2*20, y = h-110)
        self.b2.config(state=tk.DISABLED)

        self.b3 = Button(canvas, text = "Precvičenie",
                         command=self.review, height= 2, width=12)
        self.b3.place(x = 60*8+7*20+10, y = h-110)

        self.b4 = Button(canvas, text = "Upraviť",
                         command=self.update, height= 2, width=12)
        self.b4.place(x = 60*8+2*20, y = h-60)
   
        self.bm = Button(canvas, text = "Menu", command=self.menu,
                           height= 2, width=12)
        self.bm.place(x = 60*8+7*20+10, y = h-60)

        # Scroll list
        self.scroll_list()

        # vykreslenie sachovnice
        draw_board(False)

        canvas.mainloop()
    
    def selection_in_scroll_list(self, action):
        # Získajte index položky, na ktorú ste klikli
        index = self.openingList.nearest(action.y)
        # Získajte text položky, na ktorú ste klikli
        selected_item = self.openingList.get(index)

        clean_canvas([self.l, self.e, self.b1, self.b2, self.b3, self.b4, self.bm, self.openingList])
        
        if self.lerning == 0:
            OpeningLearner(selected_item + ".txt")
        elif self.lerning == 1:
            OpeningReviewer(selected_item + ".txt")
        elif self.lerning == 2:
            OpeningCreator(selected_item)

    def scroll_list(self):
        self.openingList = Listbox(window, font=10, selectmode="browse")

        # Získajte aktuálny adresár
        current_directory = os.getcwd()
        # Získajte zoznam všetkých súborov v aktuálnom adresári
        files = os.listdir(current_directory)
        
        # Iterujte každý súbor v adresári
        for file in files:
            # Skontrolujte, či je súbor súborom .txt
            if file.endswith(".txt"):
                self.openingList.insert(END, file[:-4])

        self.openingList.place(x=w-230, y=155, height=230, width=204)

        self.openingList.bind('<Button-1>', self.selection_in_scroll_list)

    def new_opening(self):
        name = self.filemane.get()
        
        # vytvorenie/vycistenie suborov
        f = open(name + ".txt", "w")
        f.close()

        if name != "":
            clean_canvas([self.l, self.e, self.b1, self.b2, self.b3, self.b4, self.bm, self.openingList])
            OpeningCreator(name)
        else:
            canvas.create_text(w-20*2-88, 150,
                               text="Musíte prve zadať názov otvorenia", 
                               font=('Helvetica','10','bold'), fill="red")
            self.e.config(bg="lightcoral")

    def learn(self):
        self.lerning = 0
        self.b2.config(state=tk.DISABLED)
        self.b3.config(state=tk.NORMAL)
        self.b4.config(state=tk.NORMAL)

    def review(self):
        self.lerning = 1
        self.b2.config(state=tk.NORMAL)
        self.b3.config(state=tk.DISABLED)
        self.b4.config(state=tk.NORMAL)

    def update(self):
        self.lerning = 2
        self.b2.config(state=tk.NORMAL)
        self.b3.config(state=tk.NORMAL)
        self.b4.config(state=tk.DISABLED)

    def menu(self):
        clean_canvas([self.l, self.e, self.b1, self.b2, self.b3, self.b4, self.bm, self.openingList])
        Menu()


class Game:
    def __init__(self, time, bonus) -> None:
        window.title('Hra s priteľom')

        # vytvorenie noveho platna
        global w, h
        w = 60 * 8 + 20
        h = 60 * 8 + 20 + 100
        canvas.config(width=w, height=h, bg='white')
        
        self.time = time
        self.bonus = bonus

        # premenné pre funkciu piece_move
        Game.position = "...."
        Game.board = chess.Board()
        Game.white_on_turn = True
        
        # vykreslenie sachovnice
        draw_board(False, [[""]], 0, 50)

        # button START
        self.b1 = Button(canvas, text="START", command=self.game_start,
               height=2, width=20)
        self.b1.place(x=w-160-15, y=h-50)

        canvas.mainloop()

    def game_start(self):
        self.b1.destroy()

        draw_board(True, create_chess_array(Game.board), 0, 50)

        # button MENU
        self.bm = Button(canvas, text="Menu", command=self.game_end,
                         height=2, width=20)
        self.bm.place(x=w-160-15, y=h-50)

        # timers
        global black_timer, white_timer
        black_timer = Timer(self.time, self.bonus, 10+15, 10)
        white_timer = Timer(self.time, self.bonus, 10+15, h-50)

        white_timer.start_timer()

        # urcovanie suradnic
        canvas.bind("<Button-1>", self.on_click)

    def on_click(self, action):
        if white_timer.time > 0 and black_timer.time > 0:
            piece_move(action.x, action.y, Game)

    def game_end(self):
        clean_canvas([self.bm, black_timer.time_label, white_timer.time_label])
        Menu()

class Timer:
    def __init__(self, time, bonus, x, y):
        self.time = time
        self.bonus = bonus
        self.formated_time = tk.StringVar()
        self.formated_time.set(self.format_time())
        
        self.time_label = tk.Label(canvas, textvariable=self.formated_time,
                                   font=("Arial", 24))
        self.time_label.place(x=x, y=y)

        self.active_timer = None

    def format_time(self):
        mins = self.time // 60
        secs = self.time % 60
        return f"{mins:02}:{secs:02}"

    def start_timer(self):
        if self.time > 0:
            self.time -= 1
            self.formated_time.set(self.format_time())
            self.active_timer = canvas.after(1000, self.start_timer)
        else:
            white_timer.stop_timer()
            black_timer.stop_timer()
            canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                         fill="lightgrey", outline="black")
            
            if Game.board.can_claim_draw():
                canvas.create_text((60 * 8 + 20)//2-5, 
                                   (60 * 8 + 20 + 100)//2,
                                    text="REMÍZA",
                                    font=('Helvetica','50','bold'))
                canvas.create_text((60 * 8 + 20)//2, 
                                   (60 * 8 + 20 + 100)//2+40,
                                    text="Nedostatok času a nedostatok materiálu",
                                    font=('Helvetica','15','bold'))
            else:
                canvas.create_text((60 * 8 + 20)//2-5, 
                                   (60 * 8 + 20 + 100)//2,
                                    text="VÝHRA",
                                    font=('Helvetica','50','bold'))
                if Game.board.turn == chess.BLACK:
                    canvas.create_text((60 * 8 + 20)//2, 
                                       (60 * 8 + 20 + 100)//2+40,
                                        text="biely vyhral - nedostatok času",
                                        font=('Helvetica','15','bold'))
                else:
                    canvas.create_text((60 * 8 + 20)//2, 
                                       (60 * 8 + 20 + 100)//2+40,
                                        text="čierny vyhral - nedostatok času",
                                        font=('Helvetica','15','bold'))

    def stop_timer(self):
        if self.active_timer is not None:
            self.time += self.bonus
            self.formated_time.set(self.format_time())
            canvas.after_cancel(self.active_timer)


class OpeningCreator:
    def __init__(self, file) -> None:
        self.variant = 0
        self.putback = 0
        self.file = file + ".txt"
        self.name_variant = tk.StringVar()
        self.notation = []

        window.title('Vytváranie otvorenia')

        # premenné pre funkciu noted
        self.position = "...."
        self.board = chess.Board()

        # vykreslenie sachovnice
        draw_board(True, create_chess_array(chess.Board()))
        
        # Scroll lists
        self.moveList = Listbox(window, font=10)
        self.moveList.place(x=w-200, y=40, height=190, width=157)

        self.varList = Listbox(window, font=10)

        # OpeningCreator buttons
        self.b1 = Button(canvas, text="Zápis", command=self.update_scroll_list,
                         height=1, width=5)
        self.b1.place(x=w-200, y=18)
        self.b1.config(state=tk.DISABLED)

        self.b2 = Button(canvas, text="Varinty", command=self.update_variant_list,
                         height=1, width=6)
        self.b2.place(x=w-156, y=18)

        self.e = Entry(canvas, textvariable=self.name_variant,
                       bg="lightgrey", width=17)
        self.e.place(x=w-200, y=243)

        self.b3 = Button(canvas, text="Uložiť", command=self.save,
                         height=1, width=5)
        self.b3.place(x=w-88, y=239)

        self.bm = Button(canvas, text="Menu", command=self.end,
                         height=2, width=21)
        self.bm.place(x=w-200, y=260+10)

        self.b4 = Button(canvas, text="Resetovať šachovnicu", command=self.reset,
                         height=2, width=21)
        self.b4.place(x=w-200, y=315+10)

        self.b5 = Button(canvas, text="Vymaž", command=self.delete,
                         height=2, width=21)
        self.b5.place(x=w-200, y=370+10)

        self.b6 = Button(canvas, text="<", command=self.back,
                         height=2, width=7)
        self.b6.place(x=w-200, y=425+10)
        self.b6.config(state=tk.DISABLED)

        self.b7 = Button(canvas, text=">", command=self.next,
                         height=2, width=7)
        self.b7.place(x=w-102, y=425+10)
        self.b7.config(state=tk.DISABLED)
        
        # action
        canvas.bind("<Button-1>", self.noted)

        canvas.mainloop()

    def noted(self, action):
        x = action.x
        y = action.y
        if 10 < x < 60*8 + 10 and 10 < y < 60*8+10:
            file = chr(ord('a') + (x - 10) // 60)
            rank = str(8 - (y - 10) // 60)

            self.position += file + rank
            self.position = self.position[2:]

            try:
                if chess.Move.from_uci(self.position) in self.board.legal_moves:
                    self.b6.config(state=tk.NORMAL)
                    
                    # zaznacenie tahu
                    self.notation.append(self.position)
                    
                    # vykreslenie tahu
                    self.board.push_san(self.position)
                    draw_board(True, create_chess_array(self.board))

                    self.update_scroll_list()
            except:
                pass

    def open_varList(self, action):
        # Získajte index položky, na ktorú ste klikli
        index = self.varList.nearest(action.y)
        # Získajte text položky, na ktorú ste klikli
        selected_item = self.varList.get(index)

        with open(self.file, "r") as f:
            lines = f.readlines()
        
        for i in range(len(lines)):
            if selected_item == lines[i][:lines[i].index("##")]:
                self.notation = lines[i][lines[i].index("##")+2:].split()

                self.board = chess.Board()
                for i in range(len(self.notation)):
                    self.board.push_san(self.notation[i])

                draw_board(True, create_chess_array(self.board))

    def delete_varList(self, action):
        # Získajte index položky, na ktorú ste klikli
        index = self.varList.nearest(action.y)
        # Získajte text položky, na ktorú ste klikli
        selected_item = self.varList.get(index)

        with open(self.file, "r") as f:
            lines = f.readlines()
        
        for i in range(len(lines)):
            if selected_item == lines[i][:lines[i].index("##")]:
                lines.pop(i)
                break

        with open(self.file, "w") as f:
            f.writelines(lines)

        self.update_variant_list()

    def update_scroll_list(self):
        self.b1.config(state=tk.DISABLED)
        self.b2.config(state=tk.NORMAL)

        if self.moveList:
            self.moveList.destroy()
        else:
            self.varList.destroy()

        self.moveList = Listbox(window, font=10, selectmode="browse")

        for i in range(0, len(self.notation), 2):
            if len(self.notation) != i+1:
                self.moveList.insert(END, str(i-(i//2)+1) + ". " + str(self.notation[i]) + "     " + str(self.notation[i+1]))
            else:
                self.moveList.insert(END, str(i-(i//2)+1) + ". " + str(self.notation[i]))
        
        self.moveList.place(x=w-200, y=40, height=200, width=157)
    
    def update_variant_list(self):
        self.b1.config(state=tk.NORMAL)
        self.b2.config(state=tk.DISABLED)

        if self.varList:
            self.varList.destroy()
        else:
            self.moveList.destroy()
        
        self.varList = Listbox(window, font=10)

        with open(self.file, "r") as f:
            lines = f.readlines()
        
        for i in range(len(lines)):
            self.varList.insert(END, lines[i][:lines[i].index("##")])

        self.varList.place(x=w-200, y=40, height=200, width=157)

        self.varList.bind('<Button-1>', self.open_varList)
        self.varList.bind('<Button-3>', self.delete_varList)

    def load_board(self):
        self.board = chess.Board()
        chess_line = self.read_specific_line(self.file, self.variant)
        #print(chess_line)

        for i in range(len(chess_line)-self.putback):
            self.board.push_san(chess_line[i])

    def read_specific_line(self, filename, line_number):
        with open(filename, 'r') as f:
            lines = f.readlines()
        try:
            return lines[line_number].split()
        except:
            return ""


    def save(self):
        name = self.name_variant.get()
        
        if name != "":
            # formatovanie z Listu do str
            note = ""
            for i in range(len(self.notation)):
                note += self.notation[i] + " "

            with open(self.file, "r") as f:
                lines = f.readlines()

            lines.append(name + "##" + note + "\n")

            with open(self.file, "w") as f:
                f.writelines(lines)

            self.update_variant_list()

            # da entry do povodneho stavu
            self.e.delete(0, tk.END)
            self.e.config(bg="white")
        else:
            self.e.config(bg="lightcoral")

    def reset(self):
        self.putback = 0
        self.position = "...."
        self.board = chess.Board()
        self.notation = []

        self.b6.config(state=tk.DISABLED)
        self.b7.config(state=tk.DISABLED)

        self.update_scroll_list()
        draw_board(True, create_chess_array(self.board))

    def delete(self):
        self.notation.pop()
        self.board.pop()
        draw_board(True, create_chess_array(self.board))
        self.update_scroll_list()

    def back(self):
        if self.putback < len(self.notation):
            self.putback += 1
            self.board.pop()
            draw_board(True, create_chess_array(self.board))
            self.b7.config(state=tk.NORMAL)

            if self.putback == len(self.notation):
                self.b6.config(state=tk.DISABLED)

    def next(self):
        if self.putback > 0:
            self.board.push_san(self.notation[-self.putback])
            self.putback -= 1
            draw_board(True, create_chess_array(self.board))
            self.b6.config(state=tk.NORMAL)

            if self.putback == 0:
                self.b7.config(state=tk.DISABLED)


    def end(self):
        clean_canvas([self.bm, self.b1, self.b2, self.b3, self.b4, self.b5, 
                      self.b5, self.b6, self.b7, self.moveList, self.varList,
                      self.e])
        OpeningLearnerMenu()

class OpeningLearner:
    def __init__(self, file) -> None:
        self.file = file
        window.title(self.file[:-4])

        # vytvorenie noveho platna
        global w, h
        w = 60 * 8 + 20
        h = 60 * 8 + 20 + 100
        canvas.config(width=w, height=h, bg='white')

        # premenné pre funkciu piece_move
        self.position = "...."
        self.board = chess.Board()
        self.white_on_turn = True

        # ostatne premenne
        self.variant = 0
        self.turn = 0

        with open(self.file, "r") as f: # ziskanie info o otvoreni
            self.lines = f.readlines()
        
        self.names = []
        self.moves = []
        for i in range(len(self.lines)):
            self.names.append(self.lines[i][:self.lines[i].index("##")])
            self.moves.append(self.lines[i][self.lines[i].index("##")+2:-2].split())

        # vykreslenie sachovnice
        draw_board(False, [[""]], 0, 50)

        # button START
        self.bs = Button(canvas, text="START", command=self.opening_start,
               height=2, width=20)
        self.bs.place(x=w-160-15, y=h-50)
        
        # názov variantu
        self.title()

        canvas.mainloop()

    def opening_start(self):
        self.bs.destroy()

        draw_board(True, create_chess_array(self.board), 0, 50)
        self.title()

        # button MENU
        self.bm = Button(canvas, text="Menu", command=self.end,
                         height=2, width=20)
        self.bm.place(x=25, y=h-50)

        # button NEXT
        self.bn = Button(canvas, text="Ďalej", command=self.next,
                         height=2, width=20)
        self.bn.place(x=w-175, y=h-50)

        # urcovanie suradnic
        canvas.bind("<Button-1>", self.on_click)
    
    def on_click(self, action): # uprav
        x = action.x
        y = action.y
        if 10 < x < 60*8 + 10 and 50 < y < 60*8+50:
            file = chr(ord('a') + (x - 10) // 60)
            rank = str(8 - (y - 50) // 60)
            
            self.position += file + rank
            self.position = self.position[2:]
            
            try:
                if chess.Move.from_uci(self.position) in self.board.legal_moves:
                    # spravny tah
                    if len(self.moves[self.variant]) > self.turn and self.position == self.moves[self.variant][self.turn]:
                        self.board.push_san(self.position)
                        draw_board(True, create_chess_array(self.board), 0, 50) # nevykresli sa
                        self.title()
                        self.turn += 1
                        self.correct()
                    else:
                        self.wrong()
            except:
                pass
    
    def title(self):
        canvas.create_text(w//2, 35, text=self.names[self.variant],
                           font=('Helvetica','30','bold'))

    def next(self):
        if len(self.moves)-1 == self.variant and self.turn == len(self.moves[self.variant]):
            self.end()

        elif self.turn == len(self.moves[self.variant]):
            self.board = chess.Board()
            draw_board(True, create_chess_array(self.board), 0, 50)

            self.turn = 0
            self.variant += 1
            self.title()
            self.correct()
            print(self.moves[self.variant][self.turn])

        else:
            self.wrong()

    def correct(self):
        self.l1 = Label(canvas, text="Správne", font=('Helvetica','23','bold'), 
                        bg="lightgreen")
        self.l1.place(x=60*3+10, y=h-50)
        self.l1.after(500, self.l1.destroy)

    def wrong(self):
        self.l2 = Label(canvas, text="Nesprávne", font=('Helvetica','23','bold'), 
                        bg="firebrick2")
        self.l2.place(x=60*3+10, y=h-50)
        self.l2.after(500, self.l2.destroy)

    def end(self):
        clean_canvas([self.bm, self.bn])
        OpeningLearnerMenu()

class OpeningReviewer:
    def __init__(self, file) -> None:
        self.file = file

window = tk.Tk()
window.title("Menu")

w = 750
h = 60 * 8 + 20
canvas = Canvas(width=w, height=h,bg='white')
canvas.pack()

Menu()