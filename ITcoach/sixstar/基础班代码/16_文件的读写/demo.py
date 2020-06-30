
# import requests
#
# url = 'https://www.baidu.com/'
#
# response = requests.get(url)
# # data = response.text.encode('utf-8')  # 得到的是str 编码成二进制
# print(response.encoding)
# data1 = response.content.decode()  # 二进制解码成gbk字符集的字符串
# print(data1)
# with open('baidu.html','w',encoding='utf-8') as file1:
#     # data2 = data1.encode('utf-8')  # gkk字符串 编码成 二进制
#     # data2 = data1.decode('gbk')  # 二进制 解码成 str
#     file1.write(data1)


# import requests
# url = 'https://www.baidu.com/'
# response = requests.get(url)
# # print(response.encoding)
# # print(type(response.text))
# # print(response.text)
# # print(response.encoding)
# # data = response.text
# # with open('baidu.html','w',encoding='utf-8') as file1:
# #     file1.write(data)
# data = response.content
# # print(type(response.content))
# data = data.decode('utf-8')
# with open('baidu.html','w',encoding='utf-8') as file1:
#     file1.write(data)

# import requests
# url = 'https://www.baidu.com/'
# response = requests.get(url)
#
# data = response.content
# print(data.decode('utf-8'))
# with open('baidu.html','wb') as file1:
#     file1.write(data)

# import requests
# url = 'https://www.baidu.com/'
# response = requests.get(url)
# data = response.text
# print(response.encoding)
# print(type(data))
# data = data.encode('ISO-8859-1')
# data = data.decode('utf-8')
# print(data)
#
# with open('baidu.html','w',encoding='utf-8') as file1:
#     file1.write(data)


import requests
url = 'https://www.baidu.com/'
response = requests.get(url)
data = response.content
print(type(data))
# with open('baidu_02.html','wb') as file1:
#     file1.write(data)
print(response.encoding)
