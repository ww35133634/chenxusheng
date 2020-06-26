l=[32,32,4,135,34]

# def agg1(list,*subtotal):
#     agg=[x(list) for x in subtotal ]
#     return agg

def agg2(list,**subtotal):
    agg=[(x,y(list)) for x,y in subtotal.items()]
    return agg

print(agg2(l,求和=sum,个数=len,最大值=max))


def avg(l: list, **demand):
    print([(x, y(l)) for x, y in demand.items()])


l = [32, 32, 4, 135, 34]
avg(l, 和=sum, 最大值=max, 最小值=min)
