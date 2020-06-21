# d={'a':1,'b':3,'c':10}
# print(d)
# d1={ x:y+100 for x,y in d.items()}
# print(d1)


l1 = [('张三',5), ('李四',2), ('周立',3)]
l2 = [100, 90, 85]
print(list(zip(l1, l2)))
d2 = {x: y + 100 for x, y in zip(l1, l2)}
print(d2)
