from math import sqrt
def function():
    for i in range(100,200):
        count = 0
        for j in range(2,int(sqrt(i))):
            if i%j==0:
                count+=1
        if count == 0:
            print(i)

function()