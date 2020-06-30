"""
演示if分支语句语法格式三
"""

# if 条件:
#     代码片段
# elif:
#     代码片段

# 多种情况的应用场景,,,bobo,,周一到周日,,七天,,七种情况,,七种计划,,
# elif else if 多种情况
day = input('今天是周几:')
if day == '周一':
    print('bobo选择了读书')
elif day == '周二':
    print('bobo选择了看电视')
elif day == '周三':
    print('bobo选择了打游戏')
elif day == '周四':
    print('bobo选择了爬山')
elif day == '周五':
    print('bobo选择了去露营')
elif day == '周六':
    print('bobo选择了学习')
elif day == '周日':
    print('bobo选择了休息')

else: # 前面都不满足 那么我就来执行 可有可无
    print('请按照正规的方式输入')

















































