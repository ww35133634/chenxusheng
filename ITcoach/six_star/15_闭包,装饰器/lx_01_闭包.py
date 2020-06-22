"""
演示闭包
"""

# def test1():
#     print("--- in test1 func ---")
#
# # test1 →  {函数}
# # 调用函数
# test1()
#
# # 引用函数 ret → test1 → {函数}
# ret = test1
#
# print(id(ret))
# print(id(test1))
#
# ret()



def func1(a,b):

    def func2(c):
        return a + b + c,id(a),id(b),id(c)

    return func2 # return a + b + c


a = func1(1,1) # a → func2
b = func1(2,2)
print(a(1))
print(b(2))











