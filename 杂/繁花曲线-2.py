import turtle
import math
import random

class Spiro:
    def __init__(self, R, r, l, num, color):
        self.R = R
        self.r = r
        self.l = l
        self.num = num
        self.pen = turtle.Turtle()
        self.pen.pencolor(color)
        turtle.colormode(1.0)
        
    def drawSingleSpiro(self):
        # 周期数 p
        p = self.periods()

        for i in range(0, 360*p + 2, 2):
            if i != 0:
                self.pen.setpos(*self.cor_x_y_Spiro(i))
            else:
                self.pen.up()
                self.pen.setpos(*self.cor_x_y_Spiro(i))
                self.pen.down()

    def drawWhole(self):
        for s in range(self.num):
            if s != 0:
                self.randomSetting()
                self.drawSingleSpiro()
            else:
                self.drawSingleSpiro()

    def randomSetting(self):
        self.l = random.random()

        r = random.random()
        g = random.random()
        b = random.random()
        self.pen.pencolor((r, g, b))

    def hcf(self, x, y):
        if x == y:
            result = x
        elif x > y:
            result = self.hcf(x-y, y)
        else:
            result = self.hcf(x, y-x)
        return result

    def periods(self):
        div = self.hcf(self.R, self.r)
        return self.r//div
    
    def cor_x_y_Spiro(self, theta):
        k = self.r/self.R
        ef = 1 - k
        
        rad = self.degreeToRadian(theta)
        x = self.R*(ef*math.cos(rad) + self.l*k*math.cos(ef/k*rad))
        y = self.R*(ef*math.sin(rad) - self.l*k*math.sin(ef/k*rad))
    
        return (x, y)

    def degreeToRadian(self, degree):
        return degree * math.pi / 180

s = Spiro(100, 30, 0.6, 5, "pink")
s.drawWhole()
turtle.mainloop()
