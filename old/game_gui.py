from tkinter import Tk, Canvas

class Game:
    def __init__(self, window: Tk, canvas: Canvas,
                 time: int, bonus: int) -> None:
        window.title('Hra s priteľom')

        # Rendering new canvas
        global w, h
        w = 60 * 8 + 20
        h = 60 * 8 + 20 + 100
        canvas.config(width=w, height=h, bg='white')

        self.time = time
        self.bonus = bonus

        # Variables for piece_move function
        self.position = "...."
        self.board = chess.Board()
        self.white_on_turn = True

        # Chessboard rendering
        draw_board(None, 10, 60)

        # Button START
        self.b1 = Button(canvas, text="START", command=self.game_start,
                         height=2, width=20)
        self.b1.place(x=w-160-15, y=h-50)

        canvas.mainloop()

    def game_start(self):
        self.b1.destroy()

        draw_board(self.board, 10, 60)

        # Button menu
        self.bm = Button(canvas, text="Menu", command=self.game_end,
                         height=2, width=20)
        self.bm.place(x=w-160-15, y=h-50)

        # Timers
        global black_timer, white_timer
        black_timer = Timer(self.time, self.bonus, 10+15, 10)
        white_timer = Timer(self.time, self.bonus, 10+15, h-50)

        white_timer.start_timer()

        # Determining coordinates
        canvas.bind("<Button-1>", self.on_click)

    def on_click(self, action):
        x = action.x
        y = action.y
        if white_timer.time > 0 and black_timer.time > 0 and \
           10 < x < 60*8 + 10 and 60 < y < 60*9:
            file = chr(ord('a') + (x - 10) // 60)
            rank = str(8 - (y - 60) // 60)

            self.position += file + rank
            self.position = self.position[2:]

            try:
                if chess.Move.from_uci(self.position) in self.board.legal_moves:
                    # Making a move
                    self.board.push_san(self.position)

                    # Timer changes
                    if self.board.turn == chess.WHITE:
                        white_timer.start_timer()
                        black_timer.stop_timer()
                    else:
                        black_timer.start_timer()
                        white_timer.stop_timer()

                    # Chessboard rendering
                    draw_board(self.board, 10, 60)
            except:
                pass

            if self.board.is_checkmate():
                white_timer.stop_timer()
                black_timer.stop_timer()
                canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                        fill="lightgrey", outline="black")
                canvas.create_text((60*8+20)//2 - 5,
                                   (60*8+20+100)//2,
                                   text="VÝHRA",
                                   font=('Helvetica', '50', 'bold'))
                if self.board.turn == chess.BLACK:
                    canvas.create_text((60*8+20)//2,
                                       (60*8+20+100)//2 + 40,
                                       text="Biely vyhral šachmatom",
                                       font=('Helvetica', '15', 'bold'))
                else:
                    canvas.create_text((60*8+20)//2,
                                       (60*8+20+100)//2 + 40,
                                       text="Čierny vyhral šachmatom",
                                       font=('Helvetica', '15', 'bold'))
            elif self.board.is_stalemate():
                white_timer.stop_timer()
                black_timer.stop_timer()
                canvas.create_rectangle(60, 60+60*3, 15+60*7, 60*6,
                                        fill="grey", outline="black")
                canvas.create_text((60*8+20)//2 - 5,
                                   (60*8+20 + 100)//2,
                                   text="REMÍZA",
                                   font=('Helvetica', '50', 'bold'))
                canvas.create_text((60*8+20)//2,
                                   (60*8+20+100)//2 + 40,
                                   text="Patová situácia",
                                   font=('Helvetica', '15', 'bold'))
            elif self.board.is_insufficient_material():
                white_timer.stop_timer()
                black_timer.stop_timer()
                canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                        fill="lightgrey", outline="black")
                canvas.create_text((60*8+20)//2 - 5,
                                   (60*8+20+100)//2,
                                   text="REMÍZA",
                                   font=('Helvetica', '50', 'bold'))
                canvas.create_text((60*8+20)//2,
                                   (60*8+20+100)//2 + 40,
                                   text="Nedostatok materiálu",
                                   font=('Helvetica', '15', 'bold'))
            elif self.board.can_claim_threefold_repetition():
                white_timer.stop_timer()
                black_timer.stop_timer()
                canvas.create_rectangle(5+60, 60+60*3, 15+60*7, 55+60*5,
                                        fill="lightgrey", outline="black")
                canvas.create_text((60*8+20)//2,
                                   (60*8+20+100)//2 - 5,
                                   text="REMÍZA",
                                   font=('Helvetica', '50', 'bold'))
                canvas.create_text((60*8+20)//2,
                                   (60*8+20+100)//2 + 40,
                                   text="Opakovanie ťahou",
                                   font=('Helvetica', '15', 'bold'))

    def game_end(self):
        clean_canvas([self.bm, black_timer.time_label, white_timer.time_label])
        Menu()