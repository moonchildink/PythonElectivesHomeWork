import os
import matplotlib.pyplot as plt
import pandas as pd

"""
    030101:绘制金砖五国的GDP和CO2排放量的折线图
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


# os.chdir(r'D:\Python\PythonElectives')
data = pd.read_excel(r'HISCO2.xls')  # 必须组件:xlpd
data.columns = list(data.iloc[2])  # 将第三行作为列名
data.drop(index=[0, 1, 2], inplace=True)  # 删除前三行
data.dropna(subset=['Country Code'], inplace=True, how='any')  # 填充NaN

gdpData = pd.read_excel(r'HISGDP.xlsx')
gdpData.dropna(subset=['Country Code'], inplace=True, how='any')

ChinaGDP = gdpData[gdpData['Country Code'] == 'CHN'].values[0][4:]
ChinaCo2 = data[data['Country Code'] == 'CHN'].values[0][4:]
IndiaGDP = gdpData[gdpData['Country Code'] == 'IND'].values[0][4:]
IndiaCo2 = data[data['Country Code'] == 'IND'].values[0][4:]
BrazilGDP = gdpData[gdpData['Country Code'] == 'BRA'].values[0][4:]
BrazilCo2 = data[data['Country Code'] == 'BRA'].values[0][4:]
RussiaGDP = gdpData[gdpData['Country Code'] == 'RUS'].values[0][4:]
RussiaCo2 = data[data['Country Code'] == 'RUS'].values[0][4:]
SouthAfricaGDP = gdpData[gdpData['Country Code'] == 'ZAF'].values[0][4:]
SouthAfricaCo2 = data[data['Country Code'] == 'ZAF'].values[0][4:]

ChinaGDP,IndiaGDP,BrazilGDP,RussiaGDP,SouthAfricaGDP =\
    func1(
        ChinaGDP,IndiaGDP,BrazilGDP,RussiaGDP,SouthAfricaGDP
)
ChinaCo2,IndiaCo2,BrazilCo2,RussiaCo2,SouthAfricaCo2 =\
    func2(
        ChinaCo2,IndiaCo2,BrazilCo2,RussiaCo2,SouthAfricaCo2
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

plt.title("金砖国家")
plt.plot(yearRange, ChinaGDP, 'g-', label='中国GDP')
plt.plot(yearRange, ChinaCo2, 'g:', label='中国CO2排放量')
plt.plot(yearRange, IndiaGDP, 'r-', label='印度GDP')
plt.plot(yearRange, IndiaCo2, 'r:', label='印度CO2排放量')
plt.plot(yearRange, BrazilGDP, 'b-', label='巴西GDP')
plt.plot(yearRange, BrazilCo2, 'b:', label='巴西CO2排放量')
plt.plot(yearRange, RussiaGDP, 'y-', label='俄罗斯GDP')
plt.plot(yearRange, RussiaCo2, 'y:', label='俄罗斯CO2排放量')
plt.plot(yearRange, SouthAfricaGDP, 'c-', label='南非GDP')
plt.plot(yearRange, SouthAfricaCo2, 'c:', label='南非CO2排放量')

plt.legend(loc='upper left')
plt.savefig("DYHBrics.jpg")
plt.show()
