"""
演示str方法
"""
class Man: # 这是创建类
    # init方法已经在我们不知道的情况下被调用运行了
    def __init__(self): # 定义完之后是需要调用才能执行里面的代码
        self.gender = "男"
        self.name = None


    def run(self,num1): # 成员方法
        print("跑了%s千米" % num1)

    def sing(self,num2):
        print("唱了%s首歌" % num2)

    def __str__(self):
        return "hello,武汉加油"

man1 = Man() # 创建了一个对象
print(man1) # 对象名被print打印的















































