# 字符串的常用方法
s='aNc'
q='1+2+3\n1+2+3+4'
a='mysql is is db'
# m=s.find('z') # 找不存在的元素，find会返回-1
# m=s.index('z')   #  找不存在的元素，index报错
# m=s.count('z')  # 计数
# print(len(a))
# m=a.rfind('db') #返回最右边字符的下标
# m=s.upper()   # #变成大写
# m=s.lower()   #变成小写
# m=s.swapcase() #大小写反转
# m=s.capitalize() #首字母大写
# m=s.split(',')   # 以，位分隔符，返回list
# m=q.splitlines()#按照换行符分割
# m=s.strip('abc') #去除“abc”
# m=s.lstrip()   ##默认去掉左边的空格和换行
# m=s.rstrip()    ##默认去掉右边的空格和换行
# m=s.replace('a','b')  # 替换
# m=s.endswith('xxx.mp3')     #判断时候xxx.mp3结尾
# m=s.startswith('186')    #判断时候186开头
# m=','.join(['sername','user2','user3'])    #1、把list变成了字符串 2、把list里面每一个元素用逗号连接起来
#                                     # username,user2,user3
# print('+'.join(['hehe', 'haha', 'ee']))  # 拼接字符串     hehe+haha+ee
# m=s.isdigits()  ##判断是否为正整数
# m=s.isalpha() #是否是英文字母
# m=s.isalnum()  #是否包含数字和字母
# m=s.zfill(5)  # 位数不足5位时，自动补零
# m=s.isidentifier() #是否是一个合法的变量名
# m=s.istitle() #是不是一个标题，判断首字母是否大写
# m=s.isidentifier())#是否是一个合法的变量名
# m=a.rfind('is')#返回最右边字符的下标
# print(m)

# # 字符串
# str = 'Hello Python'
#
# # 1. 输出完整字符串
# print("完整字符串--" + str)
# # 结果输出:
#
# # 2. 输出第一个字符
# print("第一个字符--" + str[0])
#
# # 3. 输出第三到七个字符
# print("第3-7个字符--" + str[2:6])
#
# # 4. 输出低2个字符开始的所有字符
# print("第2个开始的所有字符--" + str[1:])
#
# # 5. 拼接字符串
# # 像上面一样, 字符串用 `+`拼接
# print("拼接--" + str)
#
# # 6. 输出3次
# # `*` 表示重复操作, 需要重复操作几次, 后面跟上次数即可
# print(str * 3)
#
# # 7. 输出最后一个字符
# print("最后一个字符--" + str[-1])
#
# # 8. 输出倒数第二个字符
# print("倒数第二个字符--" + str[-2])

# password='jpg 12345456789 .jpg ABCDE'

# 输出结果 ：jpg 12345456789 .jpg ABCDE
# new_password = password.strip()  # 默认去掉字符串两边的空格
# new_password = password.strip('\n')  # 默认去掉字符串两边换行符
# new_password = password.strip('.jpg') # 默认去掉字符串两边的指定去掉字符串
# print(new_password)
# print(password.lstrip()) # 左边的
# print(password.rstrip()) # 右边的
# print('password',password)
# print('newpassword',new_password)
# print(password.upper()) # 转成大写的
# print(password.lower()) # 转成小写的
# print(password.capitalize()) # 吧首字母改成大写的
# print(password.count('jpg')) # 计算指定字符的在字符串中的次数
# print(password.replace('9','上山打老虎')) # 替换字符串

# List 列表
# list1 = [12, 34, 3.14, 5.3, 'titan']
# list2 = [10, 'jun']

# 1.完整列表
# print(list1)

# 2.列表第一个元素
# print(list1[0])

# 3.获取第2-3个元素
# print(list1[1:3])

# 4.获取第三个到最后的所有元素
# print(list1[2:])

# 5.获取最后一个元素
# print(list1[-1])

# 6.获取倒数第二个元素
# print(list1[-2])

# 7.获取最后三个元素
# print(list1[-3:])

# 8.合并列表
# print(list1 + list2)

# 9.重复操作两次
# print(list2 * 2)
# 增加列表元素
# stu_name = ['哈华','呢呢','心',1,1.5]
# print(stu_name)
# stu_name.append('小月')  # 在list的末尾添加一个元素
# stu_name.insert(0,'小军')  # 指定位置添加元素
# stu_name.insert(0,'小军')  # 指定位置再添加元素
# print('修改之后的',stu_name)

# 修改列表元素
# stu_name = ['哈华','呢呢','心',1,1.5,'强']
# stu_name[5]='花花'
# print('修改之后的 %s' %stu_name)
# print("修改之后的{}".format(stu_name))

# 删
stu_name = ['哈华','呢呢','心',1,1.5,'强' ,'小军']

# stu_name.pop()  # 删除最后一个元素
# print("删除后：",stu_name)
# stu_name.pop(4)  # 删除指定下标的元素
# print("删除后：",stu_name)
# stu_name.append('小军')  # 先增加一个小军
# print(stu_name)
# stu_name.remove('小军')  # 删除指定的元素，如果有一样的元素，只会删除第一个
# stu_name.pop(1)  # 删除指定下标的元素,删除不存在的元素会报错
# print(stu_name)
# del stu_name[-1]  # 下标、索引、如果是正数就从左边开始算起，如果是负数，则从后面开始数起，倒序
# print(stu_name)

#  查
my_list = ['小黑','小白',1,1,2,1.5]
# print(my_list[-1])
# print(my_list[0])
# print(my_list.count(5))     # 查询某个元素在list里面出现的次数
# print('index方法：',my_list.index(1))     # 查找元素的下标，元素不存在的话，会报错
# print('reverse:%s' %my_list.reverse())     # reverse是反转list
# print(my_list)
# my_list.clear()#清空整个list
# print(my_list)

# nums =[9.23,9,3,6,1,0]
# nums.sort() # 排序，升序
# nums.sort(reverse=True)    # 排序,如果指定了reverse=True，那么就是降序
# # nums.extend(my_list)#把一个list里面的元素加入进去
# print(nums)
# new_list = nums + my_list + stu_name
# # extend是把列表本身变化了，而直接
# # 两个列表相加的话，列表本身没有变化，只是相加的结果存在一个新的列表里面
# print(new_list)
# print(new_list * 3)    # 复制几个
# 函数表达式                   输出结果                描述
# len(list1)                   3                  列表元素个数
# max([1, 2, 's'])             s                  返回列表元素的最大值
# min([1, 2, 's'])             1                  返回列表元素的最小值
# list(('q', 1)             ['q', 1]              将元组转换为列表
# list1.append(2)           [1, 2, 3, 2]          在列表末尾添加新的对象
# list1.count(2)               2                  统计某个元素在列表中出现的次数
# list1.index(3)               2                  从列表中找出某个值第一个匹配项的索引位置
# list1.insert(1, 'jun')    [1, 'jun', 2, 3, 2]   将对象插入列表的指定位置
# list1.remove(3)         [1, 'jun', 2, 2]        移除列表中某个值的第一个匹配项
# list1.reverse()         [2, 2, 'jun', 1]        对列表的元素进行反向排列
# list1.sort()            [2, 2, 'jun', 1]         对原列表进行排序, 如果指定参数，则使用比较函数指定的比较函数
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         st = "{}X{}={}".format(j, i, i * j)
#         print(st,end=' ')
#         j += 1
#     i += 1
#     print()
sr = ""
for i in range(20,30):
    for j in range(20,1+i):
        st = "{}X{}={}".format(j, i, i * j)
        sr = sr + " " + st
    print(sr,end="\n")
    sr = ""

