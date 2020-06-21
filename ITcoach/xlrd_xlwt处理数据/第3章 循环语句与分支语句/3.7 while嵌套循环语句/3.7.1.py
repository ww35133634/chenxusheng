x,y=0,0
while x<9:
    x+=1
    while y<x:
        y+=1
        print('%d×%d=%d\t'%(y,x,x*y),end='')
    y=0
    print('')