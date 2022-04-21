import tkinter as tk
from tkinter import *


nameList = [0, 0, 0]
valueList = [0, 0, 0]

nl = iter(nameList)
vl = iter(valueList)

rows = 3
columns = 3

windows = tk.Tk()
windows.title("Game")

cell1 = tk.Text(windows, width=10, height=5)
cell1.grid()
c1 = cell1.getint()

cell2 = tk.Text(windows, width=10, height=5)
cell2.grid()
c2 = cell2.getint()

cell3 = tk.Text(windows, width=10, height=5)
cell3.grid()
c3 = cell3.getint()

cell4 = tk.Text(windows, width=10, height=5)
cell4.grid()
c4 = cell4.getint()

cell5 = tk.Text(windows, width=10, height=5)
cell5.grid()
c5 = cell5.getint()

cell6 = tk.Text(windows, width=10, height=5)
cell6.grid()
c6 = cell6.getint()

cell7 = tk.Text(windows, width=10, height=5)
cell7.grid()
c7 = cell7.getint()

cell8 = tk.Text(windows, width=10, height=5)
cell8.grid()
c8 = cell8.getint()

cell9 = tk.Text(windows, width=10, height=5)
cell9.grid()
c9 = cell9.getint()

if c1 + c5 + c9 == 3:
    tk.messagebox.showinfo("Player 1 Won!")
elif c1 + c5 + c9 == 6:
    tk.messagebox.showinfo("Player 2 Won!")

if c3 + c5 + c7 == 3:
    tk.messagebox.showinfo("Player 1 Won!")
elif c1 + c2 + c3 == 6:
    tk.messagebox.showinfo("Player 2 Won!")

windows.mainloop()
