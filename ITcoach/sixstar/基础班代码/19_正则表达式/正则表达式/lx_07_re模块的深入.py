"""
演示re模块的深入
"""
"""
re.match() 默认匹配开头
re.search() 只要满足了条件一个就匹配
re.findall() 所有满足都匹配
re.sub() 可以替换满足条件的数据
"""
import re

# 提取出666666
# data = '这个视频的点击量:666666'
# demo = re.match(r'\d{6}',data)
# print(demo.group())


"""
search
"""
# data = '这个视频的点击量:666666'
# # demo = re.match(r'\d{6}',data)
# demo = re.search(r'\d{6}',data)
# print(demo)
# print(demo.group())


"""
findall  匹配成功之后 不会得到 一个对象  列表
"""
# data = '这个视频的点击量:666666,下载量:555555,转发量:444444'
#
# demo = re.findall(r'\d{6}',data)
# print(demo)
# for i in demo:
#     print(i,end=',')


"""
sub >>> 替换
"""


# s = '视频的点击量:1'
# #      要被替换的部分 , 要替换成什么,,  被匹配的字符串
# data = re.sub(r'\d+','2',s)
# print(data)

# 增加点击量
def add(obj):
    num1 = obj.group()  # 得到匹配成功的数据 123
    num2 = int(num1) + 1  # 123 + 1 =124
    return str(num2)   # 124


data = re.sub(r'\d+', add, '视频播放量是:334')
print(data)


"""
split  >>> 切割
"""
#
# s = 'hello,武汉加油,湖北加油>中国加油'  # 切割
# data = re.split(r',|>',s)  # 或  ,|>
# print(data)
# # for
#
