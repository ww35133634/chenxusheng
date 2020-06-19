def test(s):
    n=s+100
    return n,n+1000,n*6000

print(test(99))

#无参函数
import os
def path():
    p=os.getcwd()
    return p
print(path())


#有参函数
def avg(lit):
    val=sum(lit)/len(lit)
    return val

l=[32,23,52,213]
print(avg(l))
print(avg([34,3,53,46,4,5376,45]))

