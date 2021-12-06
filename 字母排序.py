import tkinter as tk
import tkinter.messagebox

windows = tk.Tk()
windows.title("The begining of the text")
windows.geometry("500x200")

input_space = tkinter.Entry(windows,
                            fg="black",
                            bg="white",
                            width=50,
                            font=('Arial', 12, 'bold'),
                            show="")
input_space.place(relx=0.3, rely=0.3,
                  anchor="center")
input_space.pack()

alphabet = "abcdefghigklmnopqrstuvwxyz"

def check():
    str_get = input_space.get()
    result = str_get.split(" ")
    tk.messagebox.showinfo("提醒!", "大概是好了吧?的样子")
    t.insert(result)


convert_button = tkinter.Button(windows, text="convert",
                                fg="black",
                                bg="white",
                                font=('微软雅黑', 12, 'bold'),
                                command=check)
convert_button.pack()

windows.mainloop()
