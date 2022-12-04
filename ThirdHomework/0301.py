import os

import matplotlib.pyplot as plt
import pandas as pd

"""
    0301:绘制金砖五国的GDP和CO2排放量的折线图
"""

UNIT = 1e6  # 定义标准单位


def preProcessing(*args):
    """
    此函数用于将数据以百万为单位进行显示, 使用多参数函数可以降低程序的耦合性,提高复用性
    """

    # 应该实现去除列表之中所有的非数字元素,之后按最短的那个列表将所有的列表长度统一
    li = []
    for arg in args:
        for i in range(len(arg)):
            if arg[i] == '..':
                arg[i] = 0
        arg = [float(x) / UNIT for x in arg if x != '..'][:55]
        # arg.replace('..',0)
        li.append(arg)
    return li

def uniLength(*args):
    li = []
    for arg in args:
        arg = arg[:55]
        li.append(arg)
    return li

# def func(li):


os.chdir(r'D:\Python\PythonElectives')
data = pd.read_excel(r'HISCO2.xls')  # 必须组件:xlpd
data.columns = list(data.iloc[2])  # 将第三行作为列名
data.drop(index=[0, 1, 2], inplace=True)  # 删除前三行
data.dropna(subset=['Country Code'], inplace=True, how='any')  # 填充NaN

GDP = pd.read_excel(r'HISGDP.xlsx')
GDP.dropna(subset=['Country Code'], inplace=True, how='any')

# 提取出非洲GDP前五的国家,不知道这几个国家对不对
AlgeriaGDP = GDP[GDP['Country Code'] == 'DZA'].values[0][4:]
AlgeriaCo2 = data[data['Country Code'] == 'DZA'].values[0][4:]
AngolaGDP = GDP[GDP['Country Code'] == 'AGO'].values[0][4:]
AngolaCo2 = data[data['Country Code'] == 'AGO'].values[0][4:]
EgyptGDP = GDP[GDP['Country Code'] == 'EGY'].values[0][4:]
EgyptCo2 = data[data['Country Code'] == 'EGY'].values[0][4:]
NigeriaGDP = GDP[GDP['Country Code'] == 'NGA'].values[0][4:]
NigeriaCo2 = data[data['Country Code'] == 'NGA'].values[0][4:]
SouthAfricaGDP = GDP[GDP['Country Code'] == 'ZAF'].values[0][4:]
SouthAfricaCo2 = data[data['Country Code'] == 'ZAF'].values[0][4:]


AlgeriaGDP,AngolaGDP,EgyptGDP,NigeriaGDP,SouthAfricaGDP =\
    preProcessing(
        AlgeriaGDP,AngolaGDP,EgyptGDP,NigeriaGDP,SouthAfricaGDP
)
AlgeriaCo2,AngolaCo2,EgyptCo2,NigeriaCo2,SouthAfricaCo2 =\
    uniLength(
        AlgeriaCo2,AngolaCo2,EgyptCo2,NigeriaCo2,SouthAfricaCo2
    )
length = len(AlgeriaGDP)

yearRange = range(1960, 1960 + length)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 新建一张图
plt.figure(figsize=(10,6), dpi=100, facecolor='w', edgecolor='k')
plt.grid(color='b', linestyle=':', linewidth='1', alpha=0.5)
plt.xlim(1960, 1960 + length)
plt.xlabel("年份")
# plt.ylim(0,1e8)
plt.ylabel("单位:百万美元")

# plt.ylabel("GDP/CO2排放量")
plt.title("非洲前五国家GDP和CO2排放量的折线图")
plt.plot(yearRange, AlgeriaGDP,'g-',label='阿尔及利亚GDP')
plt.plot(yearRange, AlgeriaCo2,'g:',label='阿尔及利亚CO2排放量')
plt.plot(yearRange, AngolaGDP,'r-',label='安哥拉GDP')
plt.plot(yearRange, AngolaCo2,'r:',label='安哥拉CO2排放量')
plt.plot(yearRange, EgyptGDP,'b-',label='埃及GDP')
plt.plot(yearRange, EgyptCo2,'b:',label='埃及CO2排放量')
plt.plot(yearRange, NigeriaGDP,'y-',label='尼日利亚GDP')
plt.plot(yearRange, NigeriaCo2,'y:',label='尼日利亚CO2排放量')
plt.plot(yearRange, SouthAfricaGDP,'c-',label='南非GDP')
plt.plot(yearRange, SouthAfricaCo2,'c:',label='南非CO2排放量')

plt.legend(loc='upper left')
plt.savefig("AfricaCountryGDP_CO2.jpg")
plt.show()
