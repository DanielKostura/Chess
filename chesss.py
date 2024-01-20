from tkinter import *
import tkinter as tk


def chess_borard(current_canvas, pieces, bonus_x=0, bonus_y=0):
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
                # pawns
                if row == 1:
                    current_canvas.create_text(x+40, y+40,
                                               text="♟", font=('Helvetica','50','bold'))
                elif row == 6:
                    current_canvas.create_text(x+40, y+40,
                                               text="♙", font=('Helvetica','50','bold'))
                
                # rooks
                elif row == 0 and (column == 0 or column == 7):
                    current_canvas.create_text(x+40, y+40,
                                               text="♜", font=('Helvetica','50','bold'))
                elif row == 7 and (column == 0 or column == 7):
                    current_canvas.create_text(x+40, y+40,
                                               text="♖", font=('Helvetica','50','bold'))
                
                # nights
                elif row == 0 and (column == 1 or column == 6):
                    current_canvas.create_text(x+40, y+40,
                                               text="♞", font=('Helvetica','50','bold'))
                elif row == 7 and (column == 1 or column == 6):
                    current_canvas.create_text(x+40, y+40,
                                               text="♘", font=('Helvetica','50','bold'))
                
                # bishops
                elif row == 0 and (column == 2 or column == 5):
                    current_canvas.create_text(x+40, y+40,
                                               text="♝", font=('Helvetica','50','bold'))
                elif row == 7 and (column == 2 or column == 5):
                    current_canvas.create_text(x+40, y+40,
                                               text="♗", font=('Helvetica','50','bold'))
                
                # queen
                elif row == 0 and  column == 3:
                    current_canvas.create_text(x+40, y+40,
                                               text="♛", font=('Helvetica','50','bold'))
                elif row == 7 and column == 3:
                    current_canvas.create_text(x+40, y+40,
                                               text="♕", font=('Helvetica','50','bold'))
                
                # kings
                elif row == 0 and column == 4:
                    current_canvas.create_text(x+40, y+40,
                                               text="♚", font=('Helvetica','50','bold'))
                elif row == 7 and column == 4:
                    current_canvas.create_text(x+40, y+40,
                                               text="♔", font=('Helvetica','50','bold'))

def blitz_start():
    chess_borard(blitz.canvas, True, 0, 50)

# ----------------------- menu buttons -----------------------
def buttons():
    Button(menu_canvas, text = "Blitz", command=blitz, height= 3, width=30).place(x = 80*9, y = 100)
    Button(menu_canvas, text = "Rapid", command=rapid, height= 3, width=30).place(x = 80*9, y = 100+75)
    Button(menu_canvas, text = "Precvičenie otvorení", command=openings, height= 3, width=30).place(x = 80*9, y = 100+75*2)
    Button(menu_canvas, text = "Pravidlá", command=rules, height= 3, width=30).place(x = 80*9, y = 500)

def blitz():
    menu_window.destroy()

    blitz_window = tk.Tk()  # Vytvořte nové okno
    blitz_window.title('Blitz')

    W = 80 * 8 + 20
    H = 80 * 8 + 20 + 100
    blitz.canvas = Canvas(width=W, height=H, bg='white')
    blitz.canvas.pack()

    chess_borard(blitz.canvas, False, 0, 50)
    b = Button(blitz.canvas, text="START", command=blitz_start, height=3, width=30)
    b.place(x=W//2, y=H//2)

    blitz.canvas.mainloop()
    
def rapid():
    menu_window.destroy()
    rapid_window = Tk()  # Vytvořte nové okno
    rapid_window.title('Rapid')

    W = 80 * 8 + 20
    H = 80 * 8 + 20
    rapid_canvas = Canvas(width=W, height=H, bg='white')
    rapid_canvas.pack()

    chess_borard(rapid_canvas, 0, 20)
    rapid_canvas.mainloop()

def openings():
    menu_window.destroy()
    rules_window = Tk()  # Vytvořte nové okno
    rules_window.title('Pravidlá šachu')

    W = 500
    H = 500
    p = Canvas(width=W, height=H,bg='white')
    p.pack()

def rules():
    menu_window.destroy()
    rules_window = Tk()  # Vytvořte nové okno
    rules_window.title('Pravidlá šachu')

    W = 500
    H = 500
    p = Canvas(width=W, height=H,bg='white')
    p.pack()

    p.create_text(W//2, 30, text = "DDD", fill="black")
# ----------------------- menu buttons -----------------------

menu_window = Tk()
menu_window.title("Menu")

W = 1000
H = 80 * 8 + 20
menu_canvas = Canvas(width=W, height=H,bg='white')
menu_canvas.pack()

buttons()
chess_borard(menu_canvas, False)
menu_canvas.mainloop()