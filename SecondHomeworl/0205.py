from random import randint


def func(num):
    return num,num**2,num**3


# li = [randint(0,200) for _ in range(10)]
li = []
for _ in range(10):
    li.append(randint(0,200))

for i in li:
    print(func(i))