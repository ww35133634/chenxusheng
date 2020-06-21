# def fact(x):
#     if x==1:
#         return 1
#     else:
#         return x+fact(x-1)
#
# print(fact(5))

def con(l):
    if len(l)==0:
        return ''
    else:
        return con(l[:len(l)-1])+'-'+l[-1]
print(con(['a','b','c','d']))

