# Stands for K Layers and Entries with one button interface, a bit warped but dry

from tkinter import *
from Interface.EntryDefaultFunctions import *
from DataAccess.DataReceiver import DataReceiver
from WorkLayer.Verifier import Verifier

entryDefaultfunc = {'s': entryStringDefault, 'n': entryNumberDefault, 'd': entryDateDefault}
V = Verifier


# Example use :
#
# ro =Tk()
#
# c = KLEB(ro,0,[['Name','s'],['Address','s'],['Contact','s']],"Donation place")

class klebi:  # k labels/entries & 1 button

    def __init__(self, root, idxstart, labelandtype, entity_type):

        self.labels = []
        self.entries = []
        self.data = []

        frame = Frame(root)
        idx = 0

        self.infolabel = Label(root, text=("" + entity_type + " info"))
        self.infobox = Entry(root)
        self.infobox.grid(columnspan=2, sticky=W + E)

        self.infolabel.grid(row=idx + idxstart, column=0)
        self.infobox.grid(row=idx + idxstart, column=1)

        for label_name in labelandtype:
            self.labels.append(Label(root, text=label_name[0]))
            self.entries.append(Entry(root))

            self.labels[idx].grid(row=idx + idxstart + 1, column=0)  # +1 because of info label

            self.entries[idx].grid(row=idx + idxstart + 1, column=1)
            self.entries[idx].bind('<Double-Button-1>', entryDefaultfunc[labelandtype[idx][1]])
            # lambda event: (entryDefaultfunc[labelandtype[idx][1]]) (event,self.entries[idx]))

            idx += 1

        self.button = Button(root, text="Add " + entity_type)
        self.button.grid(row=idx + idxstart, column=2, sticky=W + E)

        def button_get_data(inner_self):
            for idx in range(0, len(self.entries)):
                if labelandtype[idx][1] == 'n':
                    auxstr = self.entries[idx].get()
                    self.entries[idx].delete(0,'end')
                    try:
                        self.entries[idx].insert(0,float(str(auxstr)))
                    except:
                        ValueError# waiting for a better solution to solve issues with tkinter entries

                if labelandtype[idx][1] == 'n' and V.numberVerifier(float(str(self.entries[idx].get()))) \
                        or labelandtype[idx][1] == 's' and V.stringVerifier(self.entries[idx].get()) \
                        or labelandtype[idx][1] == 'd' and V.dateVerifier(self.entries[idx].get()):
                    self.data.append(self.entries[idx].get())
                    # print(self.entries[idx].get())
                else:
                    self.infobox.delete(0, 'end')
                    self.infobox.insert(0, "Invalid input(" + self.entries[idx].get() + ") " + " in the " +
                                        labelandtype[idx][0] + " field!")
                    self.data.clear()
                    return
            dr = DataReceiver(entity_type, self.data)

        self.button.bind("<Button-1>", button_get_data)
