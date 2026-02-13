# How to install chess module?
For Windows: 
   pip install chess
For Mac or Linux:
   python -m pip install chess

# File structure
chess_app/
│
├── main.py                            # start app
├── gui/
│   ├── game/                          # GUI for games
│   │   ├── ai_game.py
│   │   ├── pvp_game.py
│   │   ├── start_pvp_game.py
│   │
│   ├── menus/                         # GUI for menus
│   │   ├── ai_menu.py
│   │   ├── game_menu.py
│   │   ├── menu.py
│   │   ├── opening_menu.py
│   │
│   ├── opening_gui/
│   │   ├── opening_creator.py
│   │   ├── opening_learner.py
│   │   ├── opening_reviewer.py
│   │
│   ├── timer/
│   │   ├── timer_controller.py
│   │   ├── time_view.py
│   │
│   ├── base_screen.py                 # handle lifecycle of witgets
│   ├── board_view.py                  # handle
│   ├── game_controller.py
│   ├── screen_manager.py
│   ├── visual_efects.py
│   
├── logic/
│   ├── opening_logic/                 # handle opening logic
│   │   ├── creator_manager.py
│   │   ├── learner_manager.py
│   │   ├── reviewer_manager.py
│   │   ├── opening_manager.py
│   │
│   ├── ai_manager.py                  # 
│   ├── chess_rules.py
│   ├── file_operations.py
│   ├── match_manager.py
│   ├── timer.py
│   
├── openings/
│   ├── {user`s_opening_name}.txt
│   
├── ui_component/
│   ├── listbox_manager.py
│   ├── notation_panel.py
│   ├── variant_panel.py
│
├── utils/
│   ├── chess_utils.py


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