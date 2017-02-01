from Tkinter import *
import IO
import re
from datetime import datetime


class GUI(Frame):
    def __init__(self, master):
        self.root = Tk()
        Frame.__init__(self, master)
        self.createMenu()
        self.pack()
        self.root.mainloop()

    def createMenu(self):
        ingang = \
            Button(self.root, text="Ingang", command = lambda: IO.GateProcess(True))
        ingang.pack(fill=X)

        uitgang = \
            Button(self.root, text = "Uitgang", command = lambda: IO.GateProcess(False))
        uitgang.pack(fill=X)

        registratie = \
            Button(self.root, text = "Registratie", command = lambda: self.registratieWindow)
        registratie.pack(fill=X)

    def registratieWindow(self):
        window = Toplevel(self.root)
        labels = ('Voornaam', 'Achternaam', 'Emailadres', 'IBAN', 'Geboortedatum', 'Straatnaam', 'Huisnummer', 'Plaats', 'Postcode')

        def makeform(root, fields):
            entries = []
            for field in fields:
                row = Frame(root)
                lab = Label(row, width=15, text=field, anchor='w')
                ent = Entry(row)
                row.pack(side=TOP, fill=X, padx=5, pady=5)
                lab.pack(side=LEFT)
                ent.pack(side=RIGHT, expand=YES, fill=X)
                entries.append((field, ent))
            return entries

        def fetch(entries):
            invalid_entry = None
            for entry in entries:
                field = entry[0]
                text = entry[1].get()
                regex = None
                if field in ['Voornaam', 'Achternaam', 'Straatnaam', 'Plaats']:
                    regex = "[A-Za-z0-9\-\. ]{3,64}"
                elif field is 'Emailadres':
                    regex = "([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)"
                elif field is 'IBAN':
                    regex = "[a-zA-Z]{2}[0-9]{2}[a-zA-Z0-9]{4}[0-9]{7}([a-zA-Z0-9]?){0,16}"
                elif field is 'Huisnummer':
                    regex = "\d{1,4}"
                elif field is 'Postcode':
                    regex = "\d{4}[a-zA-Z]{2}"
                elif field is 'Geboortedatum':  # Regex usage is done beforehand to ensure the input is valid in both
                    # syntax and information. We use breaks or continues to skip the regex match at the bottom.
                    regex = "(\d{2})\-(\d{2})\-(\d{4})"
                    match = re.search(regex, text)
                    if not match:
                        invalid_entry = field
                        break
                    else:
                        correctDate = None
                        try:
                            newDate = datetime(match.group(3), match.group(2), match.group(1))
                            correctDate = True
                        except ValueError:
                            correctDate = False
                            invalid_entry = field
                            break
                        continue
                if not re.match(regex, text):
                    invalid_entry = field
                    break
            if invalid_entry is None:
            # TODO: All input valid. Continue to NFC registration
                pass
            else:
                error_text = invalid_entry + " is ongeldig. Voer alstublieft de juiste gegevens in."
                error = Toplevel()
                errorLabel = Label(error, text=error_text, height=0, width=100)
                errorLabel.pack()


        ents = makeform(window, labels)
        b1 = Button(window, text='Show',
                    command=(lambda e=ents: fetch(e)))
        b1.pack(side=LEFT, padx=5, pady=5)


class main:
    def __init__(self):
        gui = GUI(master=None)
main()
