l=[32,32,4,135,34]

# def agg1(list,*subtotal):
#     agg=[x(list) for x in subtotal ]
#     return agg

def agg2(list,**subtotal):
    agg=[(x,y(list)) for x,y in subtotal.items()]
    return agg

print(agg2(l,求和=sum,个数=len,最大值=max))