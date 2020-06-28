"""
功能：获取按键精灵视频教程
版本：1.0
"""
import requests
import re
import xlwt

url = "http://bbs.anjian.com/showtopic-565244-1.aspx"

respose = requests.get(url)
html = respose.text

re_qu = '<a href="(.*?)" target="_blank">(.*?)</a>'

url_names = re.findall(re_qu,html)
# print(url_names[3:-45])

# 创建工作薄
workbook = xlwt.Workbook()
# 添加工作表，并命名为“按键精灵视频教程”
worksheet = workbook.add_sheet('按键精灵视频教程')
r = 0
for url , name in url_names[3:-45]:
    # print(url)
    # print(name)
    # 在表内写入数据
    worksheet.write(r,0,name)   #写入标题名
    worksheet.write(r,1,url)    #写入视频地址
    r=r+1

workbook.save("按键精灵视频教程.xls")