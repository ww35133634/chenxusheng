for x in range(1,10):
    for y in range(1,x+1):
        print('%d×%d=%-5d'%(y,x,y*x),end='\t')
    print('')