"""
爬取虎牙网
"""
#开发步骤：目标网站  获取数据  分析数据  解析数据  保存数据

import requests  #用来模拟浏览器发送网络请求  http=>https 2.0
from lxml import etree  #用来解析提取的数据主体做预处理
from urllib import request #用request里面的urlretrive()下载图片
import os
import time

url = "https://www.huya.com/g/4079"

# http get post 方式  获取网页内容
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
headers={
    "user-agent":user_agent
}
result = requests.get(url,headers=headers).text
# print(result)
#解析数据 Xpath 解析对象
data =  etree.HTML(result)
data_list=data.xpath('//img[@class="pic"]')
# print(data_list)

for i in data_list:
    img = i.xpath('./@data-original')[0]
    # print(img)
    img = img.split("?")[0]   #去掉网址“？”后面不需要的内容
    # print(img)
    name = i.xpath('./@alt')[0]

    folder = os.getcwd() + "/woman/"
    if not os.path.exists(folder):
        os.makedirs(folder)
    try:    #下载图片
        request.urlretrieve(img,folder + name + '.jpg')

    except Exception as e:
        pass

    print("<%s> 下载完毕" %name)
    #为了防止网站拉黑 封IP 控制下速度
    time.sleep(3)