"""
输入三角形的三个边，判断是否构成三角形。
如果能够构成三角形，则利用turtle绘制出填充红色的三角形，
并计算面积显示在其绘制的三角形下方（为显示美观，建议在输入边长较小时按比例扩大）。
不能构成三角形，则在turtle中文字提示。
"""

import turtle
from math import acos
from math import degrees


# 余弦定理,根据每个边的长度计算角度
def get_angle(a, b, c):
    A = degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
    B = degrees(acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
    C = degrees(acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
    return A, B, C


turtle.screensize(800, 800, 'white')
turtle.pencolor("black")
turtle.speed(1)
a = int(input("请输入第一条边长:"))
b = int(input("请输入第二条边长:"))
c = int(input("请输入第三条边长:"))

if a + b > c and a + c > b and b + c > a:
    A, B, C = get_angle(a, b, c)
    turtle.fd(a * 10)
    turtle.rt(180-C)
    turtle.fd(b * 10)
    turtle.rt(180-A)
    turtle.fd(c * 10)
    turtle.rt(180-B)
else:
    print('三角形不合法')

# 分别计算每个角的角度,利用余弦定理
