"""
演示局部导入资源控制
"""
# 局部导入格式下  但是却能全部导入的效果  * 代表的就是模块里面的全部资源
from lx_six777 import *  # * >>>__all__ = ['sixstar1', 'name1']
import lx_six777  # 直接坦诚相对

# ['sixstar1', 'name1']
sixstar1()
print(name1)

# 其实她并不是真正的管控到了,,
# sixstar2(): name2  不包含
sixstar2()
print(name2)

































































