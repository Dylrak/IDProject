from Tkinter import *
import IO

class GUI(Frame):
    def createMenu(self):
        ingang = \
            Button(self, text="Ingang", command = lambda: IO.GateProcess(True))
        ingang.pack(fill=X)

        uitgang = \
            Button(self, text = "Uitgang", command = lambda: IO.GateProcess(False))
        uitgang.pack(fill=X)

        registratie = \
            Button(self, text = "Registratie", command = lambda: IO.GateProcess(False))
        registratie.pack(fill=X)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createMenu()
        self.pack()
        self.mainloop()


class main:
    def __init__(self):
        root = Tk()
        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)
        gui = GUI(master=root)
main()
