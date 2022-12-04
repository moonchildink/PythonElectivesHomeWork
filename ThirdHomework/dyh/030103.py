import os
import matplotlib.pyplot as plt
import pandas as pd

"""
    030102:绘制世界主要国家的GDP和CO2排放量的折线图
"""


def func1(*args):
    li = []
    for arg in args:
        for i in range(len(arg)):
            if arg[i] == '..':
                arg[i] = 0
        arg = [float(x) / 1e6 for x in arg if x != '..'][:55]
        li.append(arg)
    return li

def func2(*args):
    li = []
    for arg in args:
        arg = arg[:55]
        li.append(arg)
    return li


os.chdir(r'D:\Python\PythonElectives')
data = pd.read_excel(r'HISCO2.xls')  # 必须组件:xlpd
data.columns = list(data.iloc[2])  # 将第三行作为列名
data.drop(index=[0, 1, 2], inplace=True)  # 删除前三行
data.dropna(subset=['Country Code'], inplace=True, how='any')  # 填充NaN

gdpData = pd.read_excel(r'HISGDP.xlsx')
gdpData.dropna(subset=['Country Code'], inplace=True, how='any')




# 非洲国家的数据
EgyptGDP = gdpData[gdpData['Country Code'] == 'EGY'].values[0][4:]
EgyptCo2 = data[data['Country Code'] == 'EGY'].values[0][4:]
AlgeriaGDP = gdpData[gdpData['Country Code'] == 'DZA'].values[0][4:]
AlgeriaCo2 = data[data['Country Code'] == 'DZA'].values[0][4:]
MorocooGDP = gdpData[gdpData['Country Code'] == 'MAR'].values[0][4:]
MorocooCo2 = data[data['Country Code'] == 'MAR'].values[0][4:]
KenyaGDP = gdpData[gdpData['Country Code'] == 'KEN'].values[0][4:]
KenyaCo2 = data[data['Country Code'] == 'KEN'].values[0][4:]
SouthAfricaGDP = gdpData[gdpData['Country Code'] == 'ZAF'].values[0][4:]
SouthAfricaCo2 = data[data['Country Code'] == 'ZAF'].values[0][4:]


EgyptGDP,AlgeriaGDP,MorocooGDP,KenyaGDP,SouthAfricaGDP =\
    func1(
        EgyptGDP,AlgeriaGDP,MorocooGDP,KenyaGDP,SouthAfricaGDP
)
EgyptCo2,AlgeriaCo2,MorocooCo2,KenyaCo2,SouthAfricaCo2 =\
    func2(
        EgyptCo2,AlgeriaCo2,MorocooCo2,KenyaCo2,SouthAfricaCo2
    )



length = len(EgyptGDP)


yearRange = range(1960, 1960 + length)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 新建一张图
plt.figure(figsize=(10, 8), dpi=120, facecolor='w')
plt.grid(color='b', linestyle=':', linewidth='1', alpha=0.5)
plt.xlim(1960, 1960 + length)
plt.xlabel("年份")

plt.ylabel("单位:百万美元")

plt.title("非洲国家")

plt.plot(yearRange, EgyptGDP, 'g-', label='埃及GDP')
plt.plot(yearRange, EgyptCo2, 'g:', label='埃及CO2排放量')
plt.plot(yearRange, AlgeriaGDP, 'r-', label='阿尔及利亚GDP')
plt.plot(yearRange, AlgeriaCo2, 'r:', label='阿尔及利亚CO2排放量')
plt.plot(yearRange, MorocooGDP, 'b-', label='摩洛哥GDP')
plt.plot(yearRange, MorocooCo2, 'b:', label='摩洛哥CO2排放量')
plt.plot(yearRange, KenyaGDP, 'y-', label='肯尼亚GDP')
plt.plot(yearRange, KenyaCo2, 'y:', label='肯尼亚CO2排放量')
plt.plot(yearRange, SouthAfricaGDP, 'c-', label='南非GDP')
plt.plot(yearRange, SouthAfricaCo2, 'c:', label='南非CO2排放量')


plt.legend(loc='upper left')
plt.savefig("DYHAfricaCountry.jpg")
plt.show()

