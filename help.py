import tkinter as tk

def clean_canvas():
    # Delete all objects on the canvas
    canvas.delete("all")
    
    # Destroy or remove buttons, labels, and entries
    for widget in [button1, label1, entry1]:
        widget.destroy()

# Create the main window
root = tk.Tk()
root.geometry("400x400")

# Create a canvas
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Add some objects to the canvas
canvas.create_rectangle(50, 50, 150, 150, fill="blue")

# Create some other widgets
button1 = tk.Button(root, text="Clean Canvas", command=clean_canvas)
button1.pack()

label1 = tk.Label(root, text="Label")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

# Run the Tkinter event loop
root.mainloop()