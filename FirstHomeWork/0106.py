"""
6.	通过input( )函数随意输入一个整数，使用//和%两种运算生成一个逆序排列的整数忽略前导0，用print()函数输出。例如输入123456，输出654321
"""

num = int(input("input a integer").strip('0'))
reverseNum = 0
while num!=0:
    reverseNum = (num % 10)+reverseNum*10
    num = num//10
print(reverseNum)
