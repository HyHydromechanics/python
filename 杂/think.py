from tkinter  import *
root= Tk() 
def lab():
    label0=Label(root,text="功能暂时未添加")
    label0.grid(column=0)
root.geometry("800x480")#窗口大小
 
 
menu0=Menu(root)#参数是父级控件
for x in ['文件','编辑','视图']:
    menu0.add_command(label=x,command=lab)#添加3个一级菜单
#二级菜单
cascade0=Menu(menu0,tearoff=False)#tearoff=False 表示这个菜单不可以被拖出来
for x in ['添加新项','添加现有项']:
    cascade0.add_command(label=x,command=lab)
cascade0.add_separator()#分割线
cascade0.add_checkbutton(label="在不调试的情况下启动")#单选框
cascade0.add_separator()#分割线
cascade0.add_radiobutton(label="添加引用")#多选框
cascade0.add_radiobutton(label="添加服务")#多选框
menu0.add_cascade(label='项目',menu=cascade0)#在menu0中添加一个label为项目的级联菜单
 
root['menu']=menu0#窗口root的menu是menu0
 
root.mainloop()  
