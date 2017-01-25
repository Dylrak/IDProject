from tkinter import *
import Gates
import threading


class GUI(Frame, threading.Thread):
    def createMenu(self):
        self.ingang = Button(self)
        self.ingang["text"] = "Ingang"
        self.ingang["command"] = lambda: self.startNewThread(self.ingang["text"])

        self.ingang.pack({"side": "left"})

        self.uitgang = Button(self)
        self.uitgang["text"] = "Uitgang"
        self.uitgang["command"] = lambda: self.startNewThread(self.ingang["text"])

        self.uitgang.pack({"side": "right"})
    def __init__(self,threadName, master=None ):
        Frame.__init__(self, master)
        self.name = threadName
        threading.Thread.__init__(self)
        self.pack()
        self.createMenu()
        self.currentThread = None

    def startNewThread(self, mode):
        if self.currentThread is None:
            if mode is "Ingang":
                self.currentThread = Gates.GateProcess(mode)
                self.currentThread.start(True)
            elif mode is "Uitgang":
                self.currentThread = Gates.GateProcess(mode)
                self.currentThread.start(False)
            self.currentThread.join()
            self.currentThread = None

class main:
    def __init__(self):
        root = Tk()
        gui = GUI(master=root)
        gui.mainloop()
        root.destroy()
main()
