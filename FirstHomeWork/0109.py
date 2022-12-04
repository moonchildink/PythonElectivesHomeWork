"""
9.	使用随机函数，生成包含100000个0-1000之间的随机整数，并使用两种不同的方法统计出每个整数对象出现的次数，分别输出出现频率最高和最低的前10个数。
"""

import random

li = [random.randint(0,1000) for i in range(100000)]
count = dict()
for elem in li:
    count[elem] = count.get(elem, 0) + 1
# sorted(count.items(), key=lambda item: item[1])

counter = 0
print("最大的十个元素:\n")
while counter<10:
    print(max(count,key=count.get),count[max(count,key=count.get)])
    counter += 1
    del count[max(count,key=count.get)]

counter = 0
print("最小的十个元素:\n")
while counter < 10:
    counter += 1
    print(min(count, key=count.get),count[min(count, key=count.get)])
    del count[min(count, key=count.get)]

