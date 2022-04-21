import tkinter
from tkintertable import TableCanvas, TableModel
from tkinter import *

master = tkinter.Tk()
master.geometry('400x500')

tframe = Frame(master)
tframe.pack()

data = {'rec1': {'col1': 99.88, 'col2': 108.79, 'label': 'rec1'},
       'rec2': {'col1': 99.88, 'col2': 108.79, 'label': 'rec2'}
       } 

table = TableCanvas(tframe, data=data)
table.show()

master.mainloop()