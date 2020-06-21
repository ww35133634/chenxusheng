#例子1-----------------
l=[45,89,67,56,98,81,44]
#推导方式筛选
l1=[x for x in l if x>=80]
print(l1)

#自定义函数筛选
def test1(x):
    return x>=80
l2=filter(test1,l)
print(list(l2))

#匿名函数筛选
l3=filter(lambda x:x>=80,l)
print(list(l3))

#例子2-----------------

s=[[56,88,95],[81],[44,98],[99,87,100,4]]
#推导方式筛选
s1=[x for x in s if len(x)>2];print(s1)

#自定义函数筛选
def test2(x):
    return len(x)>2
s2=filter(test2,s);print(list(s2))

#匿名函数筛选
s3=filter(lambda x:len(x)>2,s);print(list(s3))

#例子3
n=[[89,69],[78,96],[85,99],[96,89]]

#推导方式筛选
n1=[[x,y] for x,y in n if x>y];print(n1)

#自定义函数筛选
def test3(x):
    return x[0]>x[1]
n2=filter(test3,n);print(list(n2))

#匿名函数筛选
n3=filter(lambda x:x[0]>x[1],n);print(list(n3))