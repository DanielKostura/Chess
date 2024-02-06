import tkinter

def draw_board(current_canvas: Tk, pieces: bool,
               chess_board: list[list[str]]=[[""]], bonus_x=0, bonus_y=0):
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