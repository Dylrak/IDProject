from Tkinter import *
from IO import GateProcess, getNFCUID
import re
from datetime import datetime
from Database import *


class GUI(Frame):
    def __init__(self, master):
        self.root = Tk()
        Frame.__init__(self, master)
        self.createMenu()
        self.pack()
        self.root.mainloop()

    def createMenu(self):
        ingang = \
            Button(self.root, text="Ingang", command = lambda: GateProcess(True))
        ingang.pack(fill=X)

        uitgang = \
            Button(self.root, text = "Uitgang", command = lambda: GateProcess(False))
        uitgang.pack(fill=X)

        lopendeband = \
            Button(self.root, text="Lopende band", command=lambda: customerDevice(1, getNFCUID()))
        lopendeband.pack(fill=X)

        spinning = \
            Button(self.root, text="Spinning", command=lambda: customerDevice(2, getNFCUID()))
        spinning.pack(fill=X)

        registratie = \
            Button(self.root, text="Registratie", command=lambda: self.registratieWindow())
        registratie.pack(fill=X)

    def registratieWindow(self):
        window = Toplevel(self.root)
        labels = ('Voornaam', 'Achternaam', 'Emailadres', 'IBAN', 'Geboortedatum', 'Straatnaam', 'Huisnummer', 'Plaats', 'Postcode', 'Gebruikersnaam')

        def makeform(root, fields):
            entries = []
            for field in fields:
                row = Frame(root)
                lab = Label(row, width=15, text=field, anchor='w')
                ent = Entry(row)
                row.pack(side=TOP, fill=X, padx=5)
                lab.pack(side=LEFT)
                ent.pack(side=RIGHT, expand=YES, fill=X)
                entries.append((field, ent))
            row = Frame(root)
            lab = Label(row, width=15, text='Kies wachtwoord', anchor='w')
            ent = Entry(row, show="*")
            row.pack(side=TOP, fill=X, padx=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append(('Kies wachtwoord', ent))
            return entries

        def fetch(entries):
            invalid_entry = None
            data = []
            for entry in entries:
                field = entry[0]
                text = entry[1].get()
                if text is None:
                    invalid_entry = field
                    break
                regex = None
                if field in ['Voornaam', 'Achternaam', 'Straatnaam', 'Plaats', 'Gebruikersnaam']:
                    regex = "[A-Za-z0-9\-\. ]{3,64}"
                elif field == 'Emailadres':
                    regex = "([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)"
                elif field == 'IBAN':
                    regex = "[a-zA-Z]{2}[0-9]{2}[a-zA-Z0-9]{4}[0-9]{7}([a-zA-Z0-9]?){0,16}"
                elif field == 'Huisnummer':
                    regex = "\d{1,4}"
                elif field == 'Postcode':
                    regex = "\d{4}[a-zA-Z]{2}"
                elif field == 'Kies wachtwoord':
                    regex = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
                elif field == 'Geboortedatum':  # Regex usage is done beforehand to ensure the input is valid in both
                    # syntax and information. We use breaks or continues to skip the regex match at the bottom.
                    regex = "(\d{1,2})\-(\d{1,2})\-(\d{4})"
                    match = re.search(regex, text)
                    if not match:
                        invalid_entry = field
                        break
                    else:
                        try:
                            newDate = datetime(int(match.group(3)), int(match.group(2)), int(match.group(1)))
                            data.append(text)
                        except ValueError:
                            invalid_entry = field
                            break
                        continue
                if not re.match(regex, text):
                    invalid_entry = field
                    break
                else:
                    data.append(text)
            if invalid_entry is None:
                uID = getNFCUID()
                data.insert(0, uID)
                addCustomer(data)  # send all but username and password to customer database column
                window.destroy()
            else:
                if field == 'Kies wachtwoord':
                    error_text = "Wachtwoord moet minimaal 8 tekens zijn en heeft 1 letter en 1 nummer nodig."
                else:
                    error_text = invalid_entry + " is ongeldig. Voer alstublieft de juiste gegevens in."
                error = Toplevel(window)
                errorLabel = Label(error, text=error_text)
                errorLabel.pack()


        ents = makeform(window, labels)
        b1 = Button(window, text='Scan NFC-chip',
                    command=(lambda e=ents: fetch(e)))
        b1.pack(side=RIGHT, padx=5, pady=5)


class main:
    def __init__(self):
        gui = GUI(master=None)
main()
