def fun(x):
    return x**2

#方法1
l=[fun(x) for x in [2,4,7,5]]
print(l)

#方法2
print(list(map(fun,[2,4,7,5])))

#方法3
print(list(map(lambda x:x**2,[2,4,7,5])))

#方法
print(list(map(len,['677','89','766756','9871'])))