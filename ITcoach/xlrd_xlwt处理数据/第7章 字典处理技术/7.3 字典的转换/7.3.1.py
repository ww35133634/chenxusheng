# d1=dict(a=1,b=2)
# print(d1)
#
# d2=dict((('a',1),('b',2)))
# print(d2)
#
# k=['a','b','c']
# v=[1,2,3]
# print(dict(zip(k,v)))

l=[['a','b','c'],[1,2,3]]
print(dict(zip(*l)))

t = (('a','b','c','d'),(1,2,3,4))
print(dict(zip(*t)))
