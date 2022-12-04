
def method1(n:int)->int:
    sum = 0
    for i in range(n+1):
        sum+=i
    return sum

def method2(n:int)->int:
    li = [i for i in range(n+1)]
    return sum(li)

n = int(input('input a number'))
print('method1:',method1(n),'method2:',method2(n))