# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 11:25:39 2017
用于构建字典表，对正则提取的高速公路的路段进行划分
@author: wang
"""

import xlrd
import xlwt 
import numpy as np
import csv
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

#读取原始的文件
path = 'C:/Users/wang/Desktop/factor_road.xls'#用于构建字典的道路信息情况。如：鹤大高速 G11
def read_road_info(path):
    WB = xlrd.open_workbook(path)
    sheet1 = WB.sheet_by_name('Sheet1')
    info = np.array([ [ unicode for j  in range(2)]  for i in range(0,sheet1.nrows)] )
    for row in range(0,sheet1.nrows):  # 生成一个字符库
          for col in range(2):
              info[row][col]=sheet1.cell(row,col).value
    return info  #返回excel的所有键-值
    
def make_cict(list2,list1):
    return  dict(zip(list2,list1)) #对两个列表构建字典，list2键,list1值
    
def write2excel(path):
    # 写入excel
    book = xlwt.Workbook(encoding = 'utf8',style_compression = 0)
    sheet = book.add_sheet('sheet1', cell_overwrite_ok = True)
    for i in range(len(list2)): 
        sheet.write(i, 1, list2[i])
    book.save(path)
def createDictCSV(fileName="ABC.csv", dataDict={}):
    with open(fileName, "wb") as csvFile:
        csvWriter = csv.writer(csvFile)
        for k,v in dataDict.iteritems():
            csvWriter.writerow([k,v])
        csvFile.close()
       
        
info = read_road_info(path) #读取基本的excel信息       
list1 = info[:, 0]
list2 = info[:, 1]   
dict1 = make_cict(list2,list1) #构造字典

#for key in dict1:
#    print key, dict1[key]  #打印字典的内容
    
#将列表写入excel
path1 = 'C:/Users/wang/Desktop/A.xls'
write2excel(path1) 
#保存字典
createDictCSV('ABC', dict1)
#dict2csv('ABC',dict1)

#模拟查询字典过程
a = ['鹤大高速', '沪蓉高速', '清伊高速']  #实例，为从新闻中获取的具体的高速路的代号
for item in a:
    for key in dict1:
        if item == key:
            print item, dict1[key]    #对新来的道路进行字符库查询，并将查询的结果显示

#http://blog.csdn.net/liuxincumt/article/details/8183391 参考这个博客







