"""
演示new方法
"""
class Man: # object
    def __new__(cls, *args, **kwargs):
        print("new方法被执行......") # 增加功能的操作
        # 调用object的new方法
        instance = object.__new__(Man) # 分配一个内存空间
        return instance

    def __init__(self,name,age):
        print("init方法被执行......")
        self.name = name
        self.age = age


man1 = Man("小明",18)
















































