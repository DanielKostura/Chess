from tkinter import Button


def blink(btn: Button, new_color: str, org_color: str = "SystemButtonFace") -> None:
    btn.config(bg=new_color)
    btn.after(1000, lambda: _reset_color(btn, org_color))

def _reset_color(btn: Button, org_color: str) -> None:
    btn.config(bg=org_color)