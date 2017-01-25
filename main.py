from Tkinter import *
import Gates

class GUI(Frame):
    def createMenu(self):
        self.uitgang = \
            Button(self, text="Ingang", command = lambda: Gates.GateProcess(True))\
                .grid(row=0, column=0)

        self.uitgang = \
            Button(self, text = "Uitgang", command = lambda: Gates.GateProcess(False))\
                .grid(row=0, column = 1)

        self.registratie = \
            Button(self, text = "Registratie", command = lambda: Gates.GateProcess(False))\
                .grid(row=1, column = 0, rowspan=2)
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createMenu()


class main:
    def __init__(self):
        root = Tk()
        gui = GUI(master=root)
        gui.mainloop()
main()
