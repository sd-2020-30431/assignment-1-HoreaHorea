from tkinter import *

from Interface.klebi import klebi


class GUI:

    root = Tk()

    fi = klebi(root, 0, [['Name', 's'], ['Quantity(g)', 'n'], ['Calories(per 100g)', 'n'], ['Buy Date', 'd'],
                        ['Expiration Date', 'd']], "Food item")
    dp = klebi(root, 7, [['Name', 's'], ['Address', 's'], ['Contact', 's']], "Donation place")
    ei = klebi(root, 11, [['Name', 's'], ['Quantity', 'n']], "Eaten item")
    di = klebi(root, 14, [['Place', 's'],['Name', 's'], ['Quantity', 'n']], "Donated item")
    # KLEB for goals
    # KLEB for other stuff

    #prevday = Button(root,)


    # fidb()
    # dpdb()
    # fidb()

    root.mainloop()
