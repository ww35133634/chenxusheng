"""
演示贪婪与非贪婪
"""

"""
正则表达式取数据的时候总是贪婪的
"""
# import re
# # <asdas>  <asdas>
# s = '<a>123<a>456'
#
# data = re.match(r'<.*>\d{3}',s)
# print(data.group())

"""
<a>123<a>456  正则表达式 贪婪的

"""

import re
# <asdas>  <asdas>
s = '<a>123<a>456'
#               <匹配到第一个<    a>123<a>456都是.*匹配到的 默认是贪婪 能取多少就取多少
#               变成非贪婪 能少取就尽量少取  能少取就少取
#                满足匹配的条件下
data = re.match(r'<.*?>\d{3}',s)
print(data.group())
"""
<a>123
"""








































