def wordeasy3_label(label):
    def wordeasy3():
        global i
        if i != 3: 
            label.config(text=(list[i]))
            label.place(x=0,y=0)
            i+=1
            label.after(2000, wordeasy3)
        else:
            label.destroy()
    wordeasy3()