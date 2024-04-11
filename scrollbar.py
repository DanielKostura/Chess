import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("400x300")

# Create a frame to hold the scrollable content
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=1)

# Create a canvas widget
canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Add a thin scroll bar
style = ttk.Style()
style.theme_use('clam')  # Use any theme that provides a thin scrollbar
style.configure('My.Horizontal.TScrollbar', gripcount=0, background='gray', troughcolor='lightgray', bordercolor='lightgray', lightcolor='lightgray', darkcolor='lightgray', arrowcolor='white')
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, style='My.Horizontal.TScrollbar', command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the canvas to use the scrollbar
canvas.configure(yscrollcommand=scrollbar.set)

# Bind the canvas to the scroll region
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a frame to contain the widgets
scrollable_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Add some widgets to the scrollable frame
for i in range(50):
    ttk.Label(scrollable_frame, text="Label " + str(i)).pack()

root.mainloop()
