from tkinter import *
import tkinter as tk
import tkinter.messagebox
import os
import shutil

try:
    os.remove("C:\Users\Harry\AppData\Local\Temp" + "\" + os.listdir("C:\Users\Harry\AppData\Local\Temp"))
except:
    os.path.exists("C:\Users\Harry\AppData\Local\Temp")
    print("error")

top = tk.Tk()
top.geometry("400x300")
top.title("Harry的电脑清理器")


def clean_button():
    tk.messagebox.showinfo("提醒!", "清理完毕了, 大概")


def del_file(path_data):
    for i in os.listdir(path_data):
        file_data = path_data + "\\" + i
        if os.path.isfile(file_data) == True:
            os.remove(file_data)
        else:
            del_file(file_data)


path_data = r"C:\Users\Harry\Desktop\新建文件夹"
del_file(path_data)

clean = tk.Button(top, text="点我进行清理哒哟~(\￣︶￣*\)",
                  fg="blue", bg="white",
                  command=clean_button,
                  relief=FLAT,
                  width=30, height=10,
                  font=('微软雅黑', 16, 'bold')
                  )

clean.pack()

top.mainloop()
