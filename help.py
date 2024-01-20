import tkinter as tk

def destroy_button():
    # Destroy the button
    function.button.destroy()

# Create the main window
root = tk.Tk()
root.title("Button Destroy Example")

# Create a button
def function():
    function.button = tk.Button(root, text="Click me to destroy", command=destroy_button)
    function.button.pack(pady=20)

function()
# Start the Tkinter event loop
root.mainloop()
