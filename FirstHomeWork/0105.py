# 使用turtle库绘制一副图画

import random
from turtle import *

my_turtle = Turtle()
my_win = my_turtle.getscreen()


def tree(branch_len, t):
    if branch_len > 5:
        if branch_len <= 20:
            t.pencolor('green')  # 当树枝很小时,画笔绿色.模拟树叶
        else:
            t.pencolor('black')
        t.pensize(branch_len // 10)  # 随着递归的进行 树枝越来越细
        t.fd(branch_len)
        degree = random.randint(15, 30)  # 随机角度
        t.rt(degree)
        gap = random.uniform(10, 15)  # 随机减少的增量
        tree(branch_len - gap, t)
        t.lt(2 * degree)
        tree(branch_len - gap, t)
        t.rt(degree)
        t.backward(branch_len)


my_turtle.setheading(90)
my_turtle.speed(10)
my_turtle.up()
my_turtle.backward(300)
my_turtle.down()
tree(100, my_turtle)

my_win.exitonclick()