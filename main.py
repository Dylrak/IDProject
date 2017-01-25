from tkinter import *
import Gates


class GUI:
    def __init__(self):
        root = Tk()
        b = \
            Button(root, text="Ingang", command=Gates.GateProcess(True)).\
                grid(row=0, column = 0)
        b.pack()
        b = \
            Button(root, text="Uitgang", command=Gates.GateProcess(False)).\
                grid(row=0, column = 1)
        b.pack
        root.mainloop()
