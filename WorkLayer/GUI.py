from tkinter import *

from DataAccess.DataReceiver import DataReceiver
from Interface.klebi import klebi


class GUI:
    root = Tk()

    fi = klebi(root, 0, [['Name', 's'], ['Quantity(g)', 'n'], ['Calories(per 100g)', 'n'], ['Buy Date', 'd'],
                         ['Expiration Date', 'd']], "Food item")
    dp = klebi(root, 7, [['Name', 's'], ['Address', 's'], ['Contact', 's']], "Donation place")
    ei = klebi(root, 11, [['Name', 's'], ['Quantity', 'n']], "Eaten item")
    di = klebi(root, 14, [['Place', 's'], ['Name', 's'], ['Quantity', 'n']], "Donated item")
    # KLEB for goals
    # KLEB for other stuff

    date1 = Entry(root)
    date1.grid(row=19, column=0, sticky=W + E, columnspan=1)

    datelabel = Label(root, text="<- From                  To ->")
    datelabel.grid(row=19, column=1, sticky=W + E, columnspan=1)

    date2 = Entry(root)
    date2.grid(row=19, column=2, sticky=W + E, columnspan=1)

    nextday = Button(root, text="Next Day")
    nextday.grid(row=18, column=0, sticky=W + E, columnspan=3)

    report7 = Button(root, text="Weekly Report")
    report7.grid(row=20, column=0, sticky=W + E, columnspan=3)

    report30 = Button(root, text="Monthly Report")
    report30.grid(row=21, column=0, sticky=W + E, columnspan=3)

    report_entry = Entry(root)
    report_entry.grid(row=22, column=0, sticky=W + E, columnspan=3)

    nextday.bind("<Button-1>", DataReceiver("Next day", []))
    report7.bind("<Button-1>", DataReceiver("Weekly report", [date1.get(), date2.get(), report_entry]))
    report30.bind("<Button-1>", DataReceiver("Monthly report", [date1.get(), date2.get(), report_entry]))

    root.mainloop()
