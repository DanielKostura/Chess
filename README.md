# How to install chess module?
For Windows: 
   pip install chess
For Mac or Linux:
   python -m pip install chess

# File structure
chess_app/
│
├── main.py                # start app
├── gui/
│   ├── canvas.py          # draw_board, clean_canvas
│   ├── menu.py            # Menu, GameMenu, BotMenu
│   ├── game_gui.py        # GUI for Game
│   ├── opening_gui.py     # OpeningCreator, Learner, Reviewer
│
├── logic/
│   ├── game.py            # class Game (without Tkinter)
│   ├── timer.py           # Timer
│   ├── openings.py        # work with fikes .txt
│
├── utils/
│   └── chess_utils.py     # create_chess_array

# Not implemented
BotMenu

# Chess
NEFUNGUJE
1. funkcia delete v classe OpeningCreator obcas nevymazuje dobre