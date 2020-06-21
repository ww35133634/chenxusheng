ll=[['a',1,1],['b',3,1],['c',5,10],['a',1,10],['c',1,10]]

def distinct(l,num=1):
    return {x[num] for x in l}

print(distinct(ll,0))
