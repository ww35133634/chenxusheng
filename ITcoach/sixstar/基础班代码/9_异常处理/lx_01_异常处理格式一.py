"""
演示异常处理格式一
"""

# try:
#     # 有可能会引发异常的代码
#     demo = 123
#     print(demo)
# except:  # 如果try里面的代码出现了异常,那么就直接跳到except里面执行,,没有出现异常,就不跳
#     # 把被try管控着的代码,,一旦出现异常
#     print('bobo老师帮助你,思思也可以帮助你')




try:
    # 有可能会引发异常的代码

    demo = 123
    print(demo)
    # a = 456
    print(a)  # 因为被try管辖,,一旦出错就直接跳到except里面去执行,并且之后的代码都不执行
    b = 789
    print(b)
except:  # 如果try里面的代码出现了异常,那么就直接跳到except里面执行,,没有出现异常,就不跳
    # 把被try管控着的代码,,一旦出现异常
    print('bobo老师帮助你,思思也可以帮助你')




























































































































