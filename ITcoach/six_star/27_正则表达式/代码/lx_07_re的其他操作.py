"""
演示re的其他操作
"""

import re
#re.match() 默认自带^

# "这个视频的点击量:123456" 匹配一个数据
# demo_data = "这个视频的点击量:123456"
# print(re.search(r"\d+",demo_data).group())

# "点击量:123456 下载量:666 转发量:888"
# demo_data = "这个视频的点击量:123456 下载量:666 转发量:888"
# print(re.findall(r"\d+",demo_data))

# url www.12321sad.com




# sub sub  替换

# demo_data ="视频点击量:123" # >>>视频点击量:124
# print(re.sub(r"\d+","124",demo_data))

# def add(obj):
#     # print(obj)
#     num1 = obj.group()
#     num2 = int(num1) + 1
#     return str(num2)
#
# demo1 = re.sub(r"\d+",add,"视频点击量为:665")
#
# demo2 = re.sub(r"\d+",add,"视频下载量为:887")
#
# print(demo1)
# print(demo2)



# split
demo_data = "hello,>武汉加油,湖北加油>中国加油"
print(re.split(r",|>",demo_data))













































