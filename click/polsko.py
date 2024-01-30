from tkinter import *
import random

running = True

def polsko(udalost):
    x = udalost.x
    y = udalost.y
    a = 10

    if y < vyska // 2:
        farba = "white"
    else:
        farba = "red"
    
    platno.create_rectangle(x-a, y-a, x+a, y+a, fill=farba)

def taliansko(udalost):
    x = udalost.x
    y = udalost.y
    a = 10

    if x < sirka // 3:
        farba = "red"
    elif x > sirka // 3 and x < sirka // 3*2:
        farba = "white"
    else:
        farba = "green"
    
    platno.create_rectangle(x-a, y-a, x+a, y+a, fill=farba)

def francuzsko(udalost):
    start()
    while running:
        x = random.randint(0, sirka)
        y = random.randint(0, vyska)
        a = 10

        if x < sirka // 3:
            farba = "blue"
        elif x > sirka // 3 and x < sirka // 3*2:
            farba = "white"
        else:
            farba = "red"

        platno.create_rectangle(x-a, y-a, x+a, y+a, fill=farba)

        platno.update()
        platno.after(10)

def stop(udalost):
    global running
    running = False

def start():
    global running
    running = True

def delete(udalost):
    platno.delete("all")


okno=Tk()
okno.title('Graficka plocha')
vyska = 800
sirka = 800
platno = Canvas(width=sirka, height=vyska)
platno.pack()


platno.bind("<Button-1>", polsko)
platno.bind("<B1-Motion>", taliansko)

platno.bind_all("f", francuzsko)
platno.bind_all("s", stop)

platno.bind_all("q", delete)

okno.mainloop()