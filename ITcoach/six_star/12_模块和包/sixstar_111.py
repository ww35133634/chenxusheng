"""
演示模块的定义
"""
__all__ = ["i","a"]

# 类
class Six():
    @classmethod
    def say(cls):
        print("我是一个类呀")

# 函数
def six():
    print("hello, 武汉加油")

# 全局变量
i = 'sixstar_111'
a = "hello, 周黑鸭加油"

if __name__ == "__main__": # 来判断运行环境是否是自己的环境
#     # 测试代码, 其他的代码
    print("这是一段测试代嘛 里面有什么东西  你可以去用")

# print(__name__) # __name__ = "__main__"


# 这样一个设置,,就可以过滤掉一些我们对外提供的资源(代码)















