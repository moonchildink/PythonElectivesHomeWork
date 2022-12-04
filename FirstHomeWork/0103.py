# 编程验证6到200之间的数字满足哥德巴赫猜想:任意一个偶数可以表示为两个质数的和
from math import sqrt


def getPrime():
    li = []
    for i in range(2, 200):
        count = 0
        for j in range(2, int(sqrt(i))):
            if i % j == 0:
                count = count+1
        if count == 0:
            li.append(i)
    return li


def function():
    # 首先计算出在200以下的质数数列
    primeList = getPrime()
    print(primeList)
    for i in range(6, 201, 2):
        count = 0
        for j in range(len(primeList) // 2):
            if i - primeList[j] in primeList:
                count += 1
        if count == 0:
            print("the number", i, "doesn't satisfy the Goldbach Conjecture")
    print('numbers in range of 6 to 200 are satisfy Goldbach Conjecture')


function()
