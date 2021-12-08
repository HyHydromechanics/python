from turtle import *
from gamebase import *      #将写好的函数导入文件中
from random import randrange
from time import sleep

snake = [[0,0],[10,0],[20,0],[30,0],[40,0],[50,0]]    #定义蛇为一个
apple_x = randrange(-20, 20)*10                       #苹果有两个坐标apple_x，apple_y，调用随机函数再范围(-20, 20)*10（）要为10的倍数产生随机数
apple_y = randrange(-20, 20)*10
aim_x = 10                                       #定义开始的步长为向左移动10单位，y轴保持不变
aim_y = 0

def change(x,y):   #定义chang函数，wasd操作会调用change
    global aim_x,aim_y
    aim_x=x
    aim_y=y

def inside_snake():    #判断蛇是否咬到自己
    for n in range(len(snake)-1):      #循环遍历蛇本身，当蛇头横纵坐标全部等于身体上的任意一截坐标，返回真
        if snake[-1][0] == snake[n][0] and snake[-1][1] == snake[n][1]:
            return True
    return False


def inside():      #判断蛇是否撞墙
    if  -210<= snake[-1][0] <= 200 and -210 <= snake[-1][1] <= 200:    #判断蛇头x，y，坐标在不在画布内
        return True
    else:
        return False

def gameloop():      #循环函数，主函数，没有跳出会一直执行
    global apple_x,apple_y,aim_x,aim_y,snake     #将全球变量引用过来
    snake.append([snake[-1][0]+aim_x, snake[-1][1]+aim_y])   #蛇的头（列表的尾）添加一个数据

    if apple_x != snake[-1][0] or apple_y != snake[-1][1]:    #判断是否吃到苹果，吃到则不用丢弃数据，没吃到则丢弃列表头部（蛇尾）数据
        snake.pop(0)
    else :
        apple_x = randrange(-20,20)*10                       #吃到了生成新的苹果
        apple_y = randrange(-20,20)*10

    if (not inside()) or inside_snake():                 #重开任意一个条件满足，撞墙或者咬自己
        square(snake[-1][0],snake[-1][1],10,"red")       #蛇头变红
        update()                                         #更新画布
        sleep(2)                                          #停止两秒钟后
        snake = [[0, 0], [10, 0], [20, 0], [30, 0], [40, 0], [50, 0]]     #生成新的蛇
        apple_x = randrange(-20, 20) * 10                                 #新的苹果
        apple_y = randrange(-20, 20) * 10
        aim_x = 10
        aim_y = 0


    clear()

    square(apple_x, apple_y, 10, "red")
    for n in range(len(snake)):      #调用square函数将列表变为绿色蛇图形
        square(snake[n][0],snake[n][1],10,"green")

    ontimer(gameloop,100)
    update()#更新，要不然画面不动
Screen().setup(420,420,0,0)#建立画布
hideturtle() #隐藏画图的头
tracer(False) #隐藏画图过程
listen()   #监听输入
onkey(lambda: change(0,10),"w")  #监听键盘，w,调用change函数，传值0，10 将移动的初始值改变，蛇头获得值后就会在对应的地方append出来
onkey(lambda: change(0,-10),"s")
onkey(lambda: change(-10,0),"a")
onkey(lambda: change(10,0),"d")
gameloop()#循环主函数
done()
