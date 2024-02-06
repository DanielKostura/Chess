def on_click(action):
        x = action.x
        y = action.y

        if 10 < x < 60*8 + 10 and 60 < y < 60*9:
            file = chr(ord('a') + (x - 10) // 60)
            rank = str(8 - (y - 60) // 60)
            position = file + rank

            print(position)