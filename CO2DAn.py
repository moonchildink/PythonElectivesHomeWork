#CO2 & GDP Data analysis Figure
#-*- coding: utf-8 -*-

import os

import matplotlib.pyplot as Plt
import pandas as Pd

#Read Source data
os.chdir(r"D:\Python\PythonElectives")

ExDataCo2 = Pd.read_excel(r"HISCo2.xls")
ExDataGDP = Pd.read_excel(r"HISGDP.xlsx")
#print(ExData)
ExDataCo2 = ExDataCo2.fillna(0)         # 使用0来填充NaN

lstCHNCO2 =list(ExDataCo2.iloc[41,:])   # 获取中国的CO2数据
lstUSACO2 = list(ExDataCo2.iloc[252,:])
lstEUCO2 = list(ExDataCo2.iloc[74,:])
lstJPNCO2 = list(ExDataCo2.iloc[120,:])

lstCHNGDP = list(ExDataGDP.iloc[74])     # 获取中国的GDP数据
lstCHNGDP = lstCHNGDP[4:]

lstUSAGDP = list(ExDataGDP.iloc[237])
lstUSAGDP = lstUSAGDP[4:]

lstEUGDP = list(ExDataGDP.iloc[8])
lstEUGDP = lstEUGDP[4:]

lstJPNGDP = list(ExDataGDP.iloc[129])
lstJPNGDP = lstJPNGDP[4:]

#lstUSAGDP = list(ExDataGDP)


lstCHNGDP.pop()
lstUSAGDP.pop()
lstEUGDP.pop()
lstJPNGDP.pop()     # pop()函数可以删除列表之中指定位置的元素,当idx缺省时,使用默认值-1,即删除最后一个元素


print(lstUSAGDP)

lstCHNCO2 = lstCHNCO2[4:]
lstUSACO2 = lstUSACO2[4:]
lstEUCO2 = lstEUCO2[4:]
lstJPNCO2 = lstJPNCO2[4:]   # 剔除前四个元素


while lstUSACO2[-1] == 0:
    lstUSACO2.pop()
    lstCHNCO2.pop()
    lstEUCO2.pop()
    lstJPNCO2.pop()         # 要求所有国家的数据不存再NaN


#lgBase = 10
for i in range(len(lstCHNGDP)):
    lstCHNGDP[i] /= 1e6#math.log(lstCHNGDP[i],lgBase)      # 除以1e6,将GDP数据转换为以百万美元为单位
    lstUSAGDP[i] /= 1e6 #math.log(lstUSAGDP[i],lgBase)
    lstEUGDP[i]  /= 1e6 #math.log(lstEUGDP[i],lgBase)
    lstJPNGDP[i] /= 1e6#math.log(lstJPNGDP[i],lgBase)

    #lstCHNCO2[i] = math.log(lstCHNCO2[i], lgBase)
    #lstUSACO2[i] = math.log(lstUSACO2[i], lgBase)
    #lstEUCO2[i] = math.log(lstEUCO2[i],lgBase)
    #lstJPNCO2[i] = math.log(lstJPNCO2[i],lgBase)


Num = len(lstUSACO2)      # 获取数据的长度
#print(Num)

Plt.figure(figsize=(14,10))
Plt.rcParams['font.family'] = 'SimHei'
Plt.rcParams['font.sans-serif'] = ['SimHei']

Plt.title('二氧化碳排放&GDP表')
FontXY = {'family': 'SimHei','weight': 'normal','size': 16,}

Plt.xlabel(u'年份',FontXY)
Plt.ylabel(u'CO2&GDP',FontXY)

Plt.tick_params(labelsize=20)
lstYear = list(range(1960,1960+Num))
#print(lstYear)
x = lstYear
yCHNCo2 = lstCHNCO2
yUSACo2 = lstUSACO2
yEUCo2 = lstEUCO2
yJPNCo2 = lstJPNCO2

yCHNGdp = lstCHNGDP
yUSAGdp = lstUSAGDP
yEUGdp = lstEUGDP
yJPNGdp = lstJPNGDP

Plt.plot(x, yCHNCo2,linewidth = 4,color = 'r', label="中国")
Plt.plot(x, yCHNGdp,linewidth = 4,color = 'r', linestyle='--', label="CHNGDP")

Plt.plot(x, yUSACo2,linewidth = 4,color = 'b', label="美国")
Plt.plot(x, yUSAGdp,linewidth = 4,color = 'b', linestyle='--',label="USAGDP")

Plt.plot(x, yEUCo2, linewidth = 4,color = 'darkblue',label="欧盟")
Plt.plot(x, yEUGdp, linewidth = 4,color = 'darkblue',linestyle='--',label="EUGDP")

Plt.plot(x, yJPNCo2, linewidth = 4,color = 'gold',label="日本")
Plt.plot(x, yJPNGdp, linewidth = 4,color = 'gold',linestyle='--', label="JPGDP")

Plt.legend(prop = FontXY)
Plt.savefig(r'Co2chn.jpg')
Plt.show()


