from turtle import *



def square(x,y,size,color_name):    #定义一个话方块的函数，有四个参数
    up()
    goto(x,y)  #拿起画笔到指定坐标
    down()      #落下
    color(color_name)    #调用color函数接收参数
    begin_fill()         #开始画图

    forward(size)        #接收size forward会沿直线走size步
    left(90)              #left函数向左转90°
    forward(size)         #再直走size步 以此类推
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)

    end_fill()         #结束画图
