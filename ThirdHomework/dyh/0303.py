import re

"""
编写程序使用正则表达式验证输入身份证号或者手机号验证是否合法
"""
id = input("请输入身份证号：")
if re.match(r'^\d{17}[\dX]{1}$', id):
    print("身份证号合法")
else:
    print("身份证号不合法")


phone = input("请输入手机号：")
if re.match(r'^1[3456789]\d{9}$', phone):
    print("手机号合法")
else:
    print("手机号不合法")


