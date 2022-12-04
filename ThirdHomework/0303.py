import re

"""
编写程序使用正则表达式验证输入身份证号或者手机号验证是否合法
"""

def checkId(id):
    """
    @param: id:身份证号
    @method:验证身份证号是否合法
    """
    if re.match(r'^\d{17}[\dX]{1}$', id):
        return True
    else:
        return False

def checkPhone(phone):
    """
    @param: phone:手机号
    @method:验证手机号是否合法
    """
    if re.match(r'^1[3456789]\d{9}$', phone):
        return True
    else:
        return False


if __name__ == '__main__':
    id = input('请输入身份证号:')
    phone = input('请输入手机号:')
    if checkId(id):
        print('身份证号合法')
    else:
        print('身份证号不合法')
    if checkPhone(phone):
        print('手机号合法')
    else:
        print('手机号不合法')

