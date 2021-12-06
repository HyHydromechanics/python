import tkinter as tk

windows = tk.Tk()
windows.title("输入框、文本框")
windows.geometry("500x300")  # 界面大小
# 设置输入框，对象是在windows上，show参数--->显示文本框输入时显示方式None:文字不加密，show="*"加密
e = tk.Entry(windows, show=None)
e.pack()


def insert_point():
    var = e.get()  # 获取输入的信息
    t.insert("insert", var)  # 参数1：插入方式，参数2：插入的数据


def insert_end():
    var = e.get()
    t.insert("end", var)


# 根据光标位置插入数据
b1 = tk.Button(windows, text="insert point", width=15, height=2, command=insert_point)
b1.pack()
b2 = tk.Button(windows, text="insert end", width=15, height=2, command=insert_end)
b2.pack()
# 设置文本框
t = tk.Text(windows, height=2)
t.pack()

windows.mainloop()
