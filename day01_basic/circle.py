"""
根据提供的圆的半径，计算圆的周长和面积
"""

#方法一： 面向过程编程

'''
def check_radius():
    r = input("请输入圆的半径：")
    try:
        radius = float(r)
        return radius
    except Exception as e:
        print(e)

def get_area(radius):
    area = PI * radius ** 2
    return area
def get_perimeter(radius):
    perimeter = PI * radius * 2
    return perimeter

PI = 3.1415926
if __name__ == '__main__':
    radius = check_radius()
    area = get_area(radius)
    perimeter = get_perimeter(radius)
    print("圆的周长是%.2f,面积是%.2f" %(perimeter , area))

'''

#方法二： 面向对象编程
PI = 3.1415926
class Circle_operation:
    # 构造函数
    def __init__(self,radius):
        self.radius = radius
        self.area = 0.0
        self.perimeter = 0.0
        #把函数放入构造函数后可以自动计算周长和面积，便于在主函数内直接调用
        # self.get_perimeter()
        # self.get_area()

    def get_area(self):
        self.area = PI * self.radius ** 2

    def get_perimeter(self):
        self.perimeter = PI * self.radius * 2

if __name__ == '__main__':
    obj01 = Circle_operation(100)
    obj01.get_area()
    obj01.get_perimeter()
    print(obj01.area,obj01.perimeter)
    # print(obj01.perimeter,obj01.area)

