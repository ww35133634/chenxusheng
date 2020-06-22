"""
演示r的作用
"""
import re

demo_data = "c\\\\demo\\\\demo"  # 是一个转义符
print(re.match(r".+",demo_data).group())













