class Printer:
    __instance = None  # 用来控制只能创建出一个对象
    __is_init = False  # 用来控制创建一个新的对象时打印任务列表不被初始化
    def __new__(cls, *args, **kwargs):
        # 控制object类里面的new方法的执行来达到控制对象的创建
        if cls.__instance is None:
            cls.__instance = object.__new__(Printer)
        return cls.__instance

    def __init__(self,name):
        '''控制打印机任务列表的初始化'''
        if Printer.__is_init == False:
            self.list1 = []
            Printer.__is_init = True
        self.name = name

    def demo1(self,data):
        """调用方法用来添加打印任务"""
        self.list1.append(data)
        print('我是%s，我把%s添加到了打印机......' % (self.name,data))

    def demo2(self):
        '''调用方法来显示打印机任务'''
        print('打印机里面的任务为：%s' % (self.list1))


man1 = Printer('A')
man1.demo1('陆小凤传奇')
print(id(man1.list1))
man2 = Printer('B')
man2.demo1('小李飞刀')
print(id(man1.list1))

man3 = Printer('C')
man3.demo1('楚留香传奇')
print(id(man1.list1))

print(man3.list1)

print(id(man1))
print(id(man2))
print(id(man3))

