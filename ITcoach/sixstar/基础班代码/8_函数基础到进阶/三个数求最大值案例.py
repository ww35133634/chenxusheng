"""
演示三个数求最大值案例
"""
"""
	基于两个数最大值函数完成 三个数字求最大值 函数
	要求:
		任意给出三个数字, 可以得到最大的数字值
	思考:
		1. 选用何种函数的定义格式
		2. 是否具有参数? 如果有设置几个参数
		3. 得到最大值后做什么事情
		4. 是否具有返回值? 如果有返回什么
"""
# 繁杂,,,,
"""
参数+返回值,input,if分支
"""

def max2(a,b):
    if a > b:
        return a
    else:
        return b

def demo(a1,b1,d1):
    # 3个数求最大值
    # 1.前面两个的最大值求出来
    c1 = max2(a1,b1)  # 前面两个数的最大值
    # 2.拿结果跟第三个数进行比较 得到最大值
    return max2(c1,d1)
# 调用demo函数去得到最大值 打印出来

max3 = demo(1,2,3)
print(max3)






























































































































