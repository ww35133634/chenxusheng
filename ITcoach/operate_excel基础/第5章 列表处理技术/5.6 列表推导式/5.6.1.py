# l1=['83','98','91','100']
# l2=[int(x) for x in l1]
# print(l2)

# l2=[[98,86,74,85],[96,99,75,92],[69,93,87,85]]
# l3=[x for l in l2 for x in l]
# l4=[[x+100 for x in l] for l in l2]
# print(l4)


# l5=[85,68,98,74,95,82,93,88,74]
# l6=[x for x in l5 if x>=90]
# print(l6)


l7=[1,2,3]
l8=[ [x,y] for x in l7 for y in l7 if x!=y]
print(l8)