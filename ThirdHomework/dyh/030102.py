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


#世界主要国家的GDP数据
ChinaGDP = gdpData[gdpData['Country Code'] == 'CHN'].values[0][4:]
ChinaCo2 = data[data['Country Code'] == 'CHN'].values[0][4:]
AmericaGDP = gdpData[gdpData['Country Code'] == 'USA'].values[0][4:]
AmericaCo2 = data[data['Country Code'] == 'USA'].values[0][4:]
JapanGDP = gdpData[gdpData['Country Code'] == 'JPN'].values[0][4:]
JapanCo2 = data[data['Country Code'] == 'JPN'].values[0][4:]
GermanyGDP = gdpData[gdpData['Country Code'] == 'DEU'].values[0][4:]
GermanyCo2 = data[data['Country Code'] == 'DEU'].values[0][4:]
FranceGDP = gdpData[gdpData['Country Code'] == 'FRA'].values[0][4:]
FranceCo2 = data[data['Country Code'] == 'FRA'].values[0][4:]


ChinaGDP,AmericaGDP,JapanGDP,GermanyGDP,FranceGDP =\
    func1(
        ChinaGDP,AmericaGDP,JapanGDP,GermanyGDP,FranceGDP
)
ChinaCo2,AmericaCo2,JapanCo2,GermanyCo2,FranceCo2 =\
    func2(
        ChinaCo2,AmericaCo2,JapanCo2,GermanyCo2,FranceCo2
    )



length = len(ChinaGDP)

yearRange = range(1960, 1960 + length)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 新建一张图
plt.figure(figsize=(10, 8), dpi=120, facecolor='w')
plt.grid(color='b', linestyle=':', linewidth='1', alpha=0.5)
plt.xlim(1960, 1960 + length)
plt.xlabel("年份")

plt.ylabel("单位:百万美元")

plt.title("世界主要国家")

plt.plot(yearRange, ChinaGDP, 'g-', label='中国GDP')
plt.plot(yearRange, ChinaCo2, 'g:', label='中国CO2排放量')
plt.plot(yearRange, AmericaGDP, 'r-', label='美国GDP')
plt.plot(yearRange, AmericaCo2, 'r:', label='美国CO2排放量')
plt.plot(yearRange, JapanGDP, 'b-', label='日本GDP')
plt.plot(yearRange, JapanCo2, 'b:', label='日本CO2排放量')
plt.plot(yearRange, GermanyGDP, 'y-', label='德国GDP')
plt.plot(yearRange, GermanyCo2, 'y:', label='德国CO2排放量')
plt.plot(yearRange, FranceGDP, 'c-', label='法国GDP')
plt.plot(yearRange, FranceCo2, 'c:', label='法国CO2排放量')

plt.legend(loc='upper left')
plt.savefig("DYHMainCountry.jpg")
plt.show()

