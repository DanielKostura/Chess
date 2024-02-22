from tkinter import *

def on_select(event):
    # Get the index of the selected item
    index = mylist.curselection()
    if index:
        # Retrieve the text of the selected item
        selected_item = mylist.get(index)
        # Print different messages based on the selected item
        if selected_item == "This is line number 1":
            print("ahoj")
        elif selected_item == "This is line number 2":
            print("BU")

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set)
for line in range(1, 100):
    mylist.insert(END, str(line) + ". This is line number")

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)

# Bind left mouse button click event to on_select function
mylist.bind('<Button-1>', on_select)

mainloop()
