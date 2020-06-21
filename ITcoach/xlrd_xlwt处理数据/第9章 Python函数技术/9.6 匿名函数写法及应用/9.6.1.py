# d=lambda :'test'
# print(d())
# print((lambda :'test')())
#
#
# d1=lambda x,y,z:x+y+z
# print(d1(3,5,6))
# print((lambda x,y,z:x+y+z)(54,2,13))

# d2=lambda x,y,z=100:x+y+z
# print(d2(y=200,x=600))
# print((lambda x,y,z=100:x+y+z)(34,23))


# d3=lambda x,*y:x(y)
# print(d3(sum,5,23,7,1))
# print((lambda x,*y:x(y))(len,34,4,2,436564,66))

# d4=lambda x,**y:[(n,m(x)) for n,m in y.items()]
# print(d4([43,23,3,2,35],求和=sum,最大=max,最小=min))
# print((lambda x,**y:[(n,m(x)) for n,m in y.items()])([43,23,3,2,35],求和=sum,最大=max,最小=min))

# d5=lambda x,y: '成功' if x>y else '失败'
# print(d5(16,9))
