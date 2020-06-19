d={'name':'曾贤志','age':54,'sector':'财务部'}
l1=[x+'01' for x in d];print(l1)
l2=[x for x in d.keys()];print(l2)
l3=[x for x in d.values()];print(l3)
l4=[x for x in d.items()];print(l4)
l5=[[x,y] for x,y in d.items()];print(l5)