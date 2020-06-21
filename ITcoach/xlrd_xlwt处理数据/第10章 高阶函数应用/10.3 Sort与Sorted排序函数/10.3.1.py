# l1=[354,275,3,5,765,43]
# l1.sort();print(l1)
# l1.sort(reverse=True);print(l1)

l2=['张三-98','李四-93','刘飞龙-87','曾贤志-100']
l2.sort(key=lambda x:int(x.split('-')[1]),reverse=True);print(l2)
