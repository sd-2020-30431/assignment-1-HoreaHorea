import random

foods = ["Chocolate", "Apples", "Milk", "Bread", "More Chocolate", "Even More Chocolate", "Bacon", "Honey"]
values = [100, 1000, 300, 350, 800, 150, 250, 333, 500]
dates = ["2020-04-11", "2020-04-12", "2020-04-13", "2020-04-14", "2020-04-15", "2020-04-16", "2020-04-17", "2020-04-18"]


def entryStringDefault(event):
    event.widget.delete(0, "end")
    event.widget.insert(0, random.choice(foods))


def entryNumberDefault(event):
    event.widget.delete(0, "end")
    event.widget.insert(0, random.choice(values))


def entryDateDefault(event):
    event.widget.delete(0, "end")
    event.widget.insert(0, random.choice(dates))
