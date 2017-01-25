from Tkinter import *
import Gates

class GUI(Frame):
    def createMenu(self):
        ingang = \
            Button(self, text="Ingang", command = lambda: Gates.GateProcess(True), sticky=W)
        ingang.grid(row=0, column=0)

        uitgang = \
            Button(self, text = "Uitgang", command = lambda: Gates.GateProcess(False), sticky=E)
        uitgang.grid(row=0, column = 1)

        registratie = \
            Button(self, text = "Registratie", command = lambda: Gates.GateProcess(False), sticky = S)
        registratie.grid(row=1, column = 0)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createMenu()
        self.mainloop()


class main:
    def __init__(self):
        root = Tk()
        Grid.rowconfigure(root, 0, weight=1)
        Grid.columnconfigure(root, 0, weight=1)
        gui = GUI(master=root)
main()
