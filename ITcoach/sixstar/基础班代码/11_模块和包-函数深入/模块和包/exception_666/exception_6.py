"""
保存自定义异常类
"""
# 1.自定义异常类
# 作为资源,其他地方也有可能使用,增加资源的复用性
# 是不是减轻本文件的负担
class NameIsError(Exception):
    pass

class PwdIsError(Exception):
    pass
