from Tkinter import *
import Gates

class GUI(Frame):
    def createMenu(self):
        self.ingang = Button(self)
        self.ingang["text"] = "Ingang"
        self.ingang["command"] = lambda: Gates.GateProcess(True)

        self.ingang.pack({"side": "left"})

        self.uitgang = Button(self)
        self.uitgang["text"] = "Uitgang"
        self.uitgang["command"] = lambda: Gates.GateProcess(False)

        self.uitgang.pack({"side": "right"})
        self.registratie = Button(self)
        self.registratie["text"] = "Registratie"

        self.registratie.pack()
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createMenu()
        self.currentThread = None


class main:
    def __init__(self):
        root = Tk()
        gui = GUI(master=root)
        gui.mainloop()
main()
