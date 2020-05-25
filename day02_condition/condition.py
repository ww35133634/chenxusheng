"""
统计各种字符的数量
str = 'fdsafdsaYYYYdsafd43243243!@^%$#复读机啊发动机范德萨就开了发的撒娇'
大写字母：10个 小写字母：12个  数字：18个
汉字：15     其他字符： 18
思路：需要第字符串中每一个字符进行判断 ， 遍历
重要：在写条件选择的时候，如果条件有互斥性，建议写成if --elif ---elif ---else
"""
str01 = 'fdsafdsaYYYYdsafd43243243!@^%$#复读机啊发动机范德萨就开了发的撒娇'

for s in str01:
    lower_num = 0
    upper_num = 0
    digit_num = 0
    chinese_num = 0
    other_num = 0
    if s.islower:
        lower_num = lower_num + 1
    elif s.isupper():
        upper_num = upper_num + 1
    elif s.isdigit():
        digit_num = digit_num + 1
    elif s >= '\u4e00' and s <= '\u9fa5':
        chinese_num = chinese_num + 1
    else:
        other_num = other_num + 1

    print('在字符串中：小写字母{}个，大写字母{}个，数字{}个，其它字符{}个。'.format(lower_num,upper_num,digit_num,chinese_num,other_num))
