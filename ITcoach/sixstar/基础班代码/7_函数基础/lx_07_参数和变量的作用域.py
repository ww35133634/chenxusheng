"""
演示参数和变量的作用域
"""
# 作用的范围
# 小明
def max2(a,b): # a = 4
    if a > b:
        print(f'{a}跟{b}中,较大值是:', a)
    else:  # a < b   a <= b
        print('%s跟%s中,较大值是:%s' % (a,b,b))
# 小红
def min2(c,d):
    if c > d:
        print(f'{c}跟{d}中,较小值是:', d)
    else:  # a < b   a <= b
        print('%s跟%s中,较小值是:%s' % (c,d,c))
    # print(a)
max2(4,5)
min2(2,3)


# 参数的作用域:形参仅在自己被定义的函数内部有效.





























































































