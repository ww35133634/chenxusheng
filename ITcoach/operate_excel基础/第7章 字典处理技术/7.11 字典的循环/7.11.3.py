# d={'a':1,'b':3,'c':10}
# print(d)
# d1={ x:y+100 for x,y in d.items()}
# print(d1)


l1=['张三','李四','周立']
l2=[100,90,85]
d2={x:y+100 for x,y in zip(l1,l2)}
print(d2)