# -*- coding: utf-8 -*-
''' 
PM2.5 Analysis
'''
import requests 
from bs4 import BeautifulSoup
import re
import io
import sys
import matplotlib.pyplot as plt
import pandas as pd
import xlwt
from pyecharts.charts import Bar
from pyecharts import options as opts
import webbrowser as Web
import numpy as np


def GetDataFromWeb(subcity):
    '''
    Get data from web,return parameters list
    ''' 
    baseWeb = r'http://www.86pm25.com/city/'
    cityHtml = requests.get(baseWeb + subcity + '.html',timeout=30)
    if cityHtml.status_code != 200:
        return lstData
    cityHtml.encoding = 'utf-8'
    cityStr = cityHtml.text
    bs = BeautifulSoup(cityStr, 'html.parser')

    strData = bs.select('tr>td')
    #print(strData)
    lstData = [strData[0].string,strData[1].string, strData[3].string.strip('μg/m³'),strData[4].string.strip('μg/m³')]
    print(lstData)
    return lstData
#End of GetDataFromWeb

def main():
  
    #sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
    
    cityNames = ['北京','上海','广州','深圳','拉萨','西宁','昆明','武汉','长春','唐山','成都','乌鲁木齐','合肥','宣城']
    cityHtml = ['beijing','shanghai','guangzhou','shenzhen','lasa','xining','kunming','wuhan','changchun','tangshan','chengdu','wulumuqi','hefei','xuancheng']
    lstStationName = [] #First station name list
    lstAQI = []
    lstPm25 = []
    lstPm10 = []
   
    for city in cityHtml:
        lstData = GetDataFromWeb(city)
        if len(lstData) == 0:
            lstStationName.append("失联")
            lstAQI.append(0.0)
            lstPm25.append(0.0)
            lstPm10.append(0.0)
        else:
            lstStationName.append((lstData[0]))
            strTmp = str(lstData[1])
            if strTmp.isdigit():
                lstAQI.append(float(strTmp))
            else:
                lstAQI.append(0.0)
            #End of if
            strTmp = str(lstData[2])
            if strTmp.isdigit():
                lstPm25.append(float(strTmp))
            else:
                lstPm25.append(0.0)
            
            strTmp = str(lstData[3])
            if strTmp.isdigit():
                lstPm10.append(float(strTmp))
            else:
                lstPm10.append(0.0)
            #End of if
        #End of if
    #End of for
    print(lstStationName)
    print(lstAQI)
    print(lstPm25)
    print(lstPm10)

    OutEx = xlwt.Workbook()
    Table = OutEx.add_sheet(u"环境质量表")
    Table.write(0,0,u"城市")
    Table.write(0,1,u"测试站点")
    Table.write(0,2,u"AQI")
    Table.write(0,3,u"PM2.5")
    Table.write(0,4,u"PM10")
    for i in range(len(cityNames)):
        Table.write(i + 1, 0, cityNames[i])
        Table.write(i + 1, 1, lstStationName[i])
        Table.write(i + 1, 2, lstAQI[i])
        Table.write(i + 1, 3, lstPm25[i])
        Table.write(i + 1, 4, lstPm10[i])
    #End of for
    OutEx.save(r"D:\Pm25.xls")

    plt.figure(figsize=(10,8))
    plt.rcParams['font.family'] = 'SimHei'
    plt.rcParams['font.sans-serif'] = ['SimHei']
    #解决坐标轴符号'-'显示为方块
    plt.rcParams['axes.unicode_minus'] = False
    
    barWidth = 0.45
    LenofBar = len(cityNames)
    barPM25 = [i+barWidth/2 for i in range(LenofBar)]
    
    plt.bar(np.array(range(len(cityNames))) - barWidth/2,lstAQI,width=barWidth,color = 'r', label = 'AQI', alpha = 0.5)
    #plt.bar(range(len(cityNames)),lstPm25,width=barWidth,color = 'b', label = 'PM2.5', alpha = 0.4)
    plt.bar(barPM25,lstPm25,width=barWidth,color = 'b', label = 'PM2.5', alpha = 0.5)

    plt.xticks(list(range(len(cityNames))),['北京','上海','广州','深圳','拉萨','西宁','昆明','武汉','长春','唐山','成都','乌鲁木齐','合肥','宣城'])
    plt.title('典型城市空气质量指标',fontsize = 18)
    plt.xlabel('城市',fontsize=16)
    plt.ylabel('AQI&PM2.5指标',fontsize = 16)
    plt.legend()
    for a,b in zip(list(range(len(cityNames))),lstAQI):
        plt.text(a-0.3,b+0.2,'%.1f'%b)
    for a,b in zip(barPM25,lstPm25):
        plt.text(a-0.15,b+0.2,'%.0f'%b)
         
    plt.show()

    bar = Bar()
    bar.add_xaxis(cityNames)
    bar.set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=10,interval=0)))
    bar.add_yaxis("PM2.5值",lstPm25)

    bar.set_global_opts(title_opts=opts.TitleOpts(title="典型城市PM2.5值"))
    bar.set_colors('blue')
    bar.render("Pm25.html")

    IEPath = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    Web.register('Web', None, Web.BackgroundBrowser(IEPath))
    Web.get('Web').open(r"Pm25.html", new=1,autoraise=True)

#End of main

if __name__ == '__main__':
    main()
