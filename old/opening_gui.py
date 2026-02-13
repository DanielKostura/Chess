from chess_app.gui.old.menu_old import BaseMenu

class OpeningCreator:
    def __init__(self, file) -> None:
        self.variant = 0
        self.putback = 0
        self.file = file + ".txt"
        self.name_variant = tk.StringVar()
        self.notation = []

        window.title('Vytváranie otvorenia')

        # Variables for on_click function
        self.position = "...."
        self.board = chess.Board()

        # Chessboard rendering
        draw_board(chess.Board())

        # Scroll lists
        self.move_list = Listbox(window, font=10)
        self.move_list.place(x=w-200, y=40, height=190, width=157)

        self.var_list = Listbox(window, font=10)

        # OpeningCreator buttons
        self.b1 = Button(canvas, text="Zápis", command=self.update_scroll_list,
                         height=1, width=5)
        self.b1.place(x=w-200, y=18)
        self.b1.config(state=tk.DISABLED)

        self.b2 = Button(canvas, text="Varianty", command=self.update_var_list,
                         height=1, width=6)
        self.b2.place(x=w-156, y=18)

        self.e = Entry(canvas, textvariable=self.name_variant,
                       bg="lightgrey", width=17)
        self.e.place(x=w-200, y=243)

        self.b3 = Button(canvas, text="Uložiť",
                         command=self.save,
                         height=1, width=5)
        self.b3.place(x=w-88, y=239)

        self.bm = Button(canvas, text="Menu",
                         command=self.end,
                         height=2, width=21)
        self.bm.place(x=w-200, y=260+10)

        self.b4 = Button(canvas, text="Resetovať šachovnicu",
                         command=self.reset,
                         height=2, width=21)
        self.b4.place(x=w-200, y=315+10)

        self.b5 = Button(canvas, text="Vymaž",
                         command=self.delete,
                         height=2, width=21)
        self.b5.place(x=w-200, y=370+10)

        self.b6 = Button(canvas, text="<",
                         command=self.back,
                         height=2, width=7)
        self.b6.place(x=w-200, y=425+10)
        self.b6.config(state=tk.DISABLED)

        self.b7 = Button(canvas, text=">",
                         command=self.next,
                         height=2, width=7)
        self.b7.place(x=w-102, y=425+10)
        self.b7.config(state=tk.DISABLED)

        # Action
        canvas.bind("<Button-1>", self.on_click)

        canvas.mainloop()

    def on_click(self, action):
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

                    # Noting move
                    self.notation.append(self.position)

                    # Chessboard/move rendering
                    self.board.push_san(self.position)
                    draw_board(self.board)

                    self.update_scroll_list()
            except:
                pass

    def open_var_list(self, action):
        # Getting the index of the item you clicked on
        index = self.var_list.nearest(action.y)
        # Getting the text of the item you clicked on
        selected_item = self.var_list.get(index)

        with open(self.file, "r") as f:
            lines = f.readlines()

        for line in lines:
            if selected_item == line[:line.index("##")]:
                self.notation = line[line.index("##")+2:].split()

                self.board = chess.Board()
                for chess_line in self.notation:
                    self.board.push_san(chess_line)

                draw_board(self.board)

        self.putback = 0
        self.b6.config(state=tk.NORMAL)
        self.b7.config(state=tk.DISABLED)

    def delete_var_list(self, action):
        # Get the index of the item you clicked on
        index = self.var_list.nearest(action.y)
        # Get the text of the item you clicked on
        selected_item = self.var_list.get(index)

        with open(self.file, "r") as f:
            lines = f.readlines()

        for i in range(len(lines)):
            if selected_item == lines[i][:lines[i].index("##")]:
                lines.pop(i)
                break

        with open(self.file, "w") as f:
            f.writelines(lines)

        self.update_var_list()

    def update_scroll_list(self):
        self.b1.config(state=tk.DISABLED)
        self.b2.config(state=tk.NORMAL)

        if self.move_list:
            self.move_list.destroy()
        else:
            self.var_list.destroy()

        self.move_list = Listbox(window, font=10, selectmode="browse")

        for i in range(0, len(self.notation), 2):
            if len(self.notation) != i+1:
                self.move_list.insert(END,
                                      str(i-(i//2)+1) + ". " +
                                      str(self.notation[i]) + "     " +
                                      str(self.notation[i+1]))
            else:
                self.move_list.insert(END,
                                      str(i-(i//2)+1) + ". " +
                                      str(self.notation[i]))

        self.move_list.place(x=w-200, y=40, height=200, width=157)

    def update_var_list(self):
        self.b1.config(state=tk.NORMAL)
        self.b2.config(state=tk.DISABLED)

        if self.var_list:
            self.var_list.destroy()
        else:
            self.move_list.destroy()

        self.var_list = Listbox(window, font=10)

        with open(self.file, "r") as f:
            lines = f.readlines()

        for line in lines:
            self.var_list.insert(END, line[:line.index("##")])

        self.var_list.place(x=w-200, y=40, height=200, width=157)

        self.var_list.bind('<Button-1>', self.open_var_list)
        self.var_list.bind('<Button-3>', self.delete_var_list)

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
            # formating from Listu to str
            note = ""
            for i in range(len(self.notation)):
                note += self.notation[i] + " "

            with open(self.file, "r") as f:
                lines = f.readlines()

            lines.append(name + "##" + note + "\n")

            with open(self.file, "w") as f:
                f.writelines(lines)

            self.update_var_list()

            # Will return the entry to its original state
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
        draw_board(self.board)

    def delete(self):
        self.notation.pop()
        self.board.pop()
        draw_board(self.board)
        self.update_scroll_list()

    def back(self):
        if self.putback < len(self.notation):
            self.putback += 1
            self.board.pop()
            draw_board(self.board)
            self.b7.config(state=tk.NORMAL)

            if self.putback == len(self.notation):
                self.b6.config(state=tk.DISABLED)

    def next(self):
        if self.putback > 0:
            self.board.push_san(self.notation[-self.putback])
            self.putback -= 1
            draw_board(self.board)
            self.b6.config(state=tk.NORMAL)

            if self.putback == 0:
                self.b7.config(state=tk.DISABLED)

    def end(self):
        clean_canvas([self.bm, self.b1, self.b2, self.b3, self.b4, self.b5,
                      self.b5, self.b6, self.b7, self.move_list, self.var_list,
                      self.e])
        OpeningLearnerMenu()


class OpeningLearner:
    def __init__(self, file) -> None:
        self.file = file
        window.title(self.file[:-4])

        # Creating a new canvas
        global w, h
        w = 60 * 8 + 20
        h = 60 * 8 + 20 + 100
        canvas.config(width=w, height=h, bg='white')

        # Variables for the on_click function
        self.position = "...."
        self.board = chess.Board()
        self.white_on_turn = True

        # Other variables
        self.variant = 0
        self.turn = 0

        # Getting info about opening
        with open(self.file, "r") as f:
            self.lines = f.readlines()

        self.names = []
        self.moves = []
        for line in self.lines:
            self.names.append(line[:line.index("##")])
            self.moves.append(line[line.index("##")+2:-2].split())

        # Chessboard rendering
        draw_board(None, 10, 60)

        # Button START
        self.bs = Button(canvas, text="START", command=self.opening_start,
                         height=2, width=20)
        self.bs.place(x=w-160-15, y=h-50)

        # Button MENU
        self.bm = Button(canvas, text="Menu", command=self.end,
                         height=2, width=20)
        self.bm.place(x=25, y=h-50)

        # Variant name
        self.title()

        canvas.mainloop()

    def opening_start(self):
        self.bs.destroy()

        draw_board(self.board, 10, 60)
        self.title()
        canvas.after(750, self.next_move)

        # Button hint
        self.bh = Button(canvas, text="Zopakuj", command=self.next_move,
                         height=2, width=20)
        self.bh.place(x=w-175, y=h-50)

        # Determining coordinates
        canvas.bind("<Button-1>", self.on_click)

    def title(self):
        canvas.create_text(w//2, 35, text=self.names[self.variant],
                           font=('Helvetica', '30', 'bold'))

    def on_click(self, action):
        x = action.x
        y = action.y
        if 10 < x < 60*8 + 10 and 50 < y < 60*8+50:
            file = chr(ord('a') + (x - 10) // 60)
            rank = str(8 - (y - 50) // 60)

            self.position += file + rank
            self.position = self.position[2:]

            try:
                if chess.Move.from_uci(self.position) in self.board.legal_moves:
                    # Correct move
                    if len(self.moves[self.variant]) > self.turn and \
                       self.position == self.moves[self.variant][self.turn]:
                        self.board.push_san(self.position)
                        draw_board(self.board, 10, 60)
                        self.title()
                        self.turn += 1
                        self.correct()
                        if len(self.moves[self.variant]) == self.turn:
                            self.variant += 1
                            self.turn = 0
                            canvas.after(750, self.next_variant)
                            return
                        canvas.after(750, self.next_move)
                    else:
                        self.wrong()
            except:
                pass

    def correct(self):
        self.l1 = Label(canvas, text="Správne",
                        font=('Helvetica', '23', 'bold'),
                        bg="lightgreen")
        self.l1.place(x=60*3+10, y=h-50)
        self.l1.after(500, self.l1.destroy)

    def wrong(self):
        self.l2 = Label(canvas, text="Nesprávne",
                        font=('Helvetica', '18', 'bold'),
                        bg="firebrick2")
        self.l2.place(x=60*3+10, y=h-47)
        self.l2.after(500, self.l2.destroy)

    def next_variant(self):
        if len(self.moves) > self.variant:
            self.board = chess.Board()
            draw_board(self.board, 10, 60)
            self.title()
            self.next_move()
        else:
            self.end()

    def next_move(self):
        # try - due to multiple presses of self.bn
        try:
            self.board.push_san(self.moves[self.variant][self.turn])
            draw_board(self.board, 10, 60)
            self.title()
            canvas.after(1000, self.one_move_back)
        except:
            pass

    def one_move_back(self):
        self.board.pop()
        draw_board(self.board, 10, 60)
        self.title()

    def end(self):
        if self.bs:
            clean_canvas([self.bm, self.bs])
        else:
            clean_canvas([self.bm, self.bh])
        OpeningLearnerMenu()


class OpeningReviewer:
    def __init__(self, file) -> None:
        self.file = file
        window.title(self.file[:-4])

        # Creating a new canvas
        global w, h
        w = 60 * 8 + 20
        h = 60 * 8 + 20 + 100
        canvas.config(width=w, height=h, bg='white')

        # Variables for the on_click function
        self.position = "...."
        self.board = chess.Board()
        self.white_on_turn = True

        # Other variables
        self.variant = 0
        self.turn = 0

        self.actual_misstake = 0
        self.misstakes = []
        self.correcting_misstakes = False

        # Getting info about opening
        with open(self.file, "r") as f:
            self.lines = f.readlines()

        self.names = []
        self.moves = []
        for line in self.lines:
            self.names.append(line[:line.index("##")])
            self.moves.append(line[line.index("##")+2:-2].split())

        # Chessboard rendering
        draw_board(None, 10, 60)

        # Button START
        self.bs = Button(canvas, text="START", command=self.opening_start,
                         height=2, width=20)
        self.bs.place(x=w-160-15, y=h-50)

        # Button MENU
        self.bm = Button(canvas, text="Menu", command=self.end,
                         height=2, width=20)
        self.bm.place(x=25, y=h-50)

        # Variant name
        self.title()

        canvas.mainloop()

    def opening_start(self):
        self.bs.destroy()

        draw_board(self.board, 10, 60)
        self.title()

        # Button NEXT
        self.bn = Button(canvas, text="Ďalej", command=self.next,
                         height=2, width=20)
        self.bn.place(x=w-175, y=h-50)

        # Determining coordinates
        canvas.bind("<Button-1>", self.on_click)

    def on_click(self, action):
        x = action.x
        y = action.y
        if 10 < x < 60*8 + 10 and 50 < y < 60*8+50:
            file = chr(ord('a') + (x - 10) // 60)
            rank = str(8 - (y - 50) // 60)

            self.position += file + rank
            self.position = self.position[2:]

            try:
                if chess.Move.from_uci(self.position) in self.board.legal_moves:
                    # Correct move
                    if not self.correcting_misstakes:
                        if len(self.moves[self.variant]) > self.turn and \
                               self.position == self.moves[self.variant][self.turn]:
                            self.board.push_san(self.position)
                            draw_board(self.board, 10, 60)
                            self.title()
                            self.turn += 1
                            self.correct()
                        else:
                            self.wrong()

                    else:
                        if len(self.moves[self.variant]) > self.turn and \
                           self.position == self.moves[self.variant][self.turn]:
                            self.board.push_san(self.position)
                            draw_board(self.board, 10, 60)
                            self.title()
                            self.correct()

                            canvas.after(500, self.handle_correct_move)

                        else:
                            self.board.push_san(self.position)
                            draw_board(self.board, 10, 60)
                            self.title()
                            self.wrong()

                            canvas.after(500, self.handle_wrong_move)
            except:
                pass

    def title(self):
        canvas.create_text(w//2, 35, text=self.names[self.variant],
                           font=('Helvetica', '30', 'bold'))

    def handle_correct_move(self):
        self.fixed[self.actual_misstake] += 1

        if self.fixed[self.actual_misstake] == 3:
            self.misstakes.pop(self.actual_misstake)
            self.fixed.pop(self.actual_misstake)

            if self.misstakes == [] and len(self.moves) > self.variant:
                self.correcting_misstakes = False
                self.board = chess.Board()
                draw_board(self.board, 10, 60)

                self.turn = 0
                self.variant += 1
                self.title()

            elif len(self.moves)-1 == self.variant:
                self.end()

        if self.actual_misstake+1 == len(self.misstakes):
            self.actual_misstake = 0
            self.load_board(self.misstakes[self.actual_misstake])
        elif self.actual_misstake+1 < len(self.misstakes):
            self.actual_misstake += 1
            self.load_board(self.misstakes[self.actual_misstake])

    def handle_wrong_move(self):
        self.fixed[self.actual_misstake] = 0

        if self.actual_misstake+1 != len(self.misstakes):
            self.load_board(self.misstakes[self.actual_misstake+1])
        else:
            self.actual_misstake = 0
            self.load_board(self.misstakes[self.actual_misstake])

    def load_board(self, n):
        self.board = chess.Board()
        self.turn = n
        for i in range(n):
            self.board.push_san(self.moves[self.variant][i])

        draw_board(self.board, 10, 60)
        self.title()

    def next(self):
        # self.correcting_misstakes == True
        if self.misstakes != [] and \
           self.turn == len(self.moves[self.variant]) and \
           not self.correcting_misstakes:
            self.correcting_misstakes = True
            self.fixed = [0] * len(self.misstakes)
            self.load_board(self.misstakes[0])
            self.correct()

        elif self.correcting_misstakes and \
                self.turn == len(self.moves[self.variant]):
            self.handle_correct_move()
            self.correct()

        elif self.correcting_misstakes and \
                self.turn != len(self.moves[self.variant]):
            self.handle_wrong_move()
            self.wrong()

        # self.correcting_misstakes == False
        elif len(self.moves)-1 == self.variant and \
                self.turn == len(self.moves[self.variant]):
            self.end()

        elif self.turn == len(self.moves[self.variant]):
            self.board = chess.Board()
            draw_board(self.board, 10, 60)

            self.turn = 0
            self.variant += 1
            self.title()
            self.correct()

        else:
            self.wrong()

    def correct(self):
        self.l1 = Label(canvas, text="Správne",
                        font=('Helvetica', '23', 'bold'),
                        bg="lightgreen")
        self.l1.place(x=60*3+10, y=h-50)
        self.l1.after(500, self.l1.destroy)

    def wrong(self):
        self.l2 = Label(canvas, text="Nesprávne",
                        font=('Helvetica', '18', 'bold'),
                        bg="firebrick2")
        self.l2.place(x=60*3+10, y=h-47)
        if self.turn not in self.misstakes:
            self.misstakes.append(self.turn)
        self.l2.after(500, self.l2.destroy)

    def end(self):
        if self.bs:
            clean_canvas([self.bm, self.bs])
        else:
            clean_canvas([self.bm, self.bn])
        OpeningLearnerMenu()
