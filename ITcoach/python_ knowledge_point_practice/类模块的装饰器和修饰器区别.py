class A(object):
    def m1(self, n):
        print("self:", self)

    @classmethod
    def m2(cls, n):
        print("cls:", cls)

    @staticmethod
    def m3(n):
        print(n)
# m1 是实例方法，第一个参数必须是 self（约定俗成的）。
# m2 是类方法，第一个参数必须是cls（同样是约定俗成）。
# m3 是静态方法,只是一个函数被放到类内罢了。
a = A()
a.m1(1)  # self: <__main__.A object at 0x000001E596E41A90>
A.m2(1)  # cls: <class '__main__.A'>
A.m3(1)
