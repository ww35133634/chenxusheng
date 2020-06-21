# l1=[354,275,3,5,765,43]
# l2=sorted(l1,reverse=True);print(l2)


l3=['张三-98','李-93','刘飞龙g-87','曾贤志-100']
l4=sorted(l3,reverse=True,key=lambda x:len(x.split('-')[0]))
print(l4)