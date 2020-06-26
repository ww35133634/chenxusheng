# l1=list('abcde')
# l2=list()
# print(l2)

# l3=['Google','QQ','Taobao','Baidu']
# l3.reverse()
# print(l3)


# l3=[1,2,3,4,5,6]
# l4=l3
# l5=l3.copy()
# print(id(l3),id(l4),id(l5))



l6=[[1,2,3],[4,5,6]]
print(list(zip(*l6)))


# l7=[1,2,3]
# l8=[4,5,6]
# # l9=['a','b','c']
# print(list(zip(l7,l8)))
# print([[x,y] for x,y  in zip(l7,l8)])