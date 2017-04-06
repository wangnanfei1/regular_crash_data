# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 09:30:41 2017

@author: wang
"""
import sys
import numpy as np

import re
str = 'a123b'
str1 = 'a123b456b'
#print re.findall('a(.+?)b', str)
#print re.findall('a(.+)b', str1)
#
#PATTERN =  ur'([\u4e00-\u9fa5]{2,5}?(?:省|自治区|市))([\u4e00-\u9fa5]{2,7}?(?:市|区|县|州)){0,1}([\u4e00-\u9fa5]{2,7}?(?:市|区|县)){0,1}'  
#data_list = ['北京市', '陕西省西安市雁塔区', '西班牙', '北京市海淀区', '黑龙江省佳木斯市汤原县', '内蒙古自治区赤峰市',  
#'贵州省黔南州贵定县', '新疆维吾尔自治区伊犁州奎屯市']
#
#for data in data_list:  
#    data_utf8 = data.decode('utf8')  
#    print data_utf8  
#    country = data  
#    province = ''  
#    city = ''  
#    district = ''  
#    #pattern = re.compile(PATTERN3)  
#    pattern = re.compile(PATTERN)  
#    m = pattern.search(data_utf8)  
#    if not m:  
#        print country + '|||'  
#        continue  
#    #print m.group()  
#    country = '中国'  
#    if m.lastindex >= 1:  
#        province = m.group(1)  
#    if m.lastindex >= 2:  
#        city = m.group(2)  
#    if m.lastindex >= 3:  
#        district = m.group(3)  
#    out = '%s|%s|%s|%s' %(country, province, city, district)  
#    print out 
#m = re.match(r'hello ', 'hello World!')
#print m.group()




#reg = re.compile('^(?P<remote_ip>[^ ]*) (?P<date>[^ ]*) "(?P<request>[^"]*)" (?P<status>[^ ]*) (?P<size>[^ ]*) "(?P<referrer>[^"]*)" "(?P<user_agent>[^"]*)"')


#import xlrd
#WB = xlrd.open_workbook('C:/Users/wang/Desktop/factor_road.xls')
##filecontent = pd.read_excel('C:/Users/wang/Desktop/factor_road.xls')
#sheet=WB.sheet_by_name('Sheet1')
#StationInfor=np.array([ [ unicode for j  in range(sheet.ncols)]  for i in range(1,sheet.nrows)])
#print 'total rows:',  sheet.nrows
#print 'total cols:', sheet.ncols
#for row in range(1,sheet.nrows):
#      for col in range(sheet.ncols):
#             StationInfor[row-1][col]=sheet.cell(row,col).value
# 
#print StationInfor[0][0]

import xlrd
import xlwt 
book = xlwt.Workbook(encoding = 'utf8',style_compression = 0)
sheet = book.add_sheet('1', cell_overwrite_ok = True)
WB = xlrd.open_workbook('C:/Users/wang/Desktop/test_1.xls')
#filecontent = pd.read_excel('C:/Users/wang/Desktop/factor_road.xls')
sheet1 = WB.sheet_by_name('Sheet1')
info = np.array([ [ unicode for j  in range(sheet1.ncols)]  for i in range(0,sheet1.nrows)])
print 'total rows:',  sheet1.nrows  #显示整个列表的行数
print 'total cols:', sheet1.ncols   #显示之后整个列表的列数
for row in range(0,sheet1.nrows):  # 生成一个字符库
      for col in range(sheet1.ncols):
          info[row][col]=sheet1.cell(row,col).value

#print info[6][4]

PATTERN1 =  ur'([\u4e00-\u9fa5]{1,2}?(?:高速|公路|大桥))'
PATTERN2 = ur'((\d){1,4}([\u4e00-\u9fa5]{1,3}?(?:段|隧道|处|道路|方向))|([\u4e00-\u9fa5]{1,3}?(?:段|隧道|处|道路|方向)))'
PATTERN3 = ur'([\u4e00-\u9fa5]{1,3}?(?:追尾|相撞|侧翻|超速|起火|拥堵))'
PATTERN4 = ur'((\d){1,2}([\u4e00-\u9fa5]{0,1}?(?:身亡|人死|人死亡|伤亡))|([\u4e00-\u9fa5]{0,1}?(?:人死|人死亡))|[\u4e00-\u9fa5]受伤的((\d){1,2}人))'
PATTERN5 = ur'((\d){1,2}([\u4e00-\u9fa5]{0,1}?(?:人轻伤|人受伤|伤|人重伤|人受伤))|([\u4e00-\u9fa5]{0,1}?(?:伤|人重伤|人受伤)))'
#pattern = {PATTERN1, PATTERN2,PATTERN3 ，PATTERN4}
#pattern2 = re.compile(PATTERN2)

for row in range(0,sheet1.nrows):
    pattern1 = re.compile(PATTERN1)
    m1 = re.search(pattern1, info[row][4])
    pattern2 = re.compile(PATTERN2)
    m2 = re.search(pattern2, info[row][4])
    pattern3 = re.compile(PATTERN3)
    m3 = re.search(PATTERN3,info[row][4]) 
    pattern4 = re.compile(PATTERN4)
    m4 = re.search(PATTERN4,info[row][4])    
    pattern5 = re.compile(PATTERN5)
    m5 = re.search(PATTERN5,info[row][4])       
#    for item in pattern:
#        pattern = re.compile(item)
#        m = re.search(pattern, info[row][4])
    if m1:
        print m1.group(0)
        sheet.write(row, 5, m1.group(0))
#        book.save('C:/Users/wang/Desktop/AAA.xls')
    else:
        print 'no match'
    if m2:
        print m2.group(0)
        sheet.write(row, 6, m2.group(0))
#        book.save('C:/Users/wang/Desktop/AAA.xls')
    else:
        print 'no match'
    if m3:
        print m3.group(0)
        sheet.write(row, 7, m3.group(0))
#        book.save('C:/Users/wang/Desktop/AAA.xls')
    else:
        print 'no match'
    if m4:
        print m4.group(0)
        sheet.write(row, 8, m4.group(0))
#        book.save('C:/Users/wang/Desktop/AAA.xls')
    if m5:
        print m5.group(0)
        sheet.write(row, 9, m5.group(0))
#        book.save('C:/Users/wang/Desktop/AAA.xls')
book.save('C:/Users/wang/Desktop/AAA.xls')
    
    
    
#pattern1 = re.compile(PATTERN1)
#m1 = re.search(pattern1, info[6][4])
#pattern2 = re.compile(PATTERN2)
#m2 = re.search(pattern2, info[6][4])
#pattern3 = re.compile(PATTERN3)
#m3 = re.search(PATTERN3,info[6][4])
#
#
#
##m2 = re.search(pattern2, info[2][4])
#print m1.group(1), m2.group(0),m3.group(0)
#print m2.group()






